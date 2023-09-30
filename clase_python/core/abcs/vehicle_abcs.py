"""ABCs for Car Class."""

from abc import ABCMeta
from abc import abstractmethod #libreria decorador


class VehicleABC(metaclass=ABCMeta):
    #hace que esta clase no se pueda instanciar

    @abstractmethod 
    #que no se pueda usar e instanciar
    def move (self, distance_traveled: int) -> None: 
    #este decorador cada vez que definaos un metodo hace que todos los vehiculos que utilizan esta interfaz implementen este metodo.
        pass