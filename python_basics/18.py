with open('file.txt') as f:
	for line in f:
		if line[0]=='#' or line[0]=='\n':
			continue; 
		print(line,end='')
		