from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def click(self):
        pass


class Checkbox(ABC):
    @abstractmethod
    def check(self):
        pass


class WinButton(Button):
    def click(self):
        print("click on windows button")


class MacButton(Button):
    def click(self):
        print("Click on mac button")


class WinCheckbox(Checkbox):
    def check(self):
        print("checking windows checkbox")


class MacCheckbox(Checkbox):
    def check(self):
        print("checking mac checkbox")


class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass


class WinFactory(GUIFactory):
    def create_button(self):
        return WinButton()

    def create_checkbox(self):
        return WinCheckbox()


class MacFactory(GUIFactory):

    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()


def get_factory_based_on_os(operating_system: str):
    _os_factory_mapper = {"win": WinFactory, "mac": MacFactory}
    if _os_factory_mapper.get(operating_system.lower()) is None:
        raise ValueError("OS is not supported")
    return _os_factory_mapper[operating_system.lower()]()


def client_code(gui_factory: GUIFactory):
    button = gui_factory.create_button()
    checkbox = gui_factory.create_checkbox()
    button.click()
    checkbox.check()


if __name__ == "__main__":
    chosen_os = "Mac"
    factory = get_factory_based_on_os(chosen_os)
    client_code(factory)
