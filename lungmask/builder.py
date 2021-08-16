class Director:
    __builder = None

    def getModel(self, builder):
        self.__builder = builder


class Builder:
    def to(self, device):
        pass

    def load_state_dict(self, state_dict):
        pass

    def eval(self):
        pass


class ModelBuilder(Builder):
    def to(self, device):
        pass

    def load_state_dict(self, state_dict):
        pass

    def eval(self):
        pass

class Model:
    def __init__(self):
        pass
