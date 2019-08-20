import os, fileinput
cwd = os.getcwd()
print("your current working directory is "+cwd)
print("Doee wsadminlib.py exist :")
print(os.path.exists('wsadminlib.py'))
print("so the path for wsadminlib.py is "+os.path.abspath('wsadminlib.py'))
print("content of current working directory: ")
#print(os.listdir(cwd))
#print(os.environ)
count=0
for (x, y, z) in os.walk('.'):
    for name in x:
        print(name)
#for line in fileinput.input():
 ##   print(fileinput.lineno)
#os.mkdir(os.getcwd()+"\\TestOsMkDir");
