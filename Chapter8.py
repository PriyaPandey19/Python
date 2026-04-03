file = open("mast.txt", "r")
dataOfFile = file.read()

dataOfFile = dataOfFile.lower()

if "live" in dataOfFile:
    print("Yes live word is present in the file")
else:
    print("No")    

#file opening in write mode

file = open("report.txt", "w")
file.write("Learning python Having lot of fun....")