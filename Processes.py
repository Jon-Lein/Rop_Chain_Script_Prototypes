import psutil
import pefile


def get_mitigations(target):
	print(target)

	try:
		dll = pefile.PE(target)
		print("ASLR " + str(dll.OPTIONAL_HEADER.IMAGE_DLLCHARACTERISTICS_DYNAMIC_BASE))
		print("DEP " + str(dll.OPTIONAL_HEADER.IMAGE_DLLCHARACTERISTICS_NX_COMPAT))
		print("SafeSEH " + str(dll.OPTIONAL_HEADER.IMAGE_DLLCHARACTERISTICS_NO_SEH))
		print("High Entropy VA " + str(dll.OPTIONAL_HEADER.IMAGE_DLLCHARACTERISTICS_HIGH_ENTROPY_VA))
	except Exception as e:
		print(target + " Wasn't found")

pid = 8668

p = psutil.Process(pid)
# p.suspend()

j = 0

for i in p.memory_maps():
	if i.path.find('.exe') >= 0 or i.path.find('.dll') >= 0: 
		get_mitigations(i.path)
		print(i.path)
		j += 1
		print("---------------------------------------------------------------------")

print(j)
# p.resume()
