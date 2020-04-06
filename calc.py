#/usr/bin/python3

def add(x, y):
    """Sumo x + y"""
    return x + y

def substract(x, y):
    """Resto x - y"""
    return x - y

def multiply(x, y):
    """Multiplico x * y"""
    return x * y

def divide(x, y):
    """Divido x / y"""
    if y == 0:
        raise ValueError('No se puede dividir por cero!')
    return x / y