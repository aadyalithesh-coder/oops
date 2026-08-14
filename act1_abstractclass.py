from abc import ABC, abstractmethod

class absclass(ABC):

    def print(self,x):
        print("passed value:",x)
    
    @abstractmethod
    def task(self):
        print("We are in absclass task")

class test_class(absclass):
    def task(self):
        print("We are in test_class task")

test_obj= test_class()
test_obj.task()
test_obj.print(100)