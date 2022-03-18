import json
import re

class JsonEditor:
    def __init__(j, inputFile, outputfile):
        j.file = inputFile
        j.out = outputFile
        j.f = open(j.file, "r")
        j.parsed = json.load(j.f)
    

    def deleteElement(j, element):
        dictionary = j.__delete(j.parsed, element)
        j.__saveFile(dictionary)

    def __delete(j, dictionary, element):
        dictCopy = dictionary.copy()
        for key in dictCopy.keys():
            if key == element:
                del dictionary[key]
            if isinstance(dictCopy[key], dict):
                j.__delete(dictionary[key], element)
        return dictionary

    def __saveFile(j, dictionary):
        outFile = open("./Output/" + j.out, 'w')
        content = json.dumps(dictionary, indent=2)
        outFile.write(content)
        outFile.close()

#use for testing
print("Please provide path to file:")
inputFile = input()
print("Please specify name output file:")
outputFile = input()
print("Provide the key name for the element to remove:")
element = input()
j = JsonEditor(inputFile, outputFile)
j.deleteElement(element)