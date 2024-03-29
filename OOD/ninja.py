# define class, the blue print of Ninja

class Ninja:
    def __init__(self, name, village, chakara_level):
        self.name = name
        self.village = village
        self.chakara_level = chakara_level

    def introduce(self):
        print(f"{self.name} is from {self.village}, has {self.chakara_level} chakara level")


naruto = Ninja("Naruto", "Hidden Leaf", 1000)

naruto.introduce()

# OOP is founded on four major principles:
# 1. Encapsulation 封装 （像每个忍者都有秘密技巧，数据和操作数据的方法捆绑在一起）
# 2. Abstraction 抽象（一个忍者可以执行忍术，但不需要知道他们如何执行就能理解他们可以，隐藏复杂的实现，只暴露必要的部分）
# 3. Inheritance 继承 （就像忍者从他们的家族或老师继承忍术一样，类可以从其他类继承属性和方法)
# 4. Polymorphism 多态 （一个忍术（方法）可以根据执行忍者（对象）的不同， 而有不同的执行效果）

# 1.封装例子
print("\n### 封装例子\n")

class Book:
    def __init__(self, title, author, isbn, is_borrowed=False):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowd = is_borrowed

    def borrow_book(self):
        if self.is_borrowd:
            print('This book is not available')
        else:
            self.is_borrowd = True
            print('Success!')

# 创建一本书的实例
my_book = Book("火影忍者", "岸本斉史", "123-456-789")

# 尝试借阅这本书
my_book.borrow_book()

# 再次尝试借阅，以验证状态已改变
my_book.borrow_book()
        
# 2. 抽象的例子
print("\n### 抽象的例子\n")

class Vehicle:
    def accelerate(self):
        raise NotImplementedError("子类必须实现这个方法")
    
    def decelerate(self):
        raise NotImplementedError("子类必须实现这个方法")
    
class Car(Vehicle):
    def accelerate(self):
        print("汽车加速中...")

    def decelerate(self):
        print("汽车减速中...")

class Motorcycle(Vehicle):
    def accelerate(self):
        print("摩托车加速中...")

    def decelerate(self):
        print("摩托车减速中...")

myCar = Car()
myCar.accelerate()
myCar.decelerate()

myMotorcycle = Motorcycle()
myMotorcycle.accelerate()
myMotorcycle.decelerate()

# 3. 继承的例子
print("\n### 继承的例子\n")

class Ninja:
    def __init__(self, name, village):
        self.name = name
        self.village = village

    def perform_duty(self):
        print(f"{self.name} from {self.village} is performing their duty.")

class MedicalNinja(Ninja):
    def perform_duty(self):
        super().perform_duty()
        self.heal()

    def heal(self):
        print(f"{self.name} is healing their teammates.")

class CombatNinja(Ninja):
    def perform_duty(self):
        super().perform_duty()
        self.fight()

    def fight(self):
        print(f"{self.name} is fighting the enemy")

class ScoutNinja(Ninja):
    def perform_duty(self):
        super().perform_duty()
        self.scout()

    def scout(self):
        print(f"{self.name} is scouting the area")

# 创建忍者实例
sakura = MedicalNinja("Sakura", "Leaf")
naruto = CombatNinja("Naruto", "Leaf")
kakashi = ScoutNinja("Kakashi", "Leaf")

# 调用方法
sakura.perform_duty()
naruto.perform_duty()
kakashi.perform_duty()

# 4. 多态的例子
print("\n### 多态的例子\n")

class Ninja:
    def perform_task(self):
        print("Perform a generic task")

class MedicalNinja(Ninja):
    def perform_task(self):
        print("Healing teammates")

class CombatNinja(Ninja):
    def perform_task(self):
        print("Fight enemies")

class ScoutNinja(Ninja):
    def perform_task(self):
        print("Scouting the area")

def assign_task(ninja):
    ninja.perform_task()

# 创建不同类型的忍者对象
sakura = MedicalNinja()
naruto = CombatNinja()
kakashi = ScoutNinja()

# 分配任务
assign_task(sakura)  # 输出: Healing teammates.
assign_task(naruto)  # 输出: Fighting enemies.
assign_task(kakashi)  # 输出: Scouting the area.
