class Trainer:
    TRAINER_ID = 1

    def __init__(self, name):
        self.name = name
        self.id = self.get_next_id()

    @staticmethod
    def get_next_id():
        id = Trainer.TRAINER_ID
        Trainer.TRAINER_ID += 1
        return id

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"