#AycockChristopher
#P3T1
#CTI110
#06/24/2018

#dimensions of rectangle 1
length1 = int(input('Enter the length of rectangle 1: '))
width1 = int(input('Enter the width of rectangle 1: '))

#dimensions of rectangle 2
length2 = int(input('Enter the length of rectangle 2: ' ))
width2 = int(input(' Enter the width of rectangle 2 : '))

#calculate the areas of rectangles
area1 = length1 * width1
area2 = length2 * width2

# determine which has greater area
if area1 > area2:
    print('Rectangle 1 has the greater area.')
elif area2 > area1:
    print('Rectangle 2 has the greater area.')
else:
    print('Both have the same area.')
