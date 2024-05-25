from abc import ABC, abstractmethod

class Mutation(ABC):
    @abstractmethod
    def mutate(self, *args, **kwargs):
        pass