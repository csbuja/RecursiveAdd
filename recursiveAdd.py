# Given a array 
# {{ 4,7,3,6,7}} 

# construct a triangle like 
# {{81}} 
# {{40,41}} 
# {{21,19,22}} 
# {{11,10,9,13}} 
# {{ 4,7,3,6,7}}

def recursiveAdd_helper(l):
	if len(l) == 1:
		return [l]
	otherL = []	
	i = 0
	while(i<len(l)):
		if i != len(l) -1:
			otherL.append(l[i]+l[i+1])
		i+=1
	return recursiveAdd_helper(otherL)


def recursiveAdd(lol):
	l = lol[0]
	return recursiveAdd_helper(l)

print recursiveAdd([[4,7,3,6,7]])