from dataclasses import dataclass


@dataclass
class Participant:
    name: str
    tasks: int
    fine: int

    @classmethod
    def __verification(Participant, other):
        if not isinstance(other, Participant):
            raise TypeError('Сравнение возможно с объектом класса Participant')
        return other

    def __lt__(self, other):
        Participant.__verification(other)
        return (self.tasks > other.tasks if self.tasks != other.tasks else
                self.fine < other.fine if self.fine != other.fine else
                self.name < other.name)


a = ('alla', 4, 100)
b = ('timofey', 4, 80)

alla = Participant(*a)
gena = Participant(*b)
print(alla, gena)
print(alla < gena)
