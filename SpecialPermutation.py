def permutation():
	t = int(input())
	final = []
	while(t > 0):
		n = int(input())
		l = [None] * n
		
		for i in range(1,n+1):
			l[i-1] = i
		
		# shifting the elements one space to the right
		l=l[-1:]+l[:-1]  
		final.append(l)
		t -= 1

	for i in range(len(final)):
	 	print(*final[i])

permutation()