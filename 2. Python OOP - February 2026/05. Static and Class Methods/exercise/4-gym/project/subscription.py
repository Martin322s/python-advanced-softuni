class Subscription:
    SUBSCRIPTION_ID = 1

    def __init__(self, date, customer_id, trainer_id, exercise_id):
        self.date = date
        self.customer_id = customer_id
        self.trainer_id = trainer_id
        self.exercise_id = exercise_id
        self.id = self.get_next_id()

    @staticmethod
    def get_next_id():
        id = Subscription.SUBSCRIPTION_ID
        Subscription.SUBSCRIPTION_ID += 1
        return id
    
    def __repr__(self):
        return f"Subscription <{self.id}> on {self.date}"