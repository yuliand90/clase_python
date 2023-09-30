from model.car import Car


def main():
  

    carro1: Car = Car("Nissan",2020,4)

    carro1.move(4)

    print(carro1.distance_traveled)

if __name__ == "__main__":
    main()