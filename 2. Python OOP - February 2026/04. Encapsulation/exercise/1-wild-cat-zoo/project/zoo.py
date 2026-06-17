class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if len(self.animals) >= self.__animal_capacity:
            return "Not enough space for animal"

        if price > self.__budget:
            return "Not enough budget"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
    
    def hire_worker(self, worker):
        if len(self.workers) >= self.__workers_capacity:
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"
    
    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"
    
    def pay_workers(self):
        total_salaries = sum(worker.salary for worker in self.workers)

        if total_salaries > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= total_salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"
    
    def tend_animals(self):
        total_care = sum(animal.money_for_care for animal in self.animals)

        if total_care > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= total_care
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
    
    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"
        lions = [repr(a) for a in self.animals if a.__class__.__name__ == "Lion"]
        tigers = [repr(a) for a in self.animals if a.__class__.__name__ == "Tiger"]
        cheetahs = [repr(a) for a in self.animals if a.__class__.__name__ == "Cheetah"]

        result += f"----- {len(lions)} Lions:\n"
        result += "\n".join(lions) + "\n"
        result += f"----- {len(tigers)} Tigers:\n"
        result += "\n".join(tigers) + "\n"
        result += f"----- {len(cheetahs)} Cheetahs:\n"
        result += "\n".join(cheetahs)

        return result
    
    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"
        keepers = [repr(w) for w in self.workers if w.__class__.__name__ == "Keeper"]
        caretakers = [repr(w) for w in self.workers if w.__class__.__name__ == "Caretaker"]
        vets = [repr(w) for w in self.workers if w.__class__.__name__ == "Vet"]

        result += f"----- {len(keepers)} Keepers:\n"
        result += "\n".join(keepers) + "\n"
        result += f"----- {len(caretakers)} Caretakers:\n"
        result += "\n".join(caretakers) + "\n"
        result += f"----- {len(vets)} Vets:\n"
        result += "\n".join(vets)

        return result