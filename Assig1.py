# Ques1: Print list in sequential order
num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

for i in num_list:
    print(i)


#Ques2: Print numbers greater than 45 

for i in num_list:
    if(i>45):
        print(i)

#Ques3: Add else statement
for i in num_list:
    if(i<45):
        print('Under 45')
        print(i)
    else:
        print('Over 45')
        print(i)

#Ques4: Use enumerate function and print index

for index, i in enumerate(num_list):
    if(i == 36):
        print('Number found at position', index)

#Ques5: Count varaiable, increment count and break statement
counter = 0
for index, i in enumerate(num_list):
    
    if(i<45):
        print('Under 45')
        print(i)
    else:
        print('Over 45')
        print(i)
        
    if(i == 78):
        print('Number found at position', index)
        break
    counter += 1
print('Counter value is', counter)











