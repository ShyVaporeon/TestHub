print("hello, world")
"""
for i in range(10):
    with open("test.txt", "a") as file:
        file.write("Thank you kind sir\n" * i)
    print(i)
"""

count = 0
string = ""

with open("test.txt", "r") as file:
    for i in file.readlines():
        string += i

# print(string)
def count_newlines(value):
    count = 0
    for i in value:
        if i == "\n":
            count += 1
    return count

print(count_newlines(string))