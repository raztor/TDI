// SPDX-License-Identifier: GPL-3.0-only
#pragma once
#include <cstddef>
#include <cstdint>
#include <cstdio>
#include <cstring>

namespace cerroseguro {
inline bool matchesRegistration(uint32_t sender, uint32_t recipient, unsigned channel,
                                const uint8_t *payload, size_t size, const char *event,
                                uint32_t station, uint32_t local, unsigned expectedChannel) {
    if (sender != station || recipient != local || channel != expectedChannel)
        return false;
    char expected[64];
    const int length = snprintf(expected, sizeof(expected), "CS1|ACK|%s|REGISTRADO", event);
    return length > 0 && static_cast<size_t>(length) < sizeof(expected) &&
           size == static_cast<size_t>(length) && memcmp(payload, expected, size) == 0;
}
} // namespace cerroseguro
