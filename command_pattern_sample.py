from abc import ABC,abstractmethod
class _Command(ABC):
    @abstractmethod
    def execute(self):
        pass
class LightonCommand(_Command):
    def __init__(self,lightobject) -> None:
        self.light=lightobject
    def execute(self):
        self.light.turn_on()

class Light:
    def turn_on(self):
        print("You have done this")
    def turn_off(self):
        print("You have turned off the light")
class RemoteControl:
    def __init__(self) -> None:
        self.command=None
    def setCommand(self,command):
        self.command=command
    def pressButton(self):
        self.command.execute()

if __name__=="__main__":
    light=Light()
    remote=RemoteControl()
    light_on=LightonCommand(light)

    remote.setCommand(light_on)
    remote.pressButton()
