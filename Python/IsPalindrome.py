'''
This Programs checks if a String is a valindrome or not 
A Palindrome is word /Phrase which reads same when read both ways
'''
def isPalindrome(self, s: str) -> bool:
    start=0
    end=len(s)-1
    while start<end:
        while start<end and  not s[start].isalnum():
            start+=1
        while start<end  and not s[end].isalnum():
            end-=1
        if s[start].lower()!= s[end].lower():
            return False
        start+=1
        end-=1
    return True

# s= "IS IT PALINDROME" False
s= "M, A: D AM" #True
