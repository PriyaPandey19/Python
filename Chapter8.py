file = open("mast.txt", "r")
dataOfFile = file.read()

dataOfFile = dataOfFile.lower()

if "live" in dataOfFile:
    print("Yes live word is present in the file")
else:
    print("No")    

