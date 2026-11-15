// SPDX-License-Identifier: GPL-3.0-only
#pragma once
#include <cstdint>

namespace cerroseguro {
enum class SosStatus { Idle, Waiting, Registered, Unconfirmed };

// All elapsed-time comparisons remain valid across the millis() rollover.
class SosState {
  public:
    SosState(uint32_t debounceMs = 40, uint32_t holdMs = 2000,
             uint32_t ackTimeoutMs = 60000, unsigned maxAttempts = 3)
        : debounceMs(debounceMs), holdMs(holdMs), ackTimeoutMs(ackTimeoutMs), maxAttempts(maxAttempts) {}

    void begin(uint32_t now, bool pressed) {
        raw = stable = pressed;
        rawSince = pressedSince = now;
        armed = false; // A button held during boot must be released first.
    }

    bool sample(uint32_t now, bool pressed) {
        if (pressed != raw) {
            raw = pressed;
            rawSince = now;
            pressedSince = now;
        }
        if (raw != stable && elapsed(now, rawSince) >= debounceMs) {
            stable = raw;
            if (stable) {
                pressedSince = now;
                if (status == SosStatus::Waiting)
                    armed = false;
            }
        }
        if (!raw && !stable && elapsed(now, rawSince) >= debounceMs)
            armed = true;
        // An observed release cancels the hold even before it is debounced.
        if (raw && stable && armed && elapsed(now, rawSince) >= debounceMs && elapsed(now, pressedSince) >= holdMs) {
            armed = false;
            if (status != SosStatus::Waiting) {
                status = SosStatus::Waiting;
                attempts = 0;
                return true;
            }
        }
        return false;
    }

    bool sendDue(uint32_t now) {
        if (status != SosStatus::Waiting)
            return false;
        if (attempts && elapsed(now, lastSent) < ackTimeoutMs)
            return false;
        if (attempts >= maxAttempts) {
            status = SosStatus::Unconfirmed;
            return false;
        }
        ++attempts;
        lastSent = now;
        return true;
    }

    bool registered() {
        if (status != SosStatus::Waiting)
            return false;
        status = SosStatus::Registered;
        return true;
    }

    SosStatus getStatus() const { return status; }
    unsigned getAttempts() const { return attempts; }

  private:
    static uint32_t elapsed(uint32_t now, uint32_t then) { return now - then; }
    const uint32_t debounceMs, holdMs, ackTimeoutMs;
    const unsigned maxAttempts;
    bool raw = false, stable = false, armed = false;
    uint32_t rawSince = 0, pressedSince = 0, lastSent = 0;
    unsigned attempts = 0;
    SosStatus status = SosStatus::Idle;
};
} // namespace cerroseguro
