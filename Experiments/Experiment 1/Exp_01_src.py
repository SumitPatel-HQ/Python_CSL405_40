# Experiment 01 ~ To implement the basic data types and control structures in python.

integer_var = 10
float_var = 20.5
string_var = "Hello"
boolean_var = True
list_var = [1, 2, 3]
tuple_var = (4, 5, 6)
dict_var = {"key": "value"}

print("Integer:", integer_var)
print("Float:", float_var)
print("String:", string_var)
print("Boolean:", boolean_var)
print("List:", list_var)
print("Tuple:", tuple_var)
print("Dictionary:", dict_var)

num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

print("For Loop Example:")
for i in range(5):
    print("Iteration", i)

print("While Loop Example:")
count = 0
while count < 3:
    print("Count:", count)
    count += 1

def add(a, b):
    return a + b

print("Function Example: 5 + 3 =", add(5, 3))
