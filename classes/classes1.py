from typing import Literal
"""
Begin Shape class
"""

class shape:
    def __init__(self,shape_sides:int,shape_name:str):
        self.side=shape_sides
        self.name=shape_name
    
    def info(self):
        print("\nName:", self.name, "\nSides:", self.side)

"""
End Shape Class
"""

#Shapes:

circle= shape(0,"Circle")
triangle= shape(3, "Triangle")
square= shape(4,"Square")
pentagon= shape(5, "Pentagon")

#Info:

circle.info()
triangle.info()
square.info()
pentagon.info()

######################################################################################################################################################################
"""

"""
class dog:
    def __init__(self, name:str, breed: Literal["Bulldog", "Goldador", "Harrier"], fur: Literal["red", "green", "blue"], eye_color: Literal["red", "green", "blue"]):
        self.name = name
        self.breed = breed
        self.fur = fur
        self.color = eye_color
    
    def info(self):
        print("\nName:",self.name,"\nBreed:",self.breed,"\nFur color:",self.fur,"\nEye Color:",self.color)

dog1= dog("Goldy", 'Bulldog', "blue", "blue")
dog2= dog("Brownie", 'Goldador', 'red', 'red')
dog3= dog("Stoutty",'Harrier', "green", "green")

#Info:

dog1.info()
dog2.info()
dog3.info()
