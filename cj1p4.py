'''
Write a Python program that declares a class describing your favorite animal. 
Have the data members of the class represent the following physical parameters of the animal: 
length of the arms (float),
length of the legs (float), 
number of eyes (int), 
does it have a tail? (bool), 
is it furry? (bool). 
Write an initialization function that sets the values of the data members when an 
instance of the class is created. 
Write a member function of the class to print out and describe the data members 
representing the physical characteristics of the animal.
'''


		#55 cm arm length 
		#65 cm leg length
		#2 eyes
		#has a tail
		#very furry


class My_favorite_animal:

	def __init__(self, length_of_arms, length_of_legs,  number_of_eyes, tail_existence,
		is_it_furry): 

		self.length_of_arms = float(length_of_arms)
		self.length_of_legs = float(length_of_legs)
		self.number_of_eyes = int(number_of_eyes)
		self.tail_existence = bool(tail_existence)
		self.is_it_furry = bool(is_it_furry)

	def describe(self):
		print(f"Snow leopards front legs can be around {self.length_of_arms} cm")
		print(f"Their hind legs can be around {self.length_of_legs} cm")
		print(f"They have {self.number_of_eyes} eyes")

		if self.tail_existence:
			print("Snow leopards have a very bushy tail")
		else:
			print("Snow leopards don't have a tail")

		if self.is_it_furry:
			print("Snow leopards are exceptionally furry to "
				"deal with extreme cold temperatures")
		else:
			print("Snow leopards aren't furry")


def main():
	snow_leopard = My_favorite_animal(length_of_arms=55, length_of_legs=65, number_of_eyes=2, 
		tail_existence=True, is_it_furry=True)
	snow_leopard.describe()

if __name__ == "__main__":
	main()
