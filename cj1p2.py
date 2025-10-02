import numpy as np

'''
Prompt 2: Write a Python that prints:
1) the sum of two floating point numbers, 
2) the difference between two integers, 
3) the product of a floating point number and an integer. 
In each case, have the program print out the data type of the resulting answer.
'''

def main():
	print(f"Coding journal 1 prompt 2")	#prompt explanation
	print(f"We are asked to create Python program that prints:")
	print(f"1) the sum of two floating point numbers ")
	print(f"2) the difference between two integers ")
	print(f"3) the product of a floating point number and an integer") 
	print(f"In each case, have the program print out the data type of the resulting answer")
	print(f"-------------------------------------------------------\n")

	f1 = 1.1   #float 1
	f2 = 1.2	#float 2
	i1 = 2	#1st int 
	i2 = 3	#2nd int 
	
	print(f"My program output below:")

	float_sum = f1 + f2		#sum of float f1 and float f2
	print(f"Sum of two floating point numbers {f1} and {f2} = {float_sum}") #prints result of float_sum
	print(f"Result above has type {type(float_sum)}")	#prints type of float_sum 
	print() 	#new line

	int_diff = i1 - i2 		#difference between integers i1 and i2
	print(f"Difference between two integers {i1} and {i2} = {int_diff}")	#prints result of int_diff
	print(f"Result above has type {type(int_diff)}")	#prints type of int_diff
	print() 	#new line

	float_int_prod = f2 * i2	#product of float f2 and int i2
	print(f"Product of a floating point number {f2} and {i1} = {float_int_prod}")	#prints result of float_int_prod
	print(f"Result above has type {type(float_int_prod)}") # prints type of float_int_prod

if __name__ == "__main__":
	main()