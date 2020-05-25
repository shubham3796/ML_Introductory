largest = None
smallest = None
list = []

while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try:
        number = int(num)
    except:
        print("Invalid input")
        continue
    list.append(number)   
    print(list) 
       
    
for n in list:
    if largest is None:
        largest = n
    elif largest < n:
        largest = n
    if smallest is None:
        smallest = n
    elif smallest > n:
        smallest = n
        

print("Maximum is", largest)
print("Minimum is", smallest)

# https://www.coursera.org/learn/python-data/home/welcome
# https://www.coursera.org/programs/capgemini-learning-program-71mtd?authProvider=capgemini