from abc import ABC, abstractmethod


class DataSource(ABC):
    @abstractmethod
    def writeData(self, data):
        pass

    @abstractmethod
    def readData(self) -> str:
        pass

class FileDataSource(DataSource):
    def __init__ (self, filename):
        self.__file = filename

    def writeData(self, data):
        print(f'writing {data} to {self.__file}!')
        with open(self.__file, 'a') as file:
            file.write(data)
            file.write('\n')
        # write data to file.
        pass

    def readData(self) -> str:
        print(f'reading from {self.__file}')
        with open(self.__file, 'r') as file:
           return file.read()
        # read data from file.
        pass

class EncryptionDecorator(DataSource):
    def __init__(self, data_source: DataSource):
        self.data_source = data_source

    def __encrypt(self, data):
        return f'{"0x".join(str(ord(x)) for x in data)}'

    def __dectypt(self, data):
        return ''.join(chr(int(x)) for x in data.split('0x'))

    def writeData(self, data):
        data = self.__encrypt(data)
        return self.data_source.writeData(data)

    def readData(self) -> str:
        data = self.data_source.readData()
        return self.__dectypt(data)

fds = FileDataSource('file-test.txt')
# fds.readData()
# fds.writeData('test')

eds = EncryptionDecorator(fds)
eds.writeData('TestString')
print(eds.readData())