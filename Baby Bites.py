a = int( input() )
b = input().split()
nike = True
for i in range( a ):
    if b[ i ] != 'mumble':
        if ( int(b[i]) - 1 ) != i :
            nike = False
            break
if nike :
    print("makes sense")
else:
    print( "something is fishy")
