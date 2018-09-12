import numpy as np
from random import randint

class Square:
	def __init__(self, color):
		self.color = color

class Face:
	def __init__(self, color):
		self.squares = []
		for i in range(0, 9):
			self.squares.append(Square(color))

	def print_face(self):
		for i in range(0, 9):
			if (i + 1) % 3 == 0:
				print(self.squares[i].color)
			else:
				print(self.squares[i].color, end = " ")

	def rotate_cw(self):
		aux = self.squares[0]
		self.squares[0] = self.squares[6]
		self.squares[6] = self.squares[8]
		self.squares[8] = self.squares[2]
		self.squares[2] = aux
		aux = self.squares[1]
		self.squares[1] = self.squares[3]
		self.squares[3] = self.squares[7]
		self.squares[7] = self.squares[5]
		self.squares[5] = aux

	def rotate_ccw(self):
		aux = self.squares[0]
		self.squares[0] = self.squares[2]
		self.squares[2] = self.squares[8]
		self.squares[8] = self.squares[6]
		self.squares[6] = aux
		aux = self.squares[1]
		self.squares[1] = self.squares[5]
		self.squares[5] = self.squares[7]
		self.squares[7] = self.squares[3]
		self.squares[3] = aux

	def mirror(self):
		aux = self.squares[0]
		self.squares[0] = self.squares[2]
		self.squares[2] = aux
		aux = self.squares[3]
		self.squares[3] = self.squares[5]
		self.squares[5] = aux
		aux = self.squares[6]
		self.squares[6] = self.squares[8]
		self.squares[8] = aux
	
	def mirror_vert(self):
		aux = self.squares[0]
		self.squares[0] = self.squares[6]
		self.squares[6] = aux
		aux = self.squares[1]
		self.squares[1] = self.squares[7]
		self.squares[7] = aux
		aux = self.squares[2]
		self.squares[2] = self.squares[8]
		self.squares[8] = aux


