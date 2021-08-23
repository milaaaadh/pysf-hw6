from MatchGame import *

# cfc : Coordinates first column
# cfr : Coordinates first row
# csc : Coordinates second column
# csr : Coordinates second row


x , y = input ( 'enter your table size by two number: ' ).split ( )
x , y = int ( x ) , int ( y )
while (x * y) % 2 != 0 :
    print ( 'Enter at least one of the numbers evenly' )
    x , y = input ( 'enter your table size by two number: ' ).split ( )
    x , y = int ( x ) , int ( y )

min_value , max_value = input ( 'enter your min, max value of table: ' ).split ( )
min_value , max_value = int ( min_value ) , int ( max_value )
if min_value > max_value :
    min_value , max_value = max_value , min_value
primary_table = MatchGame.creat_primary_table ( x , y )
random_table = MatchGame.creat_random_table ( min_value , max_value , x , y )

# while primary_table != random_table:
while primary_table.dtype != 'int64' :
    print ( MatchGame.show_table ( primary_table ) )

    cfr , cfc = MatchGame.get_location ( 'first' , x , y )

    csr , csc = MatchGame.get_location ( 'second' , x , y )

    if random_table [ cfr ] [ cfc ] == random_table [ csr ] [ csc ] :
        MatchGame.correct_guess ( )
        primary_table [ cfr ] [ cfc ] = random_table [ cfr ] [ cfc ]
        primary_table [ csr ] [ csc ] = random_table [ csr ] [ csc ]
    else :
        MatchGame.bad_guess ( random_table [ cfr ] [ cfc ] , random_table [ csr ] [ csc ] , (cfr + 1 , cfc + 1) ,
                              (csr + 1 , csc + 1) )
    try :
        primary_table = primary_table.astype ( int )
    except :
        print ( '' )

print ( MatchGame.show_table ( primary_table ) )
print ( 'Great job! The table is complete' )







