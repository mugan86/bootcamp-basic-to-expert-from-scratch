x = 12_829      # int
y = -345.8      # float
z = 456 +1j     # complex

#convertir de entero a float:
a = float(x)        # 12829.0
#convertir del float a int:
b = int(y)          # -345
#convertir de int a un complex:
c = complex(x)      # 12829 + 0j
#convertir de float a un complex:
d = complex(y)      # -345.8 + 0j

# De comple a int / float
e = float(d.real)   # -345.8
f = int(c.real)     # 12829
e = int(d.real)   # -345

print("Final")