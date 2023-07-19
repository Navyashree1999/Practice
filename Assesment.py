'''Python program to find the area of a triangle whose sides are given

Python program to check whether the given integer is a multiple of 5

Python program to find the sum of the digits of an integer using a while loop

Python program to check whether the given integer is a prime number or not

Python program to check whether a string is palindrome or not'''

#Python program to find the area of a triangle whose sides are given

def area_tri():
    base = int(input('enter base of triangle :'))
    height = int(input('enter height of triangle : '))

    area = 1/2*base*height
    print('Area of triangle :' , area)
#area_tri()
print('\n')

#Python program to check whether the given integer is a multiple of 5

def mult_five():
    num = int(input("enter number :"))
    if num % 5==0:
        print('%s is a multiple of 5'%str(num))
    else:
        print('%s is not a multiple of 5' % str(num))
#mult_five()
print('\n')

#Python program to check whether a string is palindrome or not

def palindrome():
    my_string1 = input("enter string:")
    new_string = my_string1.lower()
    my_string2 = new_string[::-1]
    if new_string == my_string2:
        print('%s is a palindrome'%str(my_string1))
    else:
        print('%s is not a palindrome'%str(my_string1))
palindrome()

# Python program to check whether the given integer is a prime number or not

def prime_num():
    num = int(input("enter number:"))
    if num == 1:
        print("It is not a prime number")
    elif num>1:
        for i in range(2, num):
            if num%i==0:
                print("It is not a prime number")
                break
        else:
            print('It is a prime number')

prime_num()

#Python program to find the sum of the digits of an integer using a while loop

def sum_num():
    num = int(input('enter integer'))
    i = num[0]
    index = len(num)
    while i < index:
        sum ==0
        sum+=i
        i+=1
    print('sum of %s'%str(sum))
sum_num()








