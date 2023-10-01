"""Class for Car model."""

from clase_python.core.abcs.vehicle_abcs import VehicleABC

MAX_DISTANCE_CAN_TRAVEL = 5 #constante global

AVAILABLE_CAR_BRANDS = ['Nissan', 'Toyota', 'bmw']
# clase carro
class Car(VehicleABC):
    #se llama la interfaz VehicleABC
    #self se utiliza dentro de las funciones

    def __init__(self, brand: str, model: int, door_quantity: int) -> None:
        """cosntructor for Car class."""

        self.__brand = brand #la marca _brand _significa que es privado
        self.__model = model #modelo del carro
        self.__door_quantity = door_quantity #cantidad de puertas
        self.__distance_traveled = 0
        self._velocidad = 0

    #función de moverse
    def move(self, additional_distance) -> None: #none que no retorna nada

        if additional_distance <= MAX_DISTANCE_CAN_TRAVEL: #costante
            self.__distance_traveled += additional_distance
        else:
            self.__distance_traveled += MAX_DISTANCE_CAN_TRAVEL

    def fast(self, acelaracion ) -> None:
        if fast(aceleracion== True) :
            self._velocidad += 10
        else:
            self._velocidad = 0

    @property
    # el decorador property permite gestionar todo lo refente al atributo brand
    def brand(self):
    #definimos el atributo
        return self.__brand
        
    @brand.setter
    def brand(self, brand):
        if brand in AVAILABLE_CAR_BRANDS:
            self.__brand = brand
        else:
            print("ingrese una marca valida.")

    @property
    def distance_traveled (self):
        return self.__distance_traveled
        
    @distance_traveled.setter
    def distance_traveled(self,distance_traveled):
        self.__distance_traveled = distance_traveled