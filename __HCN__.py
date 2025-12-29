from .__BUILDER__ import Builder

class HCN:
    def __init__(self):
        self.builder = Builder()

    @staticmethod
    def start():
        return HCN()

    def show(self, path):
        return self.builder.build(path)
