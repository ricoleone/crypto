#generate the sequence of numbers up to 23 raised to a power mod 23 for the first 22 outputs, show the distnct set to the right
for i in range(1, 23):
    print( i, [pow(i,j,23) for j in range(23)], "\t\t", set([pow(i,j,23) for j in range(23)]) )

#try a smaller st
print("\n\n",[pow(3,i,7) for i in range(7)])
print([pow(3,i*2,7) for i in range(7)])
print([pow(3,i*3,7) for i in range(7)])
print([pow(3,i*4,7) for i in range(7)])
print([pow(3,i*5,7) for i in range(7)])
print([pow(3,i*6,7) for i in range(7)])
print([pow(3,i*7,7) for i in range(7)])