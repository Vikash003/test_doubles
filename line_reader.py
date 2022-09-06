import os

def readFromFile(fileName):
    if not os.path.exists(fileName):
        raise Exception("File not Found")
    file = open(fileName, "r")
    line = file.readline()
    return line