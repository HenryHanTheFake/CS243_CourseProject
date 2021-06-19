import random

preference1 = "1 2 3 4\n"
preference2 = "4 3 2 1\n"
preference3 = "2 1 4 3\n"
preference4 = "3 4 1 2\n"
address1 = "preference\preference2.txt"
address2 = "connection\connection2.txt"

'''
file = open(address1,"a")
for i in range(0,200):
	if i < 90:
		file.write(preference1)
	elif i >= 90 and i < 180:
		file.write(preference2)
	elif i >= 180 and i < 190:
		file.write(preference3)
	elif i >= 190 and i < 200:
		file.write(preference4)
	
		
file.close()
'''
_seed = "seed"

file = open(address2,"w")
for i in range(0,200):
	if  i == 0:
		x = ""
		r = random.randint(20,40)
		for j in range(0,r):
			n = random.randint(0,89)
			x = x + str(n)
			x = x + " "
		
		r = random.randint(5,10)
		for j in range(0,r):
			n = random.randint(90,179)
			x = x + str(n)
			x = x + " "
			
		r = random.randint(0,5)
		for j in range(0,r):
			n = random.randint(180,189)
			x = x + str(n)
			x = x + " "
			
		r = random.randint(1,5)
		for j in range(0,r):
			n = random.randint(190,199)
			x = x + str(n)
			if j != r-1:
				x = x + " "
				
		x = x + "\n"
		file.write(x)
		
	elif i < 90:
		x = ""
		r = random.randint(20,40)
		for j in range(0,r):
			n = random.randint(0,89)
			x = x + str(n)
			x = x + " "
		
		r = random.randint(5,10)
		for j in range(0,r):
			n = random.randint(90,179)
			x = x + str(n)
			x = x + " "
			
		r = random.randint(0,5)
		for j in range(0,r):
			n = random.randint(180,189)
			x = x + str(n)
			x = x + " "
			
		r = random.randint(1,5)
		for j in range(0,r):
			n = random.randint(190,199)
			x = x + str(n)
			if j != r-1:
				x = x + " "
				
		x = x + "\n"
		file.write(x)
		
	elif i < 180:
		x = ""
		r = random.randint(5,10)
		for j in range(0,r):
			n = random.randint(0,89)
			x = x + str(n)
			x = x + " "
		
		r = random.randint(20,40)
		for j in range(0,r):
			n = random.randint(90,179)
			x = x + str(n)
			x = x + " "
			
		r = random.randint(0,5)
		for j in range(0,r):
			n = random.randint(180,189)
			x = x + str(n)
			x = x + " "
			
		r = random.randint(1,5)
		for j in range(0,r):
			n = random.randint(190,199)
			x = x + str(n)
			if j != r-1:
				x = x + " "
				
		x = x + "\n"
		file.write(x)
		
	elif i < 190:
		x = ""
		r = random.randint(5,10)
		for j in range(0,r):
			n = random.randint(0,89)
			x = x + str(n)
			x = x + " "
		
		r = random.randint(5,10)
		for j in range(0,r):
			n = random.randint(90,179)
			x = x + str(n)
			x = x + " "
			
		r = random.randint(5,10)
		for j in range(0,r):
			n = random.randint(180,189)
			x = x + str(n)
			x = x + " "
			
		r = random.randint(5,10)
		for j in range(1,r):
			n = random.randint(190,199)
			x = x + str(n)
			if j != r-1:
				x = x + " "
				
		x = x + "\n"
		file.write(x)
		
	elif i < 200:
		x = ""
		r = random.randint(5,10)
		for j in range(0,r):
			n = random.randint(0,89)
			x = x + str(n)
			x = x + " "
		
		r = random.randint(5,10)
		for j in range(0,r):
			n = random.randint(90,179)
			x = x + str(n)
			x = x + " "
			
		r = random.randint(5,10)
		for j in range(0,r):
			n = random.randint(180,189)
			x = x + str(n)
			x = x + " "
			
		r = random.randint(5,10)
		for j in range(1,r):
			n = random.randint(190,199)
			x = x + str(n)
			if j != r-1:
				x = x + " "
				
		x = x + "\n"
		file.write(x)
file.close()