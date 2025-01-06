class Car:
    color='black'

    @staticmethod
    def start():
        print('start')

class Tata(Car):
    def __init__(self,model):
        self.model=model

t1 = Tata('tiago')
print(t1.model,t1.color)
t1.start()
      