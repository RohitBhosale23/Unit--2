class vehicle:
    def move(self):
        pass

class car(vehicle):
    def move(self):
        print("The car is driving on the road.")

class bicycle(vehicle):
    def move(self):
        print("The bicycle is being pedaled.")

#Create a object of the subclasses
car_obj = car()
bicycle_obj = bicycle()

# Call the move method for each object
car_obj.move()
bicycle_obj.move()
