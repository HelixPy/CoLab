def findPalindrome(search):
    return search == search[::-1]
 
print ("Hey there type-in a string and i will show tell you if its a palindrome or not")
search = str(input("please enter a string: "))

msg = findPalindrome(search)
 
if msg:
    print(f"your entry '{search}' is a palidrome")
else:
    print(f"your entry '{search}' is not a palidrome")