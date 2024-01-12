from enum import Enum


class Ninja:
    def __init__(self):
        self._score = 0

    @property
    def ninja_score(self) -> int:
        return self._score

    @ninja_score.setter
    def ninja_score(self, new_score: int):
        print(type(new_score))
        if new_score < 0:
            raise Exception("Score cannot be negative")
        self._score = new_score

    @classmethod
    def create_instance(cls):
        return cls()


def sum(a: int, b: int) -> int:
    return a + b


def display(set1):
    print(f"Type = {type(set1)}, id = {id(set1)} , value = {set1}")


obj = Ninja()
print(obj.ninja_score)
obj.ninja_score = 10.9
print(obj.ninja_score)

display(obj)
obj2 = Ninja.create_instance()
display(obj2)

print(type(sum(1, 2)))


class MyEnum(Enum):
    STARTED = 0
    STOPPED = 1


[print(f"{en.name}->{en.value}") for en in MyEnum]
