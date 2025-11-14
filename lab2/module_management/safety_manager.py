from module_employee.worker import Worker

class SafetyManager:
    def __init__(self, name):
        self.name = name
        self.position = "Менеджер по безопасности"
        self.inspections = []
        self.incidents = []

    def conduct_inspection(self, worker):
        self.inspections.append(worker)
        print(f"Проверка безопасности для {worker.name} проведена.")

    def report_incident(self, description):
        self.incidents.append(description)
        print(f"Инцидент зарегистрирован: {description}")

    def get_safety_score(self):
        if not self.inspections:
            return 100
        return max(0, 100 - len(self.incidents) * 10)