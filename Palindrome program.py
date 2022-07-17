text_check = 'mum'  
strstr = text_check.casefold()  
  
 
rev = reversed(text_check)  
  
if list(text_check) == list(rev):  
   print("The string is a Palindrome")  
else:  
   print("The string is not a Palindrome")  