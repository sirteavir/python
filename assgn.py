# function which return reverse of a string

def isPalindrome(s):
    return s == s[::-1]
name=int(input("Enter name:"))

# Driver code
s = "malayalam"
ans = isPalindrome(s)

if ans:
    print("Yes")
else:
    print("No")
isPalindrome(s)