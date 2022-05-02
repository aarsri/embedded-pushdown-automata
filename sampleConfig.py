### Sample Machine: recognizes 'aabbccdd' ###

Q = ['q0', 'q1', 'q2', 'q3']
Sigma = ['a', 'b', 'c', 'd']
Gamma = ['B', 'C', 'D', '#']
q0 = 'q0'
QF = []
z0 = '#'
delta = {
	('q0', 'a', '#'): [('q0', ('#','B'), (None,'D',2))],
	('q0','a','B'): [('q1', (None,'B'), (None,'D',2))],
	('q0','b','B'): [('q1', ('B',None), (None,'C',2))],
	('q1','b','B'): [('q1', ('B',None), (None,'C',2))],
	('q1','c','C'): [('q2', ('C',None), (None,None,None))],
	('q2','c','C'): [('q2', ('C',None), (None,None,None))],
	('q2','d','D'): [('q3', ('D',None), (None,None,None))],
	('q3','d','D'): [('q3', ('D',None), (None,None,None))]
}

### Your Machine (uncomment out) ###
# Q = 		# set (list type) of states
# Sigma = 	# set (list type) of input alphabet symbols
# Gamma = 	# set (list type) of stack alphabet symbols
# q0 = 		# start state (string type)
# QF = 		# set (list type) of final states (typically an empty list)
# z0 = 		# stack start symbol
# delta = 	# set (dictionary type) of transition rules
