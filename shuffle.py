from random import *
from sys import *
print "\n\n\t\t\t****************************************************************\n\t\t\t\t\t\tSF-7 SHUFFLE LIST\n\t\t\t****************************************************************"
print "\n\n\t\t\tINSTRUCTIONS\n\n\t\t\t\t[1] Enter your ID number to know your seating position.\n\n\t\t\t\t[2] You can see total shuffle list of SF-7\n\n\t\t\t\t[3] To exit instead of ID No. enter 'done'\n\n"
n1=dict()#for girls
f=dict()
n2=dict()#for boys
qw=dict()
#--------Girls-----------
gids = open('girls_ids')
b=gids.read().split('\n')
del b[-1]
b_dup=[]
for i in range(len(b)):
	b_dup.append(b[i])
shuffle(b)#shuffling girls ID's
#--------------------------------------------
a=open('girls_pos')#GIRLS SEATING POSITIONS
c=a.read()
a.close()
s=c.split()
a1=open('girls_names')#GIRLS NAMES
c1=a1.read()
a1.close()
s1=c1.split()
#---------------Assigning girls names to ID's-----------------
for i in range(len(b_dup)):
	for j in range(len(s1)):
		if i==j:
			n1[b_dup[i]]=s1[j]
#-----------Boys----------------
bids = open('boys_ids')
o=bids.read().split('\n')
del o[-1]
o_dup=[]
for i in range(len(o)):
	o_dup.append(o[i])
shuffle(o)#shuffling boys ID's
h=open('boys_pos')#BOYS SEATING POSITIONS
j=h.read()
h.close()
k=j.split()
h1=open('boys_names')#BOYS NAMES
j1=h1.read()
h1.close()
k1=j1.split()
#---------Assigning boys names to ID's--------------------------
for i in range(len(o_dup)):
	for j in range(len(k1)):
		if i==j:
			n2[o_dup[i]]=k1[j]
#-----------Assigning girls positions to ID's-----------------
for i in range(len(b)):
	for j in range(len(s)):
		if i==j:
			f[b[i]]=s[j]
#---------------------------------Assigning boys positions to ID's----------------
for i in range(len(k)):
	for j in range(len(o)):
		if i==j:
			qw[o[i]]=k[j]

#------------------------------------------------------
for i in range(60):
	ID=raw_input('\n\nEnter your ID(Ex: 0977) :-')
	if (ID=='done' or ID=='DONE'):
		print "\nThank You!!!\n\n"
		break
	else:
		n=int(ID)
		for i in f:
			if int(i[3:])==n:
				print "\n",n1[i],'your place is',f[i],"\n\n"
		for j in qw:
			if int(j[3:])==n:
				print "\n",n2[j],'your place is ',qw[j],"\n\n"
print "Do you wanna see total shuffle list???\n\n"
cho=raw_input("Enter y/n ::: ")
if (cho=='n' or cho=='N'):
	print "\nThank You..!!!\n"
else:
	print "\t\t\t\tS.No\t ID\t\t\tNAME\t\t\tPOSITION\n\n\t\t\t-----------------------------------------------------------------------------\n"
	s=1
	for i in range(len(f)):
		print "\t\t\t\t",s,"\t",str(b_dup[i]),"\t\t",n1[b_dup[i]],"\t\t",f[b_dup[i]],"\n"
		s+=1
	for i in range(len(qw)):
		print "\t\t\t\t",s,"\t",str(o_dup[i]),"\t\t",n2[o_dup[i]],"\t\t\t",qw[o_dup[i]],"\n"
		s+=1	
	
