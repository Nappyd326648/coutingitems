import re
import string

itemlist=[]
one=[]
two=[]
i = 0
f= open ("items.txt","r")
c = 0
q = 0
for x in f:
        itemlist.append(f.readline())
total =(len(itemlist))
print (total)
t = total
itemlist.sort()
print (itemlist)
one.extend(itemlist)

for x in one:
        two.append(one.count(x))

for x in itemlist:
        itemlist = one[c]
        c++
print (itemlist)
#while c < t:
#        for x in itemlist:
#                if one[c] == x:
#                        del one[q]
#                q=q+1
#        c=c+1
#        t=(len(one))
#print (one)

#while i < total:
#	for x in itemlist:
#		if one[i]==itemlist[x]:
#			two[i] == two[i] + 1
#print (two)


def printsomething():
        print ("no")
	
def PrintMe(v):
    print("You sent me: " + v)
    return 100;

def SquareValue(v):
    return v * v
	
def singleitem():
	itemlist
	one
	two
	i = 0
	f=open ("items.txt","r")
	for x in f:
		itemlist.append(f.readline())
	total =(len(itemlist))
	
	for x in itemlist:
		one.append(itemlist[x])
	print (one)

	while c < total:
		for x in itemlist:
			if one[c] == itemlist[x]:
				one.pop(x)
	print (one)

	while i < total:
		for x in itemlist:
			if one[i]==itemlist[x]:
				two[i] == two[i] + 1
	print (two)
