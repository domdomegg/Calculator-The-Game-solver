def rev(o):
	return int(str(abs(o))[::-1])*sign(o)

def sign(o):
	if o == 0:
		return 1
	return abs(o)//o

def bac(o):
	if(abs(o) < 10):
		return 0
	return int(str(o)[:-1])

def rep(o, f, t):
	return int(str(o).replace(str(f), str(t)))

def plus(o, n):
	return o + n

def minus(o, n):
	return o - n

def times(o, n):
	return o * n

def divide(o, n):
	return o // n

def append(o, n):
	return int(str(o) + str(n))

def flip(o):
	return -o

def buttontofunc(button):
	if button == 'rev' or button == 'reverse':
		return rev
	if button == 'flip':
		return flip
	if  button == 'bac' or button == 'back' or button == '<<':
		return bac
	if button[0] == '+':
		return lambda x: plus(x, int(str(button[1:])))
	if button[0] == '-':
		return lambda x: minus(x, int(str(button[1:])))
	if button[0] == '*' or button[0] == 'x' or button[0] == 'X':
		return lambda x: times(x, int(str(button[1:])))
	if button[0] == '/' or button[0] == '[' or button[0] == ']' or button[0] == '|':
		return lambda x: divide(x, int(str(button[1:])))
	if button[0] == 'a':
		return lambda x: append(x, int(str(button[1:])))
	if button[0] == 'r':
		return lambda x: rep(x, int(button[1:].split(',')[0]), int(button[1:].split(',')[1]))
	# TODO: do this better
	if button[0] == 'b':
		return lambda x: x

# Stolen from itertools
def product(*args, repeat=1):
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)

def trybuttons(order, start, goal, buttons, buttonfuncs):
	o = start

	for i in order:
		o = buttonfuncs[i](o)
		if o == goal:
			printorder(order, buttons)

def printorder(order, buttons):
	print('== RESULTS ==')

	for i in order:
		print(buttons[i])

	print('')

def getdata():
	print('== INPUT ==')

	start = int(input('Start: '))
	moves = int(input('Moves: '))
	goal = int(input('Goal: '))
	numbuttons = int(input('Number of buttons: '))
	buttons = []

	for i in range(0, numbuttons):
		buttons.append(input('Button ' + str(i) + ': '))

	buttons = tuple(buttons)

	print('')

	return {
		"start": start,
		"moves": moves,
		"goal": goal,
		"buttons": buttons,
		"buttonfuncs": buttonstofuncs(buttons)
	}

def buttonstofuncs(buttons):
	return tuple(map(buttontofunc, buttons))

def solve(data):
	for i in product(range(0, len(data["buttons"])), repeat=data["moves"]):
		trybuttons(i, data["start"], data["goal"], data["buttons"], data["buttonfuncs"])

'''
while True:
	data = getdata();
	solve(data)
'''