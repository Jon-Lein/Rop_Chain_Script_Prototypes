from Graphing_functions import *
from ROP_Counting_Functions import *
import os

command = ""

exit_words = ['quit', 'q', 'exit', 'stop']
rop_file = None

while command not in exit_words: # enter commands until exit
	command = input("[*]")

	# load a file in containing the ROP gadgets
	if command == 'load':
		path = input("Enter Path:")
		while not os.path.exists(path):
			path = input("Make sure the path is valid:")
			if path in exit_words:
				path = None
				break

		if path is not None:
			rop_file = prepare_gadgets(path) # returns dictionary of all gadgets split by instruction
			print("-> Loaded file")
		else:
			print("[!] No file loaded.")

	# display if / what file is loaded
	elif command == 'file':
		if rop_file is not None:
			file = path.split('\\')
			file = file[len(file) - 1] # last part of path is the actual file
			print("Loaded File --> " + file)
		else:
			print("[!] Load a file first.")

	elif command == 'count reg':
		print(count_register_use(rop_file))

	elif command == 'graph reg':
		a = count_register_use(rop_file)

		graph_gadgets(a, 'Register Graph')

	# catch anything else and make sure it isn't an exit command
	else:
		if command not in exit_words:
			print("[!] Unknown command")

