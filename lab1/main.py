import math

import numpy as np


def cylinder_area(r: float, h: float):
    """Obliczenie pola powierzchni walca. 
    Szczegółowy opis w zadaniu 1.
    
    Parameters:
    r (float): promień podstawy walca 
    h (float): wysokosć walca
    
    Returns:
    float: pole powierzchni walca 
    """
    if r>0 and h>0:
        pole = math.pi*r*r*h
        return pole
    else:
        return np.nan

def fib(n:int):
    """Obliczenie pierwszych n wyrazów ciągu Fibonnaciego. 
    Szczegółowy opis w zadaniu 3.
    
    Parameters:
    n (int): liczba określająca ilość wyrazów ciągu do obliczenia 
    
    Returns:
    np.ndarray: wektor n pierwszych wyrazów ciągu Fibonnaciego.
    """
    wektor = np.array(1)
    if isinstance(n, int) and n >= 1:
        for i in range(0, n - 1):
            if i == 0:
                wektor = np.append(wektor, [1])
            else:
                wektor = np.append(wektor, [wektor[i - 1] + wektor[i]])
        return [wektor]
    else:
        return None

def matrix_calculations(a:float):
    """Funkcja zwraca wartości obliczeń na macierzy stworzonej 
    na podstawie parametru a.  
    Szczegółowy opis w zadaniu 4.
    
    Parameters:
    a (float): wartość liczbowa 
    
    Returns:
    touple: krotka zawierająca wyniki obliczeń 
    (Minv, Mt, Mdet) - opis parametrów w zadaniu 4.
    """
    matrix = np.array([[a,1,-a], [0,1,1], [-a,a,1]])
    Mdet = np.linalg.det(matrix)
    Mt = matrix.T
    if Mdet != 0:
        Minv = np.linalg.inv(matrix)
    else:
        Minv = np.nan
    return Minv, Mt, Mdet



def custom_matrix(m:int, n:int):
    """Funkcja zwraca macierz o wymiarze mxn zgodnie 
    z opisem zadania 7.  
    
    Parameters:
    m (int): ilość wierszy macierzy
    n (int): ilość kolumn macierzy  
    
    Returns:
    np.ndarray: macierz zgodna z opisem z zadania 7.
    """
    return None