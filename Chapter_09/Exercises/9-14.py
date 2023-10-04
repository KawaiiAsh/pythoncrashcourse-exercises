# 请创建一个Die 类，它包含一个名为sides 的属性，该属性的默认值为6。
# 编写一个名为roll_die() 的方法，它打印位于1和骰子面数之间的随机数
# 创建一个6面的骰子，再掷10次。 创建一个10面的骰子和一个20面的骰子，并将它们都掷10次。
from random import randint

class Die():
    def __init__(self,sides = 6):
        self.sides = sides
    
    def roll_die(self):
        return randint(1,self.sides)

six_side_die = Die()
for _ in range(10):
    print(six_side_die.roll_die())

ten_side_die = Die(10)
for _ in range(10):
    print(ten_side_die.roll_die())

twenty_side_die = Die(20)
for _ in range(10):
    print(twenty_side_die.roll_die())