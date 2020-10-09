def isPalindrome(s):
    """Return whether string s is a palindrome"""
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and isPalindrome(s[1:-1])


s = input("Enter your string:")
print(isPalindrome(s))
