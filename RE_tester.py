import re
from ROP_Counting_Functions import count_register_use, prepare_gadgets, count_derefrenced_registers, count_instruction_reg

# --------------
# -----MAIN-----
# --------------
path = "C:\\Users\\User\\Desktop\\Rop_testing\\Gadget_sets\\"
file_name = "one_variable.txt"

# # create parsable list of gadgets broken into gadgets and instruction sets
gadget_list = prepare_gadgets(path + file_name)

# reg_inst_re = " " + instruction + " .*, " + r

instruction = 'add'

expression = " " + instruction + " "

count = 0

for i in gadget_list:
	for j in i[1]:
		if re.search(expression, j):
			count += 1
			print(str(count) + " ---" + j)
