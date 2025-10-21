'''
Prompt #5:
Write a Python program that writes out:
a table of the function sin(x) vs. x 
where x is tabulated between 0 and 2 with a thousand entries 
Follow the basic Python program structure, including a main program function.
'''

import numpy as np
from astropy.table import Table #import the Table class
from astropy.io import ascii #ascii plain text io
from astropy.io import fits


def main():
	x = np.linspace(0,2*np.pi,1000) #data array, 0 to 2pi in 1000 steps
	y = np.sin(x) #data array of sin of x
	data_table = Table({'x':x, 'sin(x)':y}) #create a table
	data_table['x'].info.format = '%.5f'
	data_table['sin(x)'].info.format = '%.5f'
	ascii.write(data_table, 'x_vs_sinx.txt', format='commented_header', overwrite=True)
	data_in = ascii.read('x_vs_sinx.txt') #read data in
	print(data_in)

if __name__ == "__main__":
	main()