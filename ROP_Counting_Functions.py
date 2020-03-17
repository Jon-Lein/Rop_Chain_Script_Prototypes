import collections

# -------------------
# -----FUNCTIONS-----
# -------------------

def prepare_gadgets(ROP_file):
	f = open(ROP_file, "r")
	gadgets = f.read()
	gadgets = gadgets.split('\n')

	preped_gadgets = []

	for g in gadgets[2:len(gadgets)-4]:
		g = g.replace(':', "*$", 1) # replace formatting # with other symbol for splitting purposes
		g = g.split('*$')
		g[1] = g[1].split(';')

		preped_gadgets.append(g)

	# returns in form of:
	# [address of gadget [list of instructions in gadget]]
	return preped_gadgets


def count_register_use(g_array):
	registers = {'eax': 0, 'ebx':0, 'ecx':0, 'edx':0, 'edi':0, 'esi':0, 'esp':0, 'ebp':0}
	
	for r in registers:
		for i in g_array: # search through each gadget
			for j in i[1]:  # search through each instruction in gadget
				if j.find(r) >= 0:
					registers[r] += 1
	return registers


def count_derefrenced_registers(g_array, s_or_d):
	registers = collections.OrderedDict()
	registers = {'eax': 0, 'ebx':0, 'ecx':0, 'edx':0, 'edi':0, 'esi':0, 'esp':0, 'ebp':0}

	for r in registers:
		if s_or_d == "source" or s_or_d == "s":
			search_start = "[" + r
			search_end = "],"
		elif s_or_d == "destination" or s_or_d == "d":
			search_start = "[" + r
			search_end = "] "

		for i in g_array: # search through each gadget
			for j in i[1]:  # search through each instruction in gadget
				if j.find(search_start) >= 0 and j.find(search_end) >= 0:
					registers[r] += 1
	return registers


def count_math_ops(g_array):
	registers = {}
	operations = []


# --------------
# -----MAIN-----
# --------------
# path = "C:\\Users\\User\\Desktop\\Rop_testing\\Gadget_sets\\"
# file_name = "gain_dll.txt"

# # create parsable list of gadgets broken into gadgets and instruction sets
# gadget_list = prepare_gadgets(path + file_name)

# print("---All Register Usage---")

# c = count_register_use(gadget_list)

# regs = dict(eax=0, ebx=0, ecx=0)
# regs = {'eax':0, 'ebx':0, 'ecx':0}

# for i in regs.items():
	# print(i)
# # use dict keys to preserve declaration order
# for i in c.keys():
# 	print(i + " ---> " + str(c[i]))

# print("---Derefrenced Register Source Usage---")
# deref_c = count_derefrenced_registers(gadget_list, 'source')
# for i in deref_c.keys():
# 	print(i + " ---> " + str(deref_c[i]))

# print("---Derefrenced Register Destination Usage---")
# deref_c = count_derefrenced_registers(gadget_list, 'destination')
# for i in deref_c.keys():
# 	print(i + " ---> " + str(deref_c[i]))
