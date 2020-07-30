class Transport():
    topSpeed="None"
    color="None"

    def assignColor(self,color):
        self.color=color

class Car(Transport):
    def __init__(self):
        print("NEW OBJ")
        self.topSpeed="300 KmH"

    def assignColor(self,color):
        self.color=color

    def startEngine(self):
        print(f"{self.color} Color Car started with speed{self.topSpeed}")

class Bike(Transport):
    def __init__(self):
        print("NEW OBJ") 
        self.topSpeed="100 KmH"
   
    def assignColor(self,color):
        self.color=color
      
    def startEngine(self):
        print(f"{self.color} Color Bike started with speed{self.topSpeed}")

class TransFactory():
    instances={}
    def createTransport(self,type):
        trasport=Transport()
        if(self.instances.__contains__(type)):
            trasport= self.instances[type]
        else:
            if(type=="car"):
                trasport=Car()
            elif(type=="bike"):
                trasport=Bike()
            self.instances[type]=trasport
        return trasport

tf=TransFactory()
car1=tf.createTransport("car")
car1.assignColor("Blue")
car1.startEngine()
car1.assignColor("Red")
car1.startEngine()
car2=tf.createTransport("car")
car2.assignColor("Yellow")
car2.startEngine()

vc=tf.createTransport("bike")
vc.assignColor("Yellow")
vc.startEngine()


for x in range(0,10):
    print(x)
