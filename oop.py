class Phone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.is_on = False

    def power_on(self):
        self.is_on = True
        print(f"{self.brand} {self.model} is now ON.")

    def power_off(self):
        self.is_on = False
        print(f"{self.brand} {self.model} is now OFF.")

    def get_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}GB"

# Inheritance: Smartphone with Camera
class SmartPhone(Phone):
    def __init__(self, brand, model, storage, camera_megapixels):
        super().__init__(brand, model, storage)
        self.camera_megapixels = camera_megapixels

    def take_photo(self):
        if self.is_on:
            print(f"Photo taken with {self.camera_megapixels}MP camera!")
        else:
            print("Turn on the phone to take a photo.")

    # Polymorphism: override get_info
    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Camera: {self.camera_megapixels}MP"

# Example usage
phone1 = Phone("Itel", "A22S", 16)
phone2 = SmartPhone("Apple", "iPhone 14 Pro", 256, 48)

phone1.power_on()
print(phone1.get_info())
phone1.power_off()
phone2.power_on()
print(phone2.get_info())
phone2.take_photo()

# Polymorphism Example: Vehicles with different move() implementations

class Transport:
    def move(self):
        print("The vehicle is moving.")

class Car(Transport):
    def move(self):
        print("Driving 🚗")

class Plane(Transport):
    def move(self):
        print("Flying ✈️")

class Boat(Transport):
    def move(self):
        print("Sailing 🚤")

# Example usage
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    vehicle.move()

