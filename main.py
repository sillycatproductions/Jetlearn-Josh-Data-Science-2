import numpy as np

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ])
print(array[0])
print(array[0:5]) # : = Slicing

print(array[:4]) #no number before slice = from first number
print(array[4:]) #no number past slice = from number before slice to end
print(array[:]) #no numbers whatsoever = start to end


print(array[0:10:2]) #array[start : end : step(how far it travels inbetween each value)]

print(array[::-1]) #reverse array

bigthing = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(bigthing[0:2, 0:2])

thing = np.arange(1,50).reshape(7,7)
print(thing[2:5, 2:5]) #array start with 0

evenarray = array[array%2 == 0]
print(evenarray)

oddarray = array[array%2 == 1]
print(oddarray)

b = array[array == 5]
print(b) #prints 5 if it exists

b = array[array == 100]
print(b) #prints 100 if it exists

#if doesnt exist will print nothing

print(array[[2,4,6]]) #prints the indexes

print(array[array < 5])

ar = np.array([1,2,3,4,5])
coar = np.array([6,7,8,9,10])
bigar = ar + coar
print(bigar)

def linear_eqn(x):
    y = (2*x) + 3
    print(y)

linear_eqn(4)

x = np.array([1,2,3,4,5])
linear_eqn(x)