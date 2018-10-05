import numpy as np
import math
import copy

class Rubiks:

	def __init__(self, filename):
		self.cube_state = self.import_state(filename)
		self.up = np.zeros((3, 3), dtype = int)
		self.left = np.zeros((3, 3), dtype = int)
		self.right = np.zeros((3, 3), dtype = int)
		self.front = np.zeros((3, 3), dtype = int)
		self.back = np.zeros((3, 3), dtype = int)
		self.down = np.zeros((3, 3), dtype = int)
		self.update_cube()

	def import_state(self, filename):
		fp = open(filename)
		cube_array = []
		
		for c in fp:
			cube_array.append([int(x) for x in c.split()])

		return cube_array[0]

	def update_cube(self):
		for i in range(len(self.cube_state)):
			if(i < 9):
				self.up[math.trunc((i % 9) / 3)][i % 3] = copy.deepcopy(self.cube_state[i])
			if(i >= 9 and i < 9 * 2):
				self.left[math.trunc((i % 9) / 3)][i % 3] = copy.deepcopy(self.cube_state[i])
			if(i >= 9 * 2 and i < 9 * 3):
				self.right[math.trunc((i % 9) / 3)][i % 3] = copy.deepcopy(self.cube_state[i])
			if(i >= 9 * 3 and i < 9 * 4):
				self.front[math.trunc((i % 9) / 3)][i % 3] = copy.deepcopy(self.cube_state[i])
			if(i >= 9 * 4 and i < 9 * 5):
				self.back[math.trunc((i % 9) / 3)][i % 3] = copy.deepcopy(self.cube_state[i])
			if(i >= 9 * 5 and i < 9 * 6):
				self.down[math.trunc((i % 9) / 3)][i % 3] = copy.deepcopy(self.cube_state[i])

a = Rubiks("cube.txt")
print(a.up)
print(a.left)
print(a.right)
print(a.front)
print(a.back)
print(a.down)