class Cube:

	def __init__(self):
		self.main = Face('r')
		self.up = Face('g')
		self.down = Face('b')
		self.left = Face('y')
		self.right = Face('w')
		self.back = Face('o')
		self.fit = 0

	def print_cube(self):
		print("       " + self.up.squares[0].color + " " + self.up.squares[1].color + " " + self.up.squares[2].color)
		print("       " + self.up.squares[3].color + " " + self.up.squares[4].color + " " + self.up.squares[5].color)
		print("       " + self.up.squares[6].color + " " + self.up.squares[7].color + " " + self.up.squares[8].color)
		print()
		
		print(self.left.squares[0].color + " " + self.left.squares[1].color + " " + self.left.squares[2].color, end = "  ")
		print(self.main.squares[0].color + " " + self.main.squares[1].color + " " + self.main.squares[2].color, end = "  ")
		print(self.right.squares[0].color + " " + self.right.squares[1].color + " " + self.right.squares[2].color)

		print(self.left.squares[3].color + " " + self.left.squares[4].color + " " + self.left.squares[5].color, end = "  ")
		print(self.main.squares[3].color + " " + self.main.squares[4].color + " " + self.main.squares[5].color, end = "  ")
		print(self.right.squares[3].color + " " + self.right.squares[4].color + " " + self.right.squares[5].color)
		
		print(self.left.squares[6].color + " " + self.left.squares[7].color + " " + self.left.squares[8].color, end = "  ")
		print(self.main.squares[6].color + " " + self.main.squares[7].color + " " + self.main.squares[8].color, end = "  ")
		print(self.right.squares[6].color + " " + self.right.squares[7].color + " " + self.right.squares[8].color)
		print()

		print("       " + self.down.squares[0].color + " " + self.down.squares[1].color + " " + self.down.squares[2].color)
		print("       " + self.down.squares[3].color + " " + self.down.squares[4].color + " " + self.down.squares[5].color)
		print("       " + self.down.squares[6].color + " " + self.down.squares[7].color + " " + self.down.squares[8].color)
		print()
		
		print("       " + self.back.squares[0].color + " " + self.back.squares[1].color + " " + self.back.squares[2].color)
		print("       " + self.back.squares[3].color + " " + self.back.squares[4].color + " " + self.back.squares[5].color)
		print("       " + self.back.squares[6].color + " " + self.back.squares[7].color + " " + self.back.squares[8].color)
		print()

	def array_check_colors(self, face):
		a = []
		for i in range(0, 9):
			if face.squares[i].color == "r":
				a.append(1)
			if face.squares[i].color == 'g':
				a.append(2)
			if face.squares[i].color == 'b':
				a.append(3)
			if face.squares[i].color == 'y':
				a.append(4)
			if face.squares[i].color == 'w':
				a.append(5)
			if face.squares[i].color == 'o':
				a.append(6)
		return a

	def array(self):
		a = []
		a.append(self.array_check_colors(self.up))
		a.append(self.array_check_colors(self.left))
		a.append(self.array_check_colors(self.main))
		a.append(self.array_check_colors(self.right))
		a.append(self.array_check_colors(self.down))
		a.append(self.array_check_colors(self.back))
		return np.array(a).flatten()

	def rotate(self):
		self.main.rotate_cw()
		self.back.rotate_ccw()
		self.left.rotate_cw()
		self.right.rotate_cw()
		self.up.rotate_cw()
		self.down.rotate_cw()
		aux = self.right
		self.right = self.up
		self.up = self.left
		self.left = self.down
		self.down = aux

	def change_up_main(self):
		self.left.rotate_cw()
		self.right.rotate_ccw()
		aux = self.main
		self.main = self.up
		self.up = self.back
		self.back = self.down
		self.down = aux

	def change_down_main(self):
		self.left.rotate_ccw()
		self.right.rotate_cw()
		aux = self.main
		self.main = self.down
		self.down = self.back
		self.back = self.up
		self.up = aux

	def change_left_main(self):
		self.up.rotate_ccw()
		self.down.rotate_cw()
		self.back.mirror()
		self.back.mirror_vert()
		self.right.mirror()
		self.right.mirror_vert()
		aux = self.main
		self.main = self.left
		self.left = self.back
		self.back = self.right
		self.right = aux
	
	def change_right_main(self):
		self.up.rotate_cw()
		self.down.rotate_ccw()
		self.left.mirror()
		self.left.mirror_vert()
		self.back.mirror()
		self.back.mirror_vert()
		aux = self.main
		self.main = self.right
		self.right = self.back
		self.back = self.left
		self.left = aux

	def rotate_right_row_up(self):
		aux = []
		aux.append(self.main.squares[2])
		aux.append(self.main.squares[5])
		aux.append(self.main.squares[8])

		self.right.rotate_ccw()

		self.main.squares[2] = self.up.squares[2]
		self.main.squares[5] = self.up.squares[5]
		self.main.squares[8] = self.up.squares[8]

		self.up.squares[2] = self.back.squares[2]
		self.up.squares[5] = self.back.squares[5]
		self.up.squares[8] = self.back.squares[8]

		self.back.squares[2] = self.down.squares[2]
		self.back.squares[5] = self.down.squares[5]
		self.back.squares[8] = self.down.squares[8]

		self.down.squares[2] = aux[0]
		self.down.squares[5] = aux[1]
		self.down.squares[8] = aux[2]

	def rotate_right_row_down(self):
		aux = []
		aux.append(self.main.squares[2])
		aux.append(self.main.squares[5])
		aux.append(self.main.squares[8])

		self.right.rotate_cw()

		self.main.squares[2] = self.down.squares[2]
		self.main.squares[5] = self.down.squares[5]
		self.main.squares[8] = self.down.squares[8]

		self.down.squares[2] = self.back.squares[2]
		self.down.squares[5] = self.back.squares[5]
		self.down.squares[8] = self.back.squares[8]

		self.back.squares[2] = self.up.squares[2]
		self.back.squares[5] = self.up.squares[5]
		self.back.squares[8] = self.up.squares[8]

		self.up.squares[2] = aux[0]
		self.up.squares[5] = aux[1]
		self.up.squares[8] = aux[2]

	def move(self, mov):
		for i in mov:
			if i == 0:
				self.rotate_right_row_up()
			if i == 1:
				self.rotate()
			if i == 2:
				self.change_right_main()
			if i == 3:
				self.change_up_main()
		#	if i == 4:
		#		self.rotate_right_row_down()
		#	if i == 5:
		#		self.rotate()
		#		self.rotate()
		#		self.rotate()
		#	if i == 6:
		#		self.change_left_main()
		#	if i == 7:
		#		self.change_down_main()
	
	def generate_random_moves(self, max, mov):
		for i in range(0, max):
			mov.append(randint(0, 3))

	def solve(self, mov):
		vom = mov[::-1]
		for i in range(0, len(vom)):
			vom[i] = vom[i] + 4
		return vom

	def insert_cube_colors(self, face, number, index):
		if number == 1:
			face.squares[index].color = "r"
		if number == 2:
			face.squares[index].color = "g"
		if number == 3:
			face.squares[index].color = "b"
		if number == 4:
			face.squares[index].color = "y"
		if number == 5:
			face.squares[index].color = "w"
		if number == 6:
			face.squares[index].color = "o"
		
	def read_cube(self, filename):
		a = np.loadtxt(filename)
		for i in range(0, 9):
			self.insert_cube_colors(self.up, a[i], i % 9)
		for i in range(9, 18):
			self.insert_cube_colors(self.left, a[i], i % 9)
		for i in range(18, 27):
			self.insert_cube_colors(self.main, a[i], i % 9)
		for i in range(27, 36):
			self.insert_cube_colors(self.right, a[i], i % 9)
		for i in range(36, 45):
			self.insert_cube_colors(self.down, a[i], i % 9)
		for i in range(45, 54):
			self.insert_cube_colors(self.back, a[i], i % 9)
			