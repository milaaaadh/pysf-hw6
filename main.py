from MatchGame import *

# cfc : Coordinates first column
# cfr : Coordinates first row
# csc : Coordinates second column
# csr : Coordinates second row


row , column = input ( 'enter your table size by two number: ' ).split ( )
row , column = int ( row ) , int ( column )
while (row * column) % 2 != 0 :
    print ( 'Enter at least one of the numbers evenly' )
    row , column = input ( 'enter your table size by two number: ' ).split ( )
    row , column = int ( row ) , int ( column )

min_value , max_value = input ( 'enter your min, max value of table: ' ).split ( )
min_value , max_value = int ( min_value ) , int ( max_value )
if min_value > max_value :
    min_value , max_value = max_value , min_value

a = MatchGame(min_value,max_value,row,column)
primary_table = a.primary_table
a.creat_random_table()
random_table = a.random_table


# while primary_table != random_table:
while primary_table.dtype != 'int64' :
    a.show_table()

    cfr , cfc = a.get_location ('first')
    csr , csc = a.get_location ( 'second' )

    if random_table [ cfr ] [ cfc ] == random_table [ csr ] [ csc ] :
        a.correct_guess ( )
        primary_table [ cfr ] [ cfc ] = random_table [ cfr ] [ cfc ]
        primary_table [ csr ] [ csc ] = random_table [ csr ] [ csc ]
        a.primary_table = primary_table
    else :
        a.bad_guess(random_table[cfr][cfc], random_table[csr][csc], (cfr + 1 , cfc + 1), (csr + 1 , csc + 1))
    try :
        primary_table = primary_table.astype ( int )
    except :
        print ( '' )

print ( a.show_table () )
print ( 'Great job! The table is complete' )







