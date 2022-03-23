#Read and Write Files

filename = "languages.txt"
fileHandler = open(filename, "w")

fileHandler.write("Bash\n")
fileHandler.write("Python\n")
fileHandler.write("PHP\n")

fileHandler.close()

fileHandler = open(filename, "r")

for line in fileHandler:
    print(line)

fileHandler.close()