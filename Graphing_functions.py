import matplotlib.pyplot as plt
import numpy as np
from ROP_Counting_Functions import count_register_use, prepare_gadgets

# -----------------
# ---Process Rop---
# -----------------

gad_list = prepare_gadgets("C:\\Users\\User\\Desktop\\Rop_testing\\Gadget_sets\\arduino.txt")

c = count_register_use(gad_list)

print(c)
# exit()

# --------------------
# ---setup graphing---
# --------------------
x = []

for i in c.keys():
	x.append(i) 

objects = x
y_pos = np.arange(len(objects))
performance = c.values()

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Usage')
plt.title('Register Usage for Arduino')

plt.show()
