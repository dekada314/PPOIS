from lab3.module_appointment.time_slot import TimeSlot
from lab3.module_appointment.waiting_list import WaitingList


def test_add_and_find_match():
    wl = WaitingList()
    slot1 = TimeSlot("2025-11-15T17:00:00", 30)
    slot2 = TimeSlot("2025-11-15T18:00:00", 30)
    
    wl.add("P303", slot1)
    wl.add("P404", slot1)
    wl.add("P505", slot2)
    
    matches = wl.find_match(slot1)
    assert len(matches) == 0
    