# Dinamic Typing
class pycharm:
    def execute(self):
        print("Compiling")
        print("Running")

class visualstudio:
    def execute(self):
        print("Compiling")
        print("Running")
        print("Spell checking")

class laptop:
    def code(self,ide):
        ide.execute()   

ide=pycharm()
lap1=laptop()
lap1.code(ide)