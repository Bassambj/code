#tuples (tuplas)
# Tuples like a lists in python. The detail is at tuples are immutable.
# Tuples are created similarly to lists in python.
# But with parentheses ()

tupleA = ("a","b","c")

#or

tupleB = "d","e","f"

# Tuples are ideal for representing lists of constant values.
# Also to perfom operations of packaging and unpacking of values.

# using for

for element in tupleA:
    print(element)

tupleC = 100,200,300 # numbers converting in tuples is packaging

print(tupleC)

a,b = 10,20 # unpacking values - values distribuid ins variables a and b

a = 2 # value assgined to variable

tupleD = 2, # or = (2,) -> use , for mark tuple

# tuple created with lists
# using tuple function
L = [1,2,3]
T = tuple(L)
print(L)
print(T)
# a tupla nao pode ser alterada, mas uma lista ou outro elemento alteravel que
# que ela contenha sim pode ser alterado alterando o elemento, por exemplo
# alterando a lista se for a lista.