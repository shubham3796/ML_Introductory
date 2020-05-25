print("Hare Krishna!","Prabhu!")
print(int(98.6))
fileName = input("Enter File name   ") #"practice_text_file.txt"
file_handler = open(fileName,'r')

for line in file_handler:
	for letter in line:
		print(letter)
		
for i in range(7):
	if i<2:
		print(i)
		#continue : Quit this iteration and move to the next iteration
	elif i<4:
		print(i,"...")
	elif i<6:
		print(i,"++++")
		#break : brings out of loop
	else:
		print(i,"-----")
		#quit() : same as exit() of C

for i in [15, 14, 13, 12, 11]:
	print(i)

sakhis = ['Lalita', 'Vishakha', "Champaklata", "Tungavidya", "Citra"]
for sakhi in sakhis:
	print(sakhi)
	
#Good technique to find the largest and the smallest in an array
smallest = None # A flag value which is None oly for the first time it is checked.
for num in [41, 3, 2, 45, 21, 11]:
	if smallest is None: 
		smallest = numeric_type
	elif num < smallest:
		smallest = num
	
# A function
def printSomething(str):
	print(str)
	return 1
	
val = printSomething("Jai Prabhupad!")
print(val)