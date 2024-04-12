
'''
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
'''



from datetime import datetime


def Friday_13(year: int, month: int) -> bool:
    now = datetime(year, month, 13)
    print(now.weekday())

    
    


if __name__ == "__main__":
    Friday_13(1990, 9)


