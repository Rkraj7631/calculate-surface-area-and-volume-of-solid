import math

class Solid:
    def __init__(self):
        self.shape=None

    def get_data(self):
        self.shape=input("Enter cube / cuboid / cylinder / sphere / cone :").lower()

        if self.shape=="cube":
            self.side=float(input("enter side of cube : "))

        elif self.shape=="cuboid":
            self.length=float(input("enter lenth of cubodid : "))
            self.breadth=float(input("enter breadth of cuboid : "))
            self.height=float(input("enter height of cuboid : "))

        elif self.shape=="cylinder":
            self.radius=float(input("Enter radius of cylinder : "))
            self.height=float(input("Enter height of cylinder : "))

        elif self.shape=="sphere":
            self.radius=float(input("Enter radius of sphere : "))

        elif self.shape=="cone":
            self.radius=float(input("enter radus of cone : "))
            self.height=float(input("enter height of cone : "))

        else:
            print("invalid shape")

    def surface_area(self):
        if self.shape=="cube":
            return 6*(self.side**2)

        elif self.shape=="cuboid":
            return 2*(self.length*self.breadth + self.breadth*self.height + self.height*self.length)

        elif self.shape=="cylinder":
            return 2*3.14*self.radius*(self.radius+self.height)

        elif self.shape=="sphere":
            return 4*3.14*(self.radius**2)

        elif self.shape=="cone":
            l=math.sqrt((self.radius**2)+(self.height**2))
            return 3.14*self.radius*(self.radius+l)

    def volume(self):
        if self.shape=="cube":
            return self.side**3

        elif self.shape=="cuboid":
            return self.length*self.breadth*self.height
        
        elif self.shape=="cylinder":
            return 3.14*(self.radius**2)*self.height

        elif self.shape=="sphere":
            return (4/3)*3.14*(self.radius**2)

        elif self.shape=="cone":
            return (1/3)*3.14*(self.radius**2)*self.height

    def display(self):
        print(f"surface area : {self.surface_area():.2f}")
        print(f"volume :  {self.volume():.2f}")


s=Solid()
s.get_data()
s.display()

           

        
