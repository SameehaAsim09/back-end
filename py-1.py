print(type('hello'))
example_list=[1, 'hello',4.5]
print(type(example_list))

name='sam'
print(len(name[2]))

num1 = input('enter no: ')
num2 = input('enter no: ')
a=int(num1)+int(num2)
print(a)

bill_total = 1200
discount1 = 50
discount2 = 100
if bill_total > 1000 and bill_total < 2000:
    print('You will have some discount')
    bill_total = bill_total - discount1
elif bill_total > 2000 :
    bill_total = bill_total - discount2
    print(' Enjoy 100 off')

else:
    print('No discount')

print('Total Bill ' + str(bill_total))


value = input('enter http_status code: ')
int_value = int(value)
match int_value:
    case 200 | 201:
        print('Success')
    case 400:
        print('Bad Request')
    case 502 | 503:
        print('Bad Gateway')
    case 600:
        print('Server Error')
    case _:
        print('Not Found')

for i in ['butter', 'caramel', 'coffee']:
    print(i)



