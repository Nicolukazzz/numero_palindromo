class Solution(object):
    def isPalindrome(self, x):
        xs= str(x)
        xr= xs[::-1]
        if xs==xr:
            return True
        else:
            return False 

        
        """
        :type x: int
        :rtype: bool
        """
        
