class Car:
    amount_cars = 0
    def __init__ ( self, manufacturer, model, hp):
        self.manufacturer = manufacturer
        self.model = model
        self.hp = hp
        Car.amount_cars += 1
        self.__secret = "12345"
    def print_car_amount( self ):
        print ( "Amount: {}".format(Car.amount_cars))
        
    def __del__(self):
        Car.amount_cars -= 1

car1 = Car("bmw", "x8", 200)
car2 = Car("bmw", "x7", 100)
car3 = Car("bmw", "x6", 90)

print(car1.__secret)

# car3.print_car_amount()
# del car1
# car3.print_car_amount()