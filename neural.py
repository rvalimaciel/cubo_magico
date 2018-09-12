import numpy as np
from rubiks import Square, Face, Cube

class Neural:
	def __init__(self, input, cube_index):
		self.input = input
		self.cube_index = cube_index
		self.input_pesos = self.read_pesos("input_pesos" + str(self.cube_index) + ".txt")
		self.output_pesos = self.read_pesos("output_pesos" + str(self.cube_index) + ".txt")
		self.nodes = np.empty(54)
		self.rotate_right_row_up = 0
		self.rotate = 0
		self.change_right_main = 0
		self.change_up_main = 0
		
		
	def create_input_pesos(self):
		f = open("input_pesos" + str(self.cube_index) + ".txt", "w")
		aux = np.random.random_integers(-10, 10, size=(54,54))
		for i in range(0, 54):
			for j in range(0, 54):
				f.write(str(aux[i][j]) + " ")
			f.write("\n")
		return f

	def create_output_pesos(self):
		f = open("output_pesos" + str(self.cube_index) + ".txt", "w")
		aux = np.random.random_integers(-10, 10, size=(4,54))
		for i in range(0, 4):
			for j in range(0, 54):
				f.write(str(aux[i][j]) + " ")
			f.write("\n")
		return f

	#def create_input(self)

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

	def update(self):
		np.savetxt('input_pesos' + str(self.cube_index) +'.txt', self.input_pesos , delimiter=' ')		
		np.savetxt("output_pesos" + str(self.cube_index) + ".txt",self.output_pesos, delimiter=' ')
		np.savetxt('cubo' + str(self.cube_index) +'.txt', self.input , delimiter=' ')
		
#codigo pra gerar novos pesos aleatorios FIX THIS!!!!
n = []
for i in range(0, 10):
	n.append(Neural([], i))
	n[i].create_input_pesos()
	n[i].create_output_pesos()
	n[i].update()

