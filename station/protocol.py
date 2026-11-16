"""Cerro Seguro text messages carried by Meshtastic TEXT_MESSAGE_APP."""
import re

SOS = re.compile(r"CS1\|SOS\|([0-9a-f]{24})", re.ASCII)


def parse_sos(text):
    if not isinstance(text, str):
        return None
    match = SOS.fullmatch(text)
    return match.group(1) if match else None


def acknowledgement(event_id):
    if not isinstance(event_id, str) or not re.fullmatch(r"[0-9a-f]{24}", event_id, re.ASCII):
        raise ValueError("Invalid event identifier")
    return f"CS1|ACK|{event_id}|REGISTRADO"
