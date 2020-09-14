from abc import ABC, abstractmethod
from json import loads


class DataConverter(ABC):
    @abstractmethod
    def to_dict(self, data):
        pass


class JsonDataConverter(DataImporter):
    def to_dict(self, data):
        return loads(data)


class CsvDataConvertor(DataImporter):
    def to_dict(self, data):
        return None


class DataConverterAbstractFactory(ABC):
    @abstractmethod
    def get_converter(self):
        pass

    @abstractmethod
    def get_csv_converter(self):
        pass

    @abstractmethod
    def get_json_coverter(self):
        pass


class JsonDataConverterFactory(DataConverterFactory):
    def get_converter(self) -> DataConverter:
        return JsonDataConverter()


class ConcreteDataConverter(DataConverterFactory):
    def get_converter(self, type):
        if type == 'json':
            converter = JsonDataConverter()
            return converter
        elif type == 'csv':
            converter = CsvDataConverter()
            return converter

        raise ValueError


csv = """"
name, age,
Boris, 18
"""

json = '''
{
"name": "Boris",
"age": 18
}
'''

converter = JsonDataConverter()
print(converter.to_dict(json))
