#Challenge1

numbers= input('enter the numbers:')

def sum(numbers):
    sum=0
    for i in numbers:
        sum += i
        
    return sum

print sum(numbers)

numbers= input('enter the numbers:')

def multiply(numbers):
    multiply= 1
    for i in numbers:
        multiply *= i
        
    return multiply

print multiply(numbers)
    

numbers= input('enter the numbers:')

def largest(numbers):
    return max(numbers)
print max(numbers)



numbers= input('enter the numbers:')

def minimum(numbers):
    return min(numbers)
print minimum(numbers)


numbers= input('enter the numbers:')
def sets(numbers):
    return set(numbers)
print sets (numbers)



def all_function(numbers):
    
      print sum(numbers)
    
      print max(numbers)
      print min(numbers)
      print sets(numbers)
      print multiply(numbers)
    
    
    
    
    
#Challenge 2
def combo(numbers):
    b_5,b_1,g = numbers
    if g%b_5 > b_1:
        return False
    if (b_5*5)+b_1 >= g:
        return True
    else:
        return False

while True:
    inp= raw_input("enter the possible elements number: ")
    if not inp:
        break
    inp = map(int,inp.split(","))
    print combo(inp)
    
  
#Method- 2   
    
    
inp= [int(a) for a in input("enter: ")]
if inp[2]//5 <= inp[1] and inp[2]%5 <= inp[0]:
    print("true")

else:
    print("false")    


    
    
#Challenge 3

def pattern(n):
    for i in range(1,n):
        print '* '*i
    # for i in range(1,n+1):
    #     print ('* '*(n+1-i))
    for i in range(n,0,-1):
         print '* '*i
     
pattern(9)




#Challenge 4

user_input= input("Enter (,) separated numbers: " )
my_dict = dict(zip(["a","b","c"],user_input))

def no_teen_sum(user_dict):
    nums = user_dict.values()
    return sum(fix_teen(n) for n in nums)

def fix_teen(n):
    if 13 <= n <= 19 and n not in (15, 16):
        return 0
    else: 
        return n

print no_teen_sum(my_dict)