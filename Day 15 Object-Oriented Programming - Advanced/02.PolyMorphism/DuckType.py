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
    def code(self,idle):
        idle.execute()   

idle=pycharm()
idle1=visualstudio()
lap1=laptop()
lap1.code(idle1)