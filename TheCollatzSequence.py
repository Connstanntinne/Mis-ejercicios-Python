# progamando la secuencia de Collatz

import math

number= 0
def collatz():
    print(number // 2)

print('escriba un número')
number= int(input())

if number % 2 == 0:
    print (number // 2)
    
else:
    while number > 1:
        if number % 2 == 1:    
            number= int (3* number + 1)
            print(number)
        elif number % 2 != 1:
            number= int(number // 2)
            print (number)
  







# pagina 77 de libr automatizar