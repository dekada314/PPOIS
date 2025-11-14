Worker 9 4 ->  ToolAssignment   
Foreman 4 1 -> Worker, Task, Assignment   
Driver 5 2 ->    
Engineer 3 2 -> Project   
Architect 3 2 -> Project   
Electrician 3 2 -> Task   
Plumber 3 2 -> Task   
CraneOperator 4 2 -> Material   
SafetyInspector 4 3 -> Worker, Project   
LogisticsCoordinator 3 2 ->   
SiteSupervisor 4 2 ->   
QualityController 3 2 ->   
Surveyor 3 1 -> Project   

BankCard 5 2   
Contract 7 3 -> Project  
Salary 7 4 -> Worker   
Invoice 6 2 -> Project   
Payment 5 1 -> Invoice   
Budget 5 3 -> Project   
ExpenseReport 5 2 -> Worker   
TaxDocument 4 1   
InsurancePolicy 5 2 ->   
Tender 4 2 -> Project   
Estimate 4 2 -> Project   
PurchaseOrder 4 2 ->    

Storage 4 4 -> Material, Task, MaterialUsage   
FleetManager 3 2 -> Driver, Vehicle  
HRManager 3 3 -> Worker   
ProcurementManager 4 2 -> PurchaseOrder  
ITManager 3 1 ->   
LegalAdvisor 3 1 -> Contract   
Accountant 3 1 ->   
PayrollSpecialist 3 1 -> Salary  
ChiefManager 4 3 -> Project   
GeneralManager 4 1 ->    
Safety_manager 4 3 -> Worker   

Project 12 4 -> Estimate, Budget, Milestone   
Task 10 3 -> Worker, Project   
Milestone 6 2 -> Task   
Timeline 2 1 -> Project  
RiskAssessment 3 2 -> Project  
ChangeRequest 4 2 -> Project  
ProgressReport 3 1 -> Task  

Tool 5 3 -> Worker, ToolAssignment  
Material 6 2 -> Storage, PurchaseOrder, MaterialUsage  
Vehicle 5 4 -> Driver, FleetManager  
Equipment 5 3 -> InsurancePolicy  

Assignment 6 1 -> Worker, Task  
MaterialUsage 5 0 -> Material, Task  
ToolAssignment 5 1 -> Tool, Worker  
  
Поля: 226  
Поведения: 103  
Ассоциации: 54  
