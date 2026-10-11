"""Emit only the agreed bimonthly Memory-Review reminder; never edit memory."""
from datetime import datetime
from zoneinfo import ZoneInfo


MESSAGE = (
    "Björn und Josie: Zeit für unseren gemeinsamen Memory-Pending-Review. "
    "Bitte die Memory-Review-Session öffnen, aktuelle Vorschläge gemeinsam "
    "besprechen und Änderungen nur nach Freigabe übernehmen."
)


def reminder(now=None):
    now = now or datetime.now(ZoneInfo("Europe/Berlin"))
    if now.date().isoformat() < "2026-12-01":
        return ""
    if now.month % 2 == 0 and now.day <= 7 and now.weekday() == 5:
        return MESSAGE
    return ""


if __name__ == "__main__":
    text = reminder()
    if text:
        print(text)
