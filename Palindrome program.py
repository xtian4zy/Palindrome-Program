text_check = 'mum'  #The string you want to test
strstr = text_check.casefold()  #returns the string with all the characters in lower case.
  
 
rev = reversed(text_check)  # Reversing the string. 
  
if list(text_check) == list(rev):  #Making the decision whether string is palindrome or not.
   print("The string is a Palindrome")  
else:  
   print("The string is not a Palindrome")  