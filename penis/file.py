import os

filename = "read_test.txt"
dirname = os.path.dirname(filename)
if not os.path.exists(dirname):
    os.makedirs(dirname)

f = open('read_test.txt', "r")
line = f.readline()
while line:
    print(line)
    line = f.readline()
f.close()