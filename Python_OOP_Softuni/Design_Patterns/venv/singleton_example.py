def singleton(cls):
    instances = [None]
    def wrapper(*args, **kwargs):
        if instances[0] is None:
            instances[0] = cls(*args,**kwargs)
        return instances[0]
    return wrapper

@singleton
class DataImporter:
    def __init__(self):
        pass

importer1 = DataImporter()
importer2 = DataImporter()

print(importer1)
print(importer2)
print(importer1 == importer2)