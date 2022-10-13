from enum import Enum

class season(Enum):
    summer = 1
    winter = 2
    rainy =3

print(season.rainy)
print(season(1))
print(season["winter"])
print([c for c in season])