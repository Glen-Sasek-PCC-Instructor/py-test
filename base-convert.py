# https://stackoverflow.com/questions/21765779/converting-binary-to-decimal-integer-output

binary = input('enter a binary number: ')
print(int(binary, 2))

n = int(input('enter a decimal number: '))
print('{0:b}'.format(n))

