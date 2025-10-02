import numpy as numpy

'''
Prompt 3:
Write a Python program that:
1) defines a function f(x) that returns x**3 + 8. 
2) In the main function of the program, call f(x) with x = 9 and print the result.  
Use an if statement that executes if the result is larger than 27 and prints “YAY!”.
'''

#1)
def f(x):
	return x**3 + 8

print(f"f(x) = x**3 + 8")

#2)
def main():
	result = f(9) #calls f(x) with x=9
	print(f"f(9) = {result}")

	if result>27: # if result bigger than 27 it prints Yay!
		print("Yay!")

if __name__ == "__main__":
	main()