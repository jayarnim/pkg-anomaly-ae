DATALOADER_REGISTRY = {}

def register(name):
    def wrapper(cls):
        DATALOADER_REGISTRY[name] = cls
        return cls
    return wrapper