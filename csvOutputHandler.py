import csv
from dateutil import tz
from datetime import datetime, timezone

class CsvOutputHandler:
    def __init__(outputHandler, file):
        outputHandler.file = file
        outputHandler.allowedResponses = ['200', '201']

    def reader(outputHandler):
        with open(outputHandler.file, newline='') as csvfile:
            contents = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in contents:
                print(', '.join(row))

    def readAsDict(outputHandler):
        with open(outputHandler.file, newline='') as csvfile:
            contents = csv.DictReader(csvfile)
            for row in contents:
                if row['responseCode'] not in outputHandler.allowedResponses:
                    outputHandler.__output(row)

    def __output(outputhandler, row):
        date = outputhandler.__configureDate(row['timeStamp'])
        out = str.format("{0}, {1}, {2}, {3}, {4}", row['label'], row['responseCode'], row['responseMessage'], row['failureMessage'], date)
        print(out)

    def __configureDate(outputHandler, epochDate):
        #pstTime = datetime.tzname(-timedelta(hours=8), name="PST")
        pst = tz.gettz('America/Los_Angeles')
        date_format='%m/%d/%Y %H:%M:%S %Z'
        epochTimeSeconds = int(epochDate)/1000
        utcTime = datetime.fromtimestamp(epochTimeSeconds, timezone.utc)
        pstTime = utcTime.astimezone(pst)
        pstTime = pstTime.strftime(date_format)
        return pstTime

#use for testing
print("Please provide path to Jmeter Results file:")
inputFile = input()
c = CsvOutputHandler(inputFile)
c.readAsDict()