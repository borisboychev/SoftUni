from csv import reader
from io import StringIO
from json import loads

class JsonConverter:
    def convert(self, data):
        return loads(data)

class CsvConverter:
    def convert(self, data):
        csv = reader(StrubgIO(data))
        lines = [line for line in csv]
        return lines

def convert(type, data):
    converters = {'json': JsonConverter(),
                  'csv': CsvConverter(),
                  }
    return converters[type].convert(data)

