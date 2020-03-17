import matplotlib.pyplot as plt
import numpy as np
import collections
from ROP_Counting_Functions import count_register_use, prepare_gadgets, count_derefrenced_registers

# --------------------
# ---setup graphing---
# --------------------

def graph_gadgets(gadget_list, title):
	x = []

	for i in gadget_list.keys():
		x.append(i) 

	objects = x
	y_pos = np.arange(len(objects))
	performance = gadget_list.values()

	plt.bar(y_pos, performance, align='center', alpha=0.5)
	plt.xticks(y_pos, objects)
	plt.ylabel('Times Used')
	plt.title(title)

	# add labels to height of bars
	for i,v in enumerate(performance):
		plt.text(i-0.2, v+0.1, str(v))

	plt.show()


# -----------------
# ---Process Rop---
# -----------------

gad_list = prepare_gadgets("C:\\Users\\User\\Desktop\\Rop_testing\\Gadget_sets\\one_variable.txt")

a = count_register_use(gad_list)
b = count_derefrenced_registers(gad_list, 's')
c = count_derefrenced_registers(gad_list, 'd')
graphs = [a,b,c]

for i in graphs:
	graph_gadgets(i, str(i))
