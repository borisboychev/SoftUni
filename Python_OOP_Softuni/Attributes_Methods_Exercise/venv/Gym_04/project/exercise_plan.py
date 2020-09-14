class ExercisePlan:
    autoincremental_id = 1

    def __init__(self, trainer_id: int, equipment_id: int, duration: int):
        self.trainer_id = trainer_id
        self.eqipment_id = equipment_id
        self.duration = duration
        self.id = ExercisePlan.autoincremental_id
        ExercisePlan.autoincremental_id += 1

    @classmethod
    def from_hours(cls, trainer_id: int, equipment_id: int, hours: int):
        return cls(trainer_id, equipment_id, hours*60)

    @staticmethod
    def get_next_id():
        return ExercisePlan.autoincremental_id

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"