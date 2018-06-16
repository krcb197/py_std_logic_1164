"""
Module of functions for performing arithmetic operations
"""
from .std_logic import std_logic

def FullAdderCell(A,B,Cin=std_logic('0')):
    """
    implements a 1 bit adding cell with both carry in and carry out. Check out the wikipedia page on digital adders to
    understand the implementation: https://en.wikipedia.org/wiki/Adder_(electronics)

    :param A: std_logic
    :param B: std_logic
    :param Cin: std_logic
    :return: tuple or two std_logic containg the result and the carry bit
    """

    if not issubclass(A.__class__,std_logic):
        raise TypeError('Input A must be std_logic')

    if not issubclass(B.__class__,std_logic):
        raise TypeError('Input B must be std_logic')

    if not issubclass(Cin.__class__,std_logic):
        raise TypeError('Input Cin must be std_logic')

    temp1 = A ^ B
    S = temp1 ^ Cin

    Cout = (temp1 & Cin) | (A & B)


    return (S,Cout)