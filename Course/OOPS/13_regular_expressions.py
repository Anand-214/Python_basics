mystr = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum aiii  aai   ai aaaaiiii"


print(r'Varma\n\t@')
#mystr1 = "Anand Kulkarni Mirafra Technologies"
#import re
#patt = re.compile(r'ai*')
#patt = re.compile(r'a*i+')
#patt = re.compile(r'a+i+ | in the 1960s')
#patt = re.compile(r'(a{2}i+)')
#patt = re.compile(r'^Anand')
#patt = re.compile(r'\D{6}')
#matches = patt.finditer(mystr)
#for match in matches:
#		print(match)

import re
txt = "The indian rains are the rains in rains"
x = re.search("rains",txt)
print(x.start())
y = re.findall("rains",txt)
print(x)
print(y)

my_txt = "The indian massive snow leopard"
x1 = re.split("\s",my_txt)
print(x1)


'''
patt = re.compile(r'---Syntax---')
matches = patt.finditer(mystr)
for match in matches:
	if match:
		print(match)
	else:
		print("No match")
'''	
