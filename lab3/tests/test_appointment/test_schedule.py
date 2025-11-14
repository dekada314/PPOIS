from lab3.module_appointment.schedule import Schedule
from lab3.module_appointment.time_slot import TimeSlot

def test_add_slot_and_available():
    sched = Schedule("SCH001", "D123")
    slot1 = TimeSlot("2025-11-15T10:00:00", 30)
    slot2 = TimeSlot("2025-11-15T10:30:00", 30)
    sched.add_slot(slot1)
    sched.add_slot(slot2)
    
    assert len(sched.slots) == 2
    assert len(sched.available_slots()) == 2
    
    slot1.book()
    assert len(sched.available_slots()) == 1