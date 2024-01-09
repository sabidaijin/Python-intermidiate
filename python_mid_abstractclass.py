#!/usr/bin/env python3
from abc import ABC,abstractmethod

class agent(ABC):
    @abstractmethod
    def select(self):
        raise NotImplementedError("method is not implemented yet")