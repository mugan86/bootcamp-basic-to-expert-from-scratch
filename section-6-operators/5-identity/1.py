x = ["Python", "Java", "C#", "PHP"]
y = ["Python", "Java", "C#", "PHP"]
z = x

a = x is z # True
a = y is z # False
a = x is y # False

a = x is not z # False
a = y is not z # True
a = x is not y # True

y = x
a = x is z # True
a = y is z # True
a = x is y # True

a = x == y # True
a = z == y # True

print("Final")