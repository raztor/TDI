#include "SosState.h"
#include "SosProtocol.h"
#include <cassert>
#include <cstdint>
#include <iostream>
using cerroseguro::SosState;
using cerroseguro::SosStatus;

static uint32_t hold(SosState &s, uint32_t now) {
    assert(!s.sample(now, true));
    assert(!s.sample(now + 40, true));
    assert(!s.sample(now + 2039, true));
    assert(s.sample(now + 2040, true));
    return now + 2040;
}

int main() {
    SosState s;
    s.begin(0, false);
    s.sample(40, false);
    // Contact bounce and a brief pulse never generate an alert.
    s.sample(100, true);
    s.sample(120, false);
    assert(!s.sample(160, false));
    assert(s.getStatus() == SosStatus::Idle);
    uint32_t t = hold(s, 200);
    assert(s.sendDue(t));
    assert(!s.sendDue(t + 59999));
    assert(!s.sample(t + 10000, true)); // Holding does not generate a second event.
    assert(s.sendDue(t + 60000));
    assert(s.sendDue(t + 120000));
    assert(!s.sendDue(t + 180000));
    assert(s.getStatus() == SosStatus::Unconfirmed);
    assert(!s.registered()); // Late responses cannot confirm a timed-out event.
    s.sample(t + 180010, false);
    s.sample(t + 180050, false);
    t = hold(s, t + 180060);
    assert(s.sendDue(t));
    assert(s.registered());
    assert(!s.sendDue(t + 60000));
    assert(s.getStatus() == SosStatus::Registered);

    SosState bootHeld;
    bootHeld.begin(0, true);
    assert(!bootHeld.sample(5000, true));
    bootHeld.sample(5010, false);
    bootHeld.sample(5050, false);
    hold(bootHeld, 5060);

    SosState wrap;
    const uint32_t start = UINT32_MAX - 1000;
    wrap.begin(start, false);
    wrap.sample(start + 40, false);
    t = hold(wrap, start + 100);
    assert(wrap.sendDue(t));
    assert(wrap.sendDue(t + 60000));

    SosState busy;
    busy.begin(0, false);
    busy.sample(40, false);
    t = hold(busy, 100);
    busy.sendDue(t);
    busy.sample(t + 10, false);
    busy.sample(t + 50, false);
    busy.sample(t + 100, true);
    busy.sample(t + 140, true); // A new press while waiting is ignored.
    busy.registered();
    assert(!busy.sample(t + 3000, true));

    SosState interrupted;
    interrupted.begin(0, false);
    interrupted.sample(40, false);
    interrupted.sample(100, true);
    interrupted.sample(140, true);
    interrupted.sample(2000, false); // Even a brief release interrupts the hold.
    interrupted.sample(2020, true);
    assert(!interrupted.sample(2140, true));
    assert(interrupted.sample(4020, true));

    const char *id = "0123456789abcdef00000001";
    const char *ack = "CS1|ACK|0123456789abcdef00000001|REGISTRADO";
    auto data = reinterpret_cast<const uint8_t *>(ack);
    auto length = strlen(ack);
    assert(cerroseguro::matchesRegistration(2, 1, 0, data, length, id, 2, 1, 0));
    assert(!cerroseguro::matchesRegistration(3, 1, 0, data, length, id, 2, 1, 0));
    assert(!cerroseguro::matchesRegistration(2, 3, 0, data, length, id, 2, 1, 0));
    assert(!cerroseguro::matchesRegistration(2, 1, 1, data, length, id, 2, 1, 0));
    assert(!cerroseguro::matchesRegistration(2, 1, 0, data, length - 1, id, 2, 1, 0));
    assert(!cerroseguro::matchesRegistration(2, 1, 0, data, length, "0123456789abcdef00000002", 2, 1, 0));
    std::cout << "SOS state: debounce, hold, retries, ACK, boot, busy and rollover passed\n";
}
