print("Working with files")
f=open("VikasPython.txt","w+")
for i in range(10):
    f.write("Get this inserted to file %d\r\n"%(i+1))
f.close()
