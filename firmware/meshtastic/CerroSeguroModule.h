// SPDX-License-Identifier: GPL-3.0-only
#pragma once
#include "SinglePortModule.h"
#include "SosState.h"
#include "concurrency/OSThread.h"

class CerroSeguroModule : public SinglePortModule, private concurrency::OSThread {
  public:
    CerroSeguroModule();

  protected:
    int32_t runOnce() override;
    ProcessMessage handleReceived(const meshtastic_MeshPacket &packet) override;

  private:
    cerroseguro::SosState state;
    bool initialized = false;
    uint32_t bootNonce[2] = {};
    uint32_t sequence = 0;
    char eventId[25] = {};
    void sendSos();
};
