from car import car


def main():
    brand = input("Enter brand of vehicle: ")
    model = input("Enter Model: ")
    year = int(input("Enter release year: "))
    fuel_type = input("Enter fuel tipe (gasoline, gas, diesel): ")
    max_speed = float(input("Enter max speed (km/h): "))
    engine_capacity = float(input("Enter engine capacity (L): "))
    rotation_speed = int(input("Enter max count of rotations per min: "))
    pe = float(input("Enter utillity ratio : "))
    
    my_car = car(brand, model, year, fuel_type, max_speed, engine_capacity, rotation_speed, pe)


    print("=== Vehicle informa ===")
    my_car.info()

    
    print("\n=== Mathing engine power ===")
    power = my_car.engine_power_calc()
    print(f"Engie power: {power} л.с.")

if __name__ == "__main__":
    main()