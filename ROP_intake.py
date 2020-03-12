#example of importing results from ROPChain.py to a readable format

import random

f = open('server.results.txt', 'r')

gadgets = f.read()

gadgets = gadgets.split('\n')

# print(gadgets[2]) # first gadget
# print(gadgets[len(gadgets)-4]) # last gadget
print("--------------------------")

print(gadgets[len(gadgets) - 2]) # number of unique gadgets

# print(num)
num = random.randrange(2, (len(gadgets) - 4))

g = gadgets[num]
g = g.replace(':', "*$", 1)
g = g.split('*$')
g[1] = g[1].split(';')

print("Instructions in gadget #" + str(num) + " : "  + str(len(g[1])))
print("Starting Address: " + g[0])
print("--------------------------")
for i in g[1]:
	print(i)
print("--------------------------")

