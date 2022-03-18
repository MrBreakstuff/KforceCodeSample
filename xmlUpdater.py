from datetime import date, timedelta
from xml.etree import ElementTree

class XmlUpdater:
    def __init__(updater, xmlFile, outputFile):
        updater.xmlFile = xmlFile
        updater.outputFile = outputFile
        updater.tree = ElementTree.parse(updater.xmlFile)
        updater.root = updater.tree.getroot()


    def __updateDepart(updater, x):
        for departDate in updater.root.iter('DEPART'):
            new_departDate = date.today()+timedelta(days=x)
            departDate.text = new_departDate.strftime("%Y%m%d")

    def __updateReturn(updater, y):
        for returnDate in updater.root.iter('RETURN'):
            new_returnDate = date.today()+timedelta(days=y)
            returnDate.text = new_returnDate.strftime("%Y%m%d")

    def updateXml(updater, x, y):
        updater.__updateDepart(x)
        updater.__updateReturn(y)
        updater.tree.write("./Output/" + updater.outputFile + ".xml")


#use for testing
print("Please provide path to file:")
inputFile = input()
print("Please specify name for output file:")
outputFile = input()
print("How many days from now until departure?")
departure = int(input())
print("How many days from now until return?")
_return = int(input())
x = XmlUpdater(inputFile, outputFile)
x.updateXml(departure, _return)