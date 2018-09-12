import numpy as np
from rubiks import Square, Face, Cube
from neural import Neural

class Genetica:
	def __init__(self):
		self.cube_number = 10
		self.best_cube_index = 0
		self.cube_array = []
		self.neural_array = []
		self.make_cubes(self)
		self.fit_max = self.cube_array[self.best_cube_index].fit
		
	def make_cubes(self):
		cubes = []
		neural = []
		for i in range(0, self.cube_number):
			cubes.append(Cube())
			cubes[].read_cube("scrambled_cube1.txt")
			neural.append(Neural(cube[i].array(), i))
		self.cube_array = cubes
		self.neural_array = neural


	def calc_fit_cube(self, c):
		fit = 0
		aux = c.array()
		for i in range(0, 9):
			if aux[i] == aux[4]: fit++
		for i in range(9, 18):
			if aux[i] == aux[13]: fit++
		for i in range(18, 27):
			if aux[i] == aux[22]: fit++
		for i in range(27, 36):
			if aux[i] == aux[31]: fit++
		for i in range(36, 45):
			if aux[i] == aux[40]: fit++
		for i in range(45, 54):
			if aux[i] == aux[49]: fit++
		c.fit = fit

	def calc_fit(self):
		for c in self.cube_array:
			self.calc_fit_cube(c)
#==============================================================================
	def transa(self):
		for c in self.cube_array:
			if c != cube_array[self.best_cube_index]:

				


	

