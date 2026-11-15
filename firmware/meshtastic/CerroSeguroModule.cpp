// SPDX-License-Identifier: GPL-3.0-only
#ifdef CERRO_SEGURO_SOS
#include "CerroSeguroModule.h"
#include "SosProtocol.h"
#include "HardwareRNG.h"
#include "MeshService.h"
#include "NodeDB.h"
#include "configuration.h"
#include <Arduino.h>
#include <cstdio>
#include <cstring>

#ifndef CS_STATION_NODE
#define CS_STATION_NODE 0
#endif
#ifndef CS_SOS_PIN
#define CS_SOS_PIN 31
#endif
#ifndef CS_CHANNEL
#define CS_CHANNEL 0
#endif
#ifndef CS_ACK_TIMEOUT_MS
#define CS_ACK_TIMEOUT_MS 60000
#endif
#ifndef CS_MAX_ATTEMPTS
#define CS_MAX_ATTEMPTS 3
#endif

#if CS_SOS_PIN == 31 && !MESHTASTIC_EXCLUDE_DROPZONE
#error "AIN1/GPIO31 requires the Dropzone module to remain disabled"
#endif

static_assert(CS_STATION_NODE != 0xffffffff, "Station must be a unicast destination");
static_assert(CS_ACK_TIMEOUT_MS > 0 && CS_ACK_TIMEOUT_MS < 0x80000000UL, "Invalid timeout");
static_assert(CS_MAX_ATTEMPTS > 0 && CS_MAX_ATTEMPTS <= 5, "Invalid attempt limit");

CerroSeguroModule::CerroSeguroModule()
    : SinglePortModule("cerroseguro", meshtastic_PortNum_TEXT_MESSAGE_APP),
      concurrency::OSThread("cerroseguro"), state(40, 2000, CS_ACK_TIMEOUT_MS, CS_MAX_ATTEMPTS) {}

int32_t CerroSeguroModule::runOnce() {
    if (!initialized) {
        initialized = true;
        if (CS_STATION_NODE == 0 || CS_STATION_NODE == nodeDB->getNodeNum()) {
            LOG_WARN("CS SOS disabled: configure destination station NodeID");
            return disable();
        }
        pinMode(CS_SOS_PIN, INPUT_PULLUP);
        if (!HardwareRNG::fill(reinterpret_cast<uint8_t *>(bootNonce), sizeof(bootNonce))) {
            LOG_ERROR("CS SOS disabled: random event identifier unavailable");
            return disable();
        }
        state.begin(millis(), digitalRead(CS_SOS_PIN) == LOW);
        LOG_INFO("CS SOS ready pin=%u destination=%08lx", CS_SOS_PIN, (unsigned long)CS_STATION_NODE);
    }
    const auto before = state.getStatus();
    const uint32_t now = millis();
    if (state.sample(now, digitalRead(CS_SOS_PIN) == LOW)) {
        ++sequence;
        snprintf(eventId, sizeof(eventId), "%08lx%08lx%08lx", (unsigned long)bootNonce[0],
                 (unsigned long)bootNonce[1], (unsigned long)sequence);
        LOG_INFO("CS SOS WAITING event=%s", eventId);
    }
    if (state.sendDue(now))
        sendSos();
    if (before != state.getStatus() && state.getStatus() == cerroseguro::SosStatus::Unconfirmed)
        LOG_WARN("CS SOS UNCONFIRMED event=%s attempts=%u", eventId, state.getAttempts());
    return 10;
}

void CerroSeguroModule::sendSos() {
    char payload[40];
    snprintf(payload, sizeof(payload), "CS1|SOS|%s", eventId);
    auto packet = allocDataPacket();
    packet->to = CS_STATION_NODE;
    packet->channel = CS_CHANNEL;
    // Application retries use a stable event ID and a fresh Meshtastic packet ID.
    // Delivery is confirmed only after the station commits the alert to storage.
    packet->want_ack = false;
    packet->decoded.want_response = false;
    packet->decoded.payload.size = strlen(payload);
    memcpy(packet->decoded.payload.bytes, payload, packet->decoded.payload.size);
    service->sendToMesh(packet);
    LOG_INFO("CS SOS TX event=%s attempt=%u", eventId, state.getAttempts());
}

ProcessMessage CerroSeguroModule::handleReceived(const meshtastic_MeshPacket &packet) {
    if (state.getStatus() != cerroseguro::SosStatus::Waiting)
        return ProcessMessage::CONTINUE;
    const auto &payload = packet.decoded.payload;
    if (cerroseguro::matchesRegistration(packet.from, packet.to, packet.channel, payload.bytes,
                                        payload.size, eventId, CS_STATION_NODE, nodeDB->getNodeNum(), CS_CHANNEL)) {
        state.registered();
        LOG_INFO("CS SOS REGISTERED event=%s station=%08lx", eventId, (unsigned long)packet.from);
    }
    return ProcessMessage::CONTINUE;
}
#endif
