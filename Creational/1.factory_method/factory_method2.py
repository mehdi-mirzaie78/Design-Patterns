"""
Editor file
file can be of type pdf, xml, json
"""

from abc import ABC, abstractmethod


class Creator(ABC):

    @abstractmethod
    def create_editor(self):
        pass

    def call_edit(self):
        editor = self.create_editor()
        return editor.edit()


class JsonCreator(Creator):
    def create_editor(self):
        return Json()


class PdfCreator(Creator):
    def create_editor(self):
        return Pdf()


class Product(ABC):

    @abstractmethod
    def edit(self):
        pass


class Json(Product):
    def edit(self):
        return "Editing Json file"


class Pdf(Product):
    def edit(self):
        return "Editing Pdf file"


def client_code(creator: Creator):
    print(creator.call_edit())      


if __name__ == "__main__":
    client_code(PdfCreator())
