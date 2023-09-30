"""configuration test file."""

import pytest

from clase_python.model.car import Car

#prueba unitaria para el metodo move de la clase car
@pytest.fixture() #metodo decorador de la libreria pytest le da unas propiedades a car
def car():
    return Car ('BMW', 2004, 4)
#le entrego este objeto a la prueba inyecion de depedencias