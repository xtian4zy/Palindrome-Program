#Program to check if a number is palindrome using While loop.
num = 404 
temp_num = num  
rev = 0  
while(num > 0):  
    dig = num % 10  
    revrev = rev * 10 + dig  
    numnum = num // 10  
if(temp_num == rev):  
    print("This value is a palindrome number!")  
else:  
    print("This value is not a palindrome number!")  