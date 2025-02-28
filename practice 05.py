
class car:
    year = 0
    mpg = 0
    speed = 0
    car_owners = []

    def __init__(self, year, mpg, speed):
        self.year = year
        self.mpg = mpg
        self.speed = speed
        

    def accelerate(self):
        self.speed += 30

    def brake(self):
        self.speed -= 60
    
    def __str__(self):
        return f"car_year_{self.year}_mpg_{self.mpg}_speed_{self.speed}"


def record_car_owners(owner1, owner2):

    obj_car1 = car(2016,20,80)
    obj_car2 = car(2013,25,60)

    obj_car1.car_owners = owner1
    obj_car2.car_owners = owner2

    return obj_car1,obj_car2