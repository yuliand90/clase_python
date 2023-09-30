"""Class for Airplane model."""

MAX_DISTANCE_CAN_TRAVEL = 5
# clase avion
class Airplane:

    def __init__(self, brand: str, engines_quanity: int, door_quantity: int) ->None:
        """cosntructor for Airplane class."""

        self.brand = brand #la marca
        self.engines_quanity = engines_quanity #modelo del carro
        self.door_quantity = door_quantity #cantidad de puertas
        self.distance_traveled = 0
    #función de moverse
    def move(self, additional_distance) -> None: #none que no retorna nada

        if additional_distance <= MAX_DISTANCE_CAN_TRAVEL: #costante
            self.distance_traveled += additional_distance
        else:
            self.distance_traveled += MAX_DISTANCE_CAN_TRAVEL

