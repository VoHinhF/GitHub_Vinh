
def encodeString(s):
	i = 0
	y = len(s) - 1
	code = []
	k = 0
	while i < y:
		
		if s[i] != s[i+1]:
			code.append(s[i]+str(s.count(s[i],k,i+1)))
			k = i+1
		i+=1
		
	#print(k)
	code.append(s[-1]+str(s.count(s[-1],k)))
	print("".join(str(w) for w in code))


s = str(input())

#print(len(s))

encodeString(s)

