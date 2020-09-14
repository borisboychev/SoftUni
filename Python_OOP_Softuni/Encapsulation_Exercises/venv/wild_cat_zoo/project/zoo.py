from project.tiger import Tiger
from project.lion import Lion
from project.cheetah import Cheetah
from project.caretaker import Caretaker
from project.vet import Vet
from project.keeper import Keeper

class Zoo:

    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.animals = []
        self.workers = []
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity

    def add_animal(self, animal, price):
        if self.__budget > price:
            if self.__animal_capacity > 0:
                self.animals.append(animal)
                self.__budget -= price
                self.__animal_capacity -= 1
                return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
            else:
                return "Not enough space for animal"
        else:
            return "Not enough budget"

    def hire_worker(self, worker):
        if not self.__workers_capacity <= len(self.workers):
            self.workers.append(worker)
            #self.__workers_capacity -= 1
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        if worker_name in [x.name for x in self.workers]:
            worker_to_remove = [x for x in self.workers if x.name == worker_name][0]
            self.workers.remove(worker_to_remove)
            #self.__workers_capacity += 1
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        summed_salaries = 0

        for worker in self.workers:
            summed_salaries += worker.salary

        if summed_salaries <= self.__budget:
            self.__budget -= summed_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        sum_tended_animals = 0

        for animal in self.animals:
            sum_tended_animals += animal.get_needs()

        if sum_tended_animals <= self.__budget:
            self.__budget -= sum_tended_animals
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"
        result += f"----- {len([x for x in self.animals if x.__class__.__name__ == 'Lion'])} Lions:\n"
        for lion in [x for x in self.animals if x.__class__.__name__ == 'Lion']:
            result += f"{lion.__repr__()}\n"

        result += f"----- {len([x for x in self.animals if x.__class__.__name__ == 'Tiger'])} Tigers:\n"
        for tiger in [x for x in self.animals if x.__class__.__name__ == 'Tiger']:
            result += f"{tiger.__repr__()}\n"

        result += f"----- {len([x for x in self.animals if x.__class__.__name__ == 'Cheetah'])} Cheetahs:\n"
        for cheetah in [x for x in self.animals if x.__class__.__name__ == 'Cheetah']:
            result += f"{cheetah.__repr__()}"

        return result

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"
        result += f"----- {len([x for x in self.workers if x.__class__.__name__ == 'Keeper'])} Keepers:\n"
        for keeper in [x for x in self.workers if x.__class__.__name__ == 'Keeper']:
            result += f"{keeper.__repr__()}\n"

        result += f"----- {len([x for x in self.workers if x.__class__.__name__ == 'Caretaker'])} Caretakers:\n"
        for caretaker in [x for x in self.workers if x.__class__.__name__ == 'Caretaker']:
            result += f"{caretaker.__repr__()}\n"

        result += f"----- {len([x for x in self.workers if x.__class__.__name__ == 'Vet'])} Vets:\n"
        for vet in [x for x in self.workers if x.__class__.__name__ == 'Vet']:
            result += f"{vet.__repr__()}"

        return result


""""Test Code"""
# zoo = Zoo("Zootopia", 3000, 5, 8)
#
# # Animals creation
# animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]
#
# # Animal prices
# prices = [200, 190, 204, 156, 211, 140]
#
# # Workers creation
# workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]
#
# # Adding all animals
# for i in range(len(animals)):
#     animal = animals[i]
#     price = prices[i]
#     print(zoo.add_animal(animal, price))
#
# # Adding all workers
# for worker in workers:
#     print(zoo.hire_worker(worker))
#
# # Tending animals
# print(zoo.tend_animals())
#
# # Paying keepers
# print(zoo.pay_workers())
#
# # Fireing worker
# print(zoo.fire_worker("Adam"))
#
# # Printing statuses
# print(zoo.animals_status())
#

# test zoo hire_worker success
#
# test zoo workers_status



