Patient 3 2 → MedicalRecord
MedicalRecord 3 2 → Diagnosis
Doctor 4 2 → 
Appointment 6 2 → Patient
Prescription 7 2 → Medication, Doctor
Medication 4 2 → 
Diagnosis 4 2 → Doctor                      42,20 6
Hospital 4 2 → 
Insurance 4 2 → 
VitalSigns 4 2 →

Pharmacy 4 2 → Inventory
Inventory 2 4 → 
Drug 4 1 → 
Batch 3 2 → 
Pharmacist 3 2 → 
RefillRequest 3 2 → Patient         
Supplier 4 1 → Order                    30, 21, 3
Order 4 2 → 
DispenseLog 1 2 → 
PriceCalculator 2 3 → 

Lab 4 2 → Sample
Sample 5 2 → Test
Test 4 2 → 
TestResult 5 1 → Sample, Test               34, 17, 7
Analyzer 3 2 → Sample
Technician 4 1 → Sample
Report 3 2 → Sample
QualityControl 2 2 → 
ReferenceRange 4 1 → 
EquipmentLog 1 2 → 

Invoice 5 4 → BillingItem
BillingItem 4 2 → 
Payment 4 3 → Invoice
InsuranceClaim 3 4 → Invoice
BillingService 3 4 →                        35,29 6
Account 4 3 → Invoice
DiscountPolicy 3 2 → 
AuditLog 1 3 → 
Statement 4 2 → Account
Refund 4 2 → Invoice

Schedule 4 2 → TimeSlot
TimeSlot 3 2 → 
Appointment 4 1 → TimeSlot
DoctorAvailability 4 1 → TimeSlot
Notification 3 1 → Appointment              30, 15, 8
Room 4 2 → 
Booking 3 1 → Appointment, Room
Calendar 1 2 → 
Reminder 3 1 → Appointment
WaitingList 1 2 → TimeSlot

Поля: 171	
Поведения : 102	
Ассоциации: 30	
Исключения: 12	