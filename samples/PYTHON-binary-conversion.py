print('Binary Conversion - Python 3.6')
stringInput = input('Type your string:')

print('\n--------------------------------------------------')

binary_with_space = ' '.join(format(ord(i),'b').zfill(8) for i in stringInput)
binary_no_space  = ''.join(format(ord(i),'b').zfill(8) for i in stringInput)

print("\nString: '%s' in binary:\n%s"%(stringInput,binary_with_space))
print('\n--------------------------------------------------\n')

def binary_to_string(b):
   return ''.join(chr(int(b[i*8:i*8+8],2)) for i in range(len(b)//8))

stringBin = binary_to_string(binary_no_space)

print("Binary numer:'%s' to string:%s\n"%(binary_with_space,stringBin))
print('\n--------------------------------------------------\n')



