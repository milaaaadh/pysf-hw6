import numpy as np


class MatchGame :

    def __init__ ( self , min , max , row , column , random_table=[ [ ] ] ) :
        self.min = min
        self.max = max
        self.row = row
        self.column = column
        self.primary_table = np.full ( (row , column) , '*' )
        self.random_table = random_table

    def creat_random_table ( self ) :
        first_table = np.random.randint ( self.min , self.max+1 , size=self.row * self.column // 2 )
        first_table = np.repeat ( first_table , 2 )
        np.random.shuffle ( first_table )
        random_table = first_table.reshape ( self.row , self.column )
        self.random_table = random_table

        # when use class then use a.creat_random_table() for creat random table

    def show_table ( self ) :
        """
        Show a table based on guessed or un guessed elements
        Give an array
        @type array: numpy array
        @rtype: only show a schematic of conjectures and nothing for return
        """

        print ( end='    ' )
        for i in range ( self.column ) :
            print ( '' , i + 1 , end=' ' )
        print ( '' )
        print ( '   ' , '_' * (self.column * 3) )
        for j in range ( self.row) :
            print ( '' , j+1  , end=' |' )
            for i in range (self.column ) :
                print ( '' , self.primary_table [ j ] [ i ] , end=' ' )
            print ( )

        return ('')
        # you can show table when use a.show_table()

    def bad_guess (self, a , b , aa , bb ) :

        print ( f'Not an identical pair. Found {a} at {aa} and {b} at {bb}' )

    def correct_guess (self) :

        print ( f'good guess' )

    def get_location ( self, round) :
        x , y = input ( f'Enter coordinates for {round} card:' ).split ( )
        x , y = int ( x )-1 , int ( y )-1


        while x > self.row or y > self.column or x < 0 or y < 0 :
            print ( f'your location out of range (table size is {self.row}*{self.column})' )
            x , y = input ( f'Enter coordinates for {round} card:' ).split ( )
            x , y = int ( x )-1 , int ( y )-1

        return x , y




