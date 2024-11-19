n = int(input("Enter your number here"))
s = n
sum = 0
length = len(str(n))
while n > 0:
    digit=n%10
    sum = sum*10 + digit
    n=n//10
    print(sum)
if sum == s:

    print("Number is a palindrome")

else:

    print("Number is not a palindrome")