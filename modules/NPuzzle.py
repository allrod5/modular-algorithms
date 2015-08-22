import global_settings as this
from random import shuffle
import math
import copy

def solvable():
	if len(this.list_a) == 0:
		return False

	summation = 0
	for i in range(len(this.list_a)):
		for j in range(i, len(this.list_a)):
			if(this.list_a[j] != 0 and this.list_a[j]<this.list_a[i]):
				summation += 1
	if summation % 2 == 0:
		return True
	else:
		return False

def populate():
	this.dimensions = int(input("Board size: "))
	this.population = []
	this.fitness = []

	#this.block_size = math.ceil(math.log2(this.dimensions*this.dimensions))
	while not solvable():
		this.list_a = []
		for i in range(this.dimensions*this.dimensions):
			this.list_a.append(i)
		shuffle(this.list_a)

		'''for i in range(len(this.list_b)):
			tmp = [int(x) for x in bin(this.list_b[i])[2:]]
			while len(tmp)!=this.block_size:
				tmp.insert(0,0)
			this.list_a += tmp

		array = []
		for i in range(0, len(this.list_a), this.block_size):
			s = ''
			for j in range(0, this.block_size):
				s += str(this.list_a[i+j])
			array.append(int(s, 2))'''

	this.block_size = 2
	for i in range(this.popsize):
		this.population.append([])
		for j in range(this.dimensions*this.dimensions*this.dimensions):
			tmp = [int(x) for x in bin(this.randint(0,2))[2:]]
			while len(tmp)!=this.block_size:
				tmp.insert(0,0)
			this.population[i] += tmp
		this.fitness.append(check(this.population[i]))



def check(array):
	game = copy.deepcopy(this.list_a)
	this.int_a = -1
	for bit in array:
		for i in range(len(game)):
			if game[i] == 0:
				break

		if i==0 or i==this.dimensions-1 or i==len(game)-1 or i==len(game)-this.dimensions:
			mod = 1
		elif 0 < i < this.dimensions-1 or len(game)-this.dimensions < i < len(game)-1 \
			or i%this.dimensions==0 or i%this.dimensions==this.dimensions-1:
			mod = 2
		else:
			mod = 3

		moves = []
		if i%this.dimensions!=0 and i-1 != this.int_a:
			moves.append(i-1)
		if i >= this.dimensions and i-this.dimensions != this.int_a:
			moves.append(i-this.dimensions)
		if i%this.dimensions!=this.dimensions-1 and i+1 != this.int_a:
			moves.append(i+1)
		if i < len(game)-this.dimensions and i+this.dimensions != this.int_a:
			moves.append(i+this.dimensions)

		#print(moves, bit, mod, bit%mod)
		game[i], game[moves[bit%mod]] = game[moves[bit%mod]], game[i]

		this.int_a = i

		mDistance = 0
		for i in range(len(game)):
			if(game[i]):
				mDistance += abs((i)%this.dimensions-(game[i]-1)%this.dimensions)
				mDistance += abs((i)//this.dimensions-(game[i]-1)//this.dimensions)
		#print("mDistance: "+str(mDistance))
		if mDistance == 0:
			break
		if mDistance < 4:
			print(mDistance)
			for i in range(len(game)):
				if i%this.dimensions == 0:
					print()
				print(game[i], end='')
			print("\n")

	mDistance = 0
	for i in range(len(game)):
		if(game[i]):
			mDistance += abs((i)%this.dimensions-(game[i]-1)%this.dimensions)
			mDistance += abs((i)//this.dimensions-(game[i]-1)//this.dimensions)
	#print()
	#print(2*this.dimensions*this.dimensions*this.dimensions-mDistance)
	#print("\n")
	return 2*this.dimensions*this.dimensions*this.dimensions-mDistance

def stopCriteria():
	this.maxi ==  2*this.dimensions*this.dimensions*this.dimensions
	'''for i in range(1, len(array)):
		if array[i] >= array[i-1]:
			return False
	return True'''
