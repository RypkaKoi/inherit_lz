class Vehicle:
    def __init__(self, brand, model,  year):
        self.brand = brand
        self.model = model
        self.year = year

    def info(self):
            print(f"Brand: {self.brand}")
            print(f"Model: {self.model}")
            print(f"Release: {self.year}")


class car(Vehicle):
    def __init__(self, brand, model, year, fuel_type, max_speed, engine_capacity, rotation_speed, pe):
        super().__init__(brand, model, year)
        self.fuel_type = fuel_type
        self.max_speed = max_speed
        self.engine_capacity = engine_capacity
        self.rotation_speed = rotation_speed
        self.pe = pe

    def info(self):
        super().info()
        print(f"Fuel type: {self.fuel_type}")
        print(f"Max speed: {self.max_speed} км/ч")
        print(f"Engine capacity: {self.engine_capacity} л")
        print(f"Rotations: {self.rotation_speed} об/мин")
        print(f"Rario PE: {self.pe}")

    def engine_power_calc(self):
        power_hp = (self.engine_capacity * self.rotation_speed * self.pe) / 100
        return power_hp