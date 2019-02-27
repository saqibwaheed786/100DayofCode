#numbers = [1,1000000]
#for number in numbers:
  #print(numbers)

#for value in range(1,20):
  #print(value)
#cubes = []
#-----------------------------------------------------------------------------------------------
#4-8. Cubes: A number raised to the third power is called a cube. For example,
#the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
#is, the cube of each integer from 1 through 10), and use a for loop to print out
#the value of each cube.

#for value in range(3,30):
#cube = value **3
  #cubes.append(cube)
  #print(cubes)
#-----------------------------------------------------------------------------------------------
#4-9. Cube Comprehension: Use a list comprehension to generate a list of the
#first 10 cubes
cubes = [value**3 for value in range (1,10)]
print(cubes)
