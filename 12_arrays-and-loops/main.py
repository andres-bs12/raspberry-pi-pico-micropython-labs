from machine import Pin

x = 1


# For structure
# Start - stop - uodate

print('increase 1 by 1 till 4')
for i in range(5):
    print ('i = ', i) # Print from 0 to 12


print('increase 2 by 2 till 10')
for i in range(1, 11, 2): # increas 1 by 1 till 11
    print ('i = ', i) # Print from 0 to 12


print('Print list numbers with for')
x = [5, 23, 45, 50, -23]
for i in x:
    print('i = ', i)

print('Print list items and then its letters, with for')
fruits = ['apple', 'orange', 'banana']
for fruit in fruits:
    print('i = ', fruit)
    for letter in fruit:
        print(letter)

