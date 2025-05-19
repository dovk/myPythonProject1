print("hello" " engineers")
# create a new file called hello.py and write the above code in it
print("hello" " engineers")

print("hello" " engineers1")
print("hello" " engineers2")
print("hello" " engineers3")


print("batel", "mirel")
name = "batel"
dir(name)

lst1 = [1, 2, 3]
lst1.insert(3, 4)
print(lst1)
num = lst1.pop(1)
print(num)
print(lst1)


x = [10, 1]
y = [10, 1]

if x is y:
    print("x is y")
else:
    print("x is not y")
# %%
# exercise 1
# Create a list of tuples with name and age: (”Amit", 25)
persons = [("batel", 39), ("avi", 45), ("lines", 9), ("sahar", 6), ("ann", 5)]
# Slice the list to keep only first 3 people
persons = persons[:3]
#
names = persons[0:3]
print(names)
ages = persons[0][1], persons[1][1], persons[2][1]
ages2 = [item[1] for item in persons]
print(ages2)

is_adult = []
if ages[0] >= 18:
    is_adult.append(True)
else:
    is_adult.append(False)

is_adult.append(ages[1] >= 18)
is_adult.append(ages[2] >= 18)

print(is_adult)
persons.pop(1)
print(persons)
persons.append(("maya", 39))

# lesson 2
# %%
x = 2
if x != None:
    print("x is not None")

x = 0
if x != None:
    print("x is not None")


# %%
