alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
key = raw_input('Enter the key: ')
text = raw_input('Enter the text: ')
i=0;lenth=len(text)
code='';decode=''
while len(text) > len(key):
	key = key + key[i]
	i = i + 1
i=0
while i < lenth:
	cur = alph.find(key[i])
	ch = alph.find(text[i])
	code = code + alph[(ch+cur)%26]
	i=i+1
print('code: ' + code)
i=0
lenth = len(code)
while i < lenth:
	ch = alph.find(code[i])
	cur = alph.find(key[i])
	decode = decode + alph[(ch-cur)%26]
	i=i+1
print('decode: ' + decode)
