# class Dog():
#     def __init__(self, name):
#         self.name = name

#     def setAge(self, age):
#         self.age = age


# tim = Dog("lasi")
# print(tim.name)
# tim.name = "tim"
# print(tim.name)
# tim.setAge(5)
# print(tim.age)


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def setColor(self, color):
        self.color = color
        print(self.color)

    def print_name(self):
        print(self.name)

# %%
# p1 = Point(1, 2)
# p2 = Point(3, 4)
# p3 = Point(5, 6)

# p1 = p2
# p1 = p3
# print(p2.x)

# lst1 = [1,2,3,4,5]
# lst2 = [6,7,8,9]
# lst3 = [1,1,1,1,1]

# lst1 = lst2
# lst1 = lst3
# print(lst2)
# %%


class BankAccount:
    defaultAccNumber = 1  # Class attribute

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance  # Public attribute
        self.accountNumber = BankAccount.defaultAccNumber
        BankAccount.defaultAccNumber += 1

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
        else:
            self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough balance!")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount

    def get_balance(self):
        return self.balance

    def set_name(self, name):
        self.name = name


acc1 = BankAccount("batel", 500)
acc1.set_name("noam")
print(acc1.name)
print(acc1.balance)


# %%
