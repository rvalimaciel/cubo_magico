import numpy as np
from rubiks import Square, Face, Cube

class Neural:
	def __init__(self, input):
		self.input = input
		self.input_pesos = self.read_pesos("pesos1.txt")
		self.output_pesos = self.read_pesos("output_pesos1.txt")
		self.nodes = np.empty(54)
		self.rotate_right_row_up = 0		
		self.rotate = 0
		self.change_right_main = 0
		self.change_up_main = 0
		
	def create_pesos(self, it):
		f = open("output_pesos" + str(it) + ".txt", "w")
		aux = np.random.random_integers(-1, 1, size=(54,54))
		for i in range(0, 4):
			for j in range(0, 54):
				f.write(str(aux[i][j]) + " ")
			f.write("\n")
		return f

	def read_pesos(self, filename):
		input = np.loadtxt(filename)
		return input

	def relu(self, input):
		return(max(0, input))

	def check_move(self, cube):
		print([self.rotate_right_row_up, self.rotate, self.change_right_main, self.change_up_main])
		
		max_out = max([self.rotate_right_row_up, self.rotate, self.change_right_main, self.change_up_main]) 
		
		if max_out == self.rotate_right_row_up:
			cube.rotate_right_row_up()
			return 0
		if max_out == self.rotate:
			cube.rotate()
			return 1
		if max_out == self.change_right_main:
			cube.change_right_main()
			return 2
		if max_out == self.change_up_main:
			cube.change_up_main()
			return 3

	def propagate(self, cube):
		for i in range(0, len(self.nodes)):
			self.nodes[i] = (self.input * self.input_pesos[i]).sum()
			self.nodes[i] = self.relu(self.nodes[i])
		self.rotate_right_row_up = (self.nodes * self.output_pesos[0]).sum()		
		self.rotate = (self.nodes * self.output_pesos[1]).sum()
		self.change_right_main = (self.nodes * self.output_pesos[2]).sum()
		self.change_up_main = (self.nodes * self.output_pesos[3]).sum()
		self.check_move(cube)
		self.input = cube.array()



a = Cube()
a.read_cube("scrambled_cube1.txt")
a.print_cube()
n = Neural(a.array())



n.propagate(a)
a.print_cube()
n.propagate(a)
a.print_cube()
n.propagate(a)
a.print_cube()
n.propagate(a)
a.print_cube()
n.propagate(a)
a.print_cube()
