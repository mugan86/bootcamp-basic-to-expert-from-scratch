# int
s = "100"
# Conversión del string a entero base 2 (binario)
c = int(s, 2)
print('string converted to int base 2 : ', c)
# Conversión del string a entero base 10 (número normal)
c = int(s)
print('string converted to int base 10: ', c)

# str
print("int => string:  ", str(10))  
print("float => string:  ", str(10.0)) 
print("complex => string:  ", str(10 + 2839j))  
# "10"
# "10.0"
# "10+2839j"

# hexadecimal
s = 18  
c = hex(s) #Convierte el 18 en un valor hexadecimal  
print("Valor Hexadecimal de 18 : ", c) # 0x12

# octal
s = 18  
c = oct(s) #Convierte el 18 en un valor hexadecimal  
print("Valor Hexadecimal de 18 : ", c) 
# 0o22 (octal) <==== 010010 (en binario)

# list
print("string => list:  ", list('anartz'))  
print("int (a str) => list:  ", list(str(12))) 
print("tuple => list:  ", list(tuple('anartz'))) 
"""
string => list:   ['a', 'n', 'a', 'r', 't', 'z']
int (convertido a str) => list:   ['1', '2']
tuple => list:   ['a', 'n', 'a', 'r', 't', 'z']
"""

# set
print("string => set:  ", set('anartz'))  
print("int (a str) => set:  ", set(str(12))) 
print("tuple => set:  ", set(tuple('anartz'))) 
"""
string => set:   {'r', 't', 'n', 'z', 'a'}
int (a str) => set:   {'1', '2'}
tuple => set:   {'r', 't', 'n', 'z', 'a'}
"""
