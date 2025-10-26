from .worker import Worker


class QualityController(Worker):
    def __init__(self, name: str):
        super().__init__(name, "Контролёр качества", 38.0)

    def test_concrete(self, sample: str) -> str:
        return "Прочность: 35 МПа"

    def approve_material(self, material) -> None:
        material.approved = True