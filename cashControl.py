# cash control
from tokenize import Double


class Real():
    country = "Brasil"
    value = float
    types = str

rs00001 = Real()
rs00001.value = 0.01

rs00005 = Real()
rs00010 = Real()
rs00025 = Real()
rs00050 = Real()
rs00100 = Real()
rs00200 = Real()

print(rs00001.value)