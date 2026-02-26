class Solution:
    def isPalindrome(self,x):
        if x<0:
           return False
        num=x
        temp=num
        result=0

        while num>0:
            digit=num %10
            result=result*10+digit
            num=num //10

        return result==temp
        