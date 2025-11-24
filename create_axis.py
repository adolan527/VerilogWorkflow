import sys



def main():
	args = sys.argv[1].split(' ')
	if len(args) > 3:
		print("Usage: python create_axis.py [MODE] [TYPE] [NAME]")
		print("Mode: d(efinition), i(nstantiation), w(ire). Default: definition")
		print("Types: s(lave), m(aster). Defualt: slave")
		return
		

	mode = 'd'
	if len(args) >= 1:
		if args[0][0].lower() not in ['d', 'i', 'w']:
			print("Invalid mode: ",args[0])
			return
		mode = args[0][0]
		
	type = 's'
	if len(args) >= 2:
		if args[1][0].lower() not in ['s', 'm']:
			print("Invalid type: ",args[1])
			return
		type = args[1][0]
		
	name = ''
	if len(args) >= 3:
		name = args[2] + "_"
		
		
	
	fields = ["tdata", "tvalid", "tready", "tlast", "tuser", "tid" ] #tdest, tkeep, tstrb, etc, not included
	prefix = ""
	suffix = ""
	if mode == 'd':
		suffix = ","
		if type == 's':
			prefix = "input\t[0:0]\t"
		else:
			prefix = "output\t[0:0]\t"
	elif mode =='i':
		suffix = ","
		prefix = "."
	else:
		suffix = ";"
		prefix = "wire\t[0:0]\t"
	
	
	
	
	base = f"{type}_axis_{name}"
	for field in fields:
		output_str = f"{prefix}{base}{field}"
		if mode == 'i':
			output_str +=  f"({base}{field})"
		
		print(output_str+suffix)
		




if __name__ == "__main__":
	main()