class car:
    def start_engine(self):
        pass
    def drive(self):
        pass
class BMW(car):
    def start_engine(self):
        print("BMW engine started with a roar!")
    def drive(self):
        print("BMW is driving smoothly on the highwawy")
def test_drive(car):
    car.start_engine()
    car.drive()
bmw_car = BMW()
test_drive(bmw_car)
print()