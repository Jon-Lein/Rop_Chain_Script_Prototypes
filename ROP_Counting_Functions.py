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


def count_register_use(reg_array, register):
	count = 0
	for i in reg_array: # search through each gadget
		for j in i[1]:  # search through each instruction in gadget
			if j.find(register) >= 0:
				count += 1
	return count


def count_derefrenced_registers(g_array, register, s_or_d):
	count = 0
	if s_or_d == "source" or s_or_d == "s":
		search_start = "[" + register
		search_end = "],"
	elif s_or_d == "destination" or s_or_d == "d":
		search_start = "[" + register
		search_end = "] "

	for i in g_array: # search through each gadget
		for j in i[1]:  # search through each instruction in gadget
			if j.find(search_start) >= 0 and j.find(search_end) >= 0:
				count += 1
	return count


regs = ['eax', 'ebx', 'ecx', 'edx', 'esi', 'edi', 'ebp', 'esp']

gadget_list = prepare_gadgets('server.results.txt')

print("---All Register Usage---")
for r in regs:
	print(str(r) + " " + str(count_register_use(gadget_list, r)))

print("---Derefrenced Register Source Usage---")
for r in regs:
	print(str(r) + " " + str(count_derefrenced_registers(gadget_list, r, 's')))

print("---Derefrenced Register Destination Usage---")
for r in regs:
	print(str(r) + " " + str(count_derefrenced_registers(gadget_list, r, 'd')))