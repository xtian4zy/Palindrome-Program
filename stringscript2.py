string=input(("Enter a letter:"))  # collect input from user
if(string==string[::-1]):  #reverse string and check if same with original
      print("The string entered is a palindrome")  
else:  
      print("The string entered is not a palindrome")  