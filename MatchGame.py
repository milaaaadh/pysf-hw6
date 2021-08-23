import numpy as np
from tkinter import *


class MatchGame :
    """
    A simple game to challenge your memory
    I used the tips of a website to better design a work
    See at : https://b2n.ir/q92597
    """

    def creat_primary_table ( x , y ) :
        """
        creat a primary table for show True guesses
        set size by x,y value
        @type x,y: int, int
        @rtype: return a numpy array
        """

        primary_array = np.full ( (x , y) , '*' )

        return primary_array

    def show_table ( array ) :
        """
        Show a table based on guessed or un guessed elements
        Give an array
        @type array: numpy array
        @rtype: only show a schematic of conjectures and nothing for return
        """

        x , y = array.shape
        print ( end='    ' )
        for i in range ( y ) :
            print ( '' , i + 1 , end=' ' )
        print ( '' )
        print ( '   ' , '_' * (y * 3) )
        for j in range ( x ) :
            print ( '' , j + 1 , end=' |' )
            for i in range ( y ) :
                print ( '' , array [ j ] [ i ] , end=' ' )
            print ( )

        return ('')

    def creat_random_table ( min_value , max_value , x , y ) :
        """
        Give min, max value and row and column
        You should give a x,y that x*y//2 because repetition of each number must be even
        Creat a random table for guesse
        @type min_value,max_value,x,y: int, int, int, int
        @rtype: numpy random
        """

        first_table = np.random.randint ( min_value , max_value , size=x * y // 2 )
        first_table = np.repeat ( first_table , 2 )
        np.random.shuffle ( first_table )
        random_table = first_table.reshape ( x , y )

        return random_table

    def bad_guess ( a , b , aa , bb ) :

        print ( f'Not an identical pair. Found {a} at {aa} and {b} at {bb}' )

    def correct_guess () :

        print ( f'good guess' )

    def get_location ( round , r , c ) :
        x , y = input ( f'Enter coordinates for {round} card:' ).split ( )
        x , y = int ( x ) , int ( y )
        while x > r or y > c or x < 1 or y < 1 :
            print ( f'your location out of range (table size is {r}*{c})' )
            x , y = input ( f'Enter coordinates for {round} card:' ).split ( )
            x , y = int ( x ) , int ( y )
        return int ( x ) - 1 , int ( y ) - 1


