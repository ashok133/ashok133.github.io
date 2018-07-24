# def poetryformatter():

all_poems = ''
line_num = 0
with open('poems.txt','rb') as fp:
	for line in fp:
		if line_num == 1:
			line = line+"</br></br>"
			all_poems += line
		else:
			line = line+"</br>"
			all_poems += line
		line_num = line_num + 1

print all_poems

