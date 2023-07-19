#if
a,b=20,30
if(a>b):
    print('a is greater')
if(a<b):
    print('b is greater')

n=20
if(n%2==0):
    print('n is a even number')

name = 'navya'
if(name.islower()):
    print('true')

# using if and else
a,b = 100,20
if(a>b):
    print('a is greater')
else:
    print('b is greater')

name = 'navya'
if(name.isdigit()):
    print('true')
else:
    print('false')

if(name.isspace()):
    print('true')
else:
    print('false')

#if and elif

x = 3
if(x%2==0):
    print('x is divisible by 2')
elif(x%3==0):
    print('x is divisible by 3')

room = 'bed'
area = 13.0
if room =='kit':
    print('looking arround in Kitchen')
elif room == 'bed':
    print('looking arround in bedroom')

if area>13:
    print('big place')
elif area<13:
    print('pretty small')
elif area==13:
    print("enough")

name = 'navya'
if name.islower():
    print('"navya" is lowercase')
elif name.upper():
    print('"navya" is uppercase')

# using if, elif, else
a = 20
if a%2==0:
    print(str(a) + ' is a even number')
elif a%2==1:
    print(str(a) + ' is a odd number')
else:
    print(str(a) + ' is neither even nor odd')

room = 'bed'
if room =='kit':
    print('looking arround in Kitchen')
elif room == 'bed':
    print('looking arround in bedroom')
else:
    print('looking arround elsewhere')

price = 50
quantity = 5
amount = price * quantity

if amount > 100:
    if amount > 500:
        print('amount is greater than 500')
    else:
        if amount <=500 and amount>=400:
            print('amount is between 400 and 500')
        elif amount<=400 and amount>=300:
            print('amount is between 300 and 400')
        else:
            print('amount is between 200 and 300')
elif amount==100:
    print("amount is 100")
else:
    print('amount is less than 100')

a,b,c=20,80,70
if a>b and a>c:
    print('a is greatest')
else:
    if b>c:
        print("b is greatest")
    else:
        print('c is greatest')

x = 15
if x>18:
    pass
elif x==18:
    print('eligible to vote')
else:
    print('not eligible to vote')

exam1 = 85
exam2 = 92
exam3 = 78

average_score = (exam1 + exam2 + exam3) / 3

if average_score >= 90:
    grade = "A"
elif average_score >= 80:
    grade = "B"
elif average_score >= 70:
    grade = "C"
elif average_score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Average score: {average_score}")
print(f"Grade: {grade}")



