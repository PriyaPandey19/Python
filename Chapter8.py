file = open("mast.txt", "r")
dataOfFile = file.read()

dataOfFile = dataOfFile.lower()

if "live" in dataOfFile:
    print("Yes live word is present in the file")
else:
    print("No")    

#file opening in write mode

#file = open("report.txt", "w")
#file.write("Learning python Having lot of fun....")

#with keyword
with open("report.txt", "r") as f:
    data = f.read()
    print("file data:", data)

with open("newTextFile.txt","r") as f:
    line1 = f.readline()
    line2 = f.readline()
    line3 = f.readline()

    print("Line 1", line1)
    print("Line 2",line2)
    print("Line 3", line3)

