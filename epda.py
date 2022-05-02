import random
import time
import json
import ast
from sampleConfig import Q, Sigma, Gamma, q0, QF, z0, delta

BOTTOM = 'bottom'
EMPTY_SYMBOL = None
#empty stacks are automatically deleted
#complete when everything is empty

# def readMachine(config):
# 	with open(config, 'r') as f:
# 		machine = json.load(f)
# 	Q = ast.literal_eval(machine['Q'])
# 	Sigma = ast.literal_eval(machine['Sigma'])
# 	Gamma = ast.literal_eval(machine['Gamma'])
# 	q0 = ast.literal_eval(machine['q0'])
# 	QF = ast.literal_eval(machine['QF'])
# 	z0 = ast.literal_eval(machine['z0'])
# 	delta = machine['delta']
# 	for k, v in delta.items():
# 		delta.pop(k)
# 		k = ast.literal_eval(k)
# 		delta[k] = ast.literal_eval(v)
# 	print(Q, Sigma, Gamma, q0, QF, z0, delta)
# 	return Q, Sigma, Gamma, q0, QF, z0, delta

class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

class Stack:
	def __init__(self, value=None):
		self.head = Node(BOTTOM)
		self.size = 0
		if value:
			self.push(value)
	def isEmpty(self):
		return self.size==0
	def peek(self):
		if self.isEmpty():
			raise Exception("empty stack")
		return self.head.next.value
	def push(self, value):
		node = Node(value)
		node.next = self.head.next
		self.head.next = node
		self.size += 1
	def pop(self):
		if self.isEmpty():
			raise Exception("empty stack")
		remove = self.head.next
		self.head.next = self.head.next.next
		self.size -= 1
		return remove.value
	def posPush(self, value, pos):
		if self.isEmpty():
			raise Exception("empty stack")
		popped_vals = []
		for i in range(pos-1):
			popped_vals.append(self.pop())
		self.push(value)
		popped_vals.reverse()
		for val in popped_vals:
			self.push(val)
	def strPrint(self):
		cur = self.head.next
		out = ""
		while cur:
			if isinstance(cur.value,Stack):
				cur2 = cur.value.head.next
				out2 = ''
				while cur2:
					out2 += str(cur2.value) + '->'
					cur2 = cur2.next
				out += '['+out2+']'+'->'
			else:
				out += str(cur.value) + "->"
			cur = cur.next
		return out

def main():
	tape = input('please provide your input tape (symbols with no separation)\n')
	state = q0
	epda = Stack(value=Stack(value=z0))
	i = 0
	while i<len(tape):
		char = tape[i]
		if char not in Sigma:
			print("symbol not in Sigma")
			break
		print('\nCurrent state: ' + state)
		print('Reading symbol 1: ' + char)
		if (state, char, epda.peek().peek()) not in delta.keys():
			print('rule not in delta')
			break
		transitions = delta[(state, char, epda.peek().peek())]
		transition = random.choice(transitions)
		
		if len(transitions)>1: #non-determinism
			epda_temp = epda
			state = transition[0]
			if transition[1][0]:
				epda_temp.peek().pop()
			if transition[1][1]:
				epda_temp.peek().push(transition[1][1])
			if transition[2][0]:
				epda_temp.pop()
			if transition[2][1]:
				epda_temp.posPush(Stack(value=transition[2][1]), transition[2][2])
			# cleanup - remove empty stacks
			popped_vals = []
			while not epda_temp.isEmpty():
				popped = epda_temp.pop()
				if not popped.isEmpty():
					popped_vals.append(popped)
			popped_vals.reverse()
			for val in popped_vals:
				epda_temp.push(val)
			# print out
			print('Current view of stack (Right=Top):')
			print(epda_temp.strPrint())
			nd = input('This step involved nondeterminism. Would you like to try this step again? Y/N')
			if nd=='N':
				epda = epda_temp
		else:
			state = transition[0]
			if transition[1][0]:
				epda.peek().pop()
			if transition[1][1]:
				epda.peek().push(transition[1][1])
			if transition[2][0]:
				epda.pop()
			if transition[2][1]:
				epda.posPush(Stack(value=transition[2][1]), transition[2][2])
			# cleanup - remove empty stacks
			popped_vals = []
			while not epda.isEmpty():
				popped = epda.pop()
				if not popped.isEmpty():
					popped_vals.append(popped)
			popped_vals.reverse()
			for val in popped_vals:
				epda.push(val)
			# print out
			print('Current view of stack (Right=Top):')
			print(epda.strPrint())
			i += 1
		time.sleep(1)
	
	print()
	if len(QF)==0:
		if epda.isEmpty():
			print('accepted')
		else:
			print('rejected')
	else:
		if state in qF:
			print('accepted')
		else:
			print('rejected')

if __name__ == '__main__':
	main()
