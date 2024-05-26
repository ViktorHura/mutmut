from abc import ABC, abstractmethod

class Mutation(ABC):
    @abstractmethod
    def mutate(self, *args, **kwargs):
        raise NotImplemented

    @abstractmethod
    def get_mutate_pointer(self):
        """
        Returns pointer to self.mutate in a dict, with key as either "children" or "value"
        """
        raise NotImplemented