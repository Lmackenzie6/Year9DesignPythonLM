import math

#Input
#What inputs are needed to calculate the volume of a cylinder?
print("Volume of a Cylinder Formula: ")

name = input("What is your name: ")#takes users name
radius = 1
height = 1

while (radius != 0 or height != 0):


	
	try:
		radius = input("input radius(cm): ")
		radius = int(radius)#cast to int

		height = input("Input height(cm): ")#input
		height = int(height)#cast to int
	except:
		print("\tNumeric Type Required")
		radius = -1
		height = -1
		

	

		
	

		
		#Process
		#What formula is used to calculate the volume of a cylinder?
		if (radius >= 0 and height >= 0):
			volume = math.pi * radius * radius * height
			volume = round(volume,2)

		#Output
		#What is important about the output?
	





		print("\nHi "+name+"!")
		print("Give a cylinder with:")
		print("Radius = "+str(radius))
		print("Height = "+str(height))
		print("The volume is: "+str(volume)) 
		print("\nV = \u03C0\u00d7radius\u00b2\u00d7height")

	else:
		print("Inputs are invalid")

		print("END PROGRAM")

