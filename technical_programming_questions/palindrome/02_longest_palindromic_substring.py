# Given a string s, return the longest palindromic substring in s.

#**********************************************************************************************************#

# Function to check if a substring s[low..high] is a palindrome
def check_pal(s, low, high):
    while low < high:
        if s[low] != s[high]:
            return False
        low += 1
        high -= 1
    return True

# This function prints the longest palindrome substring
# It also returns the length of the longest palindrome
def longest_pal_substr(s:str)->str:
    n = len(s)

    # All substrings of length 1 are palindromes
    max_len = 1
    start = 0

    # Nested loop to mark start and end index
    for i in range(n):
        for j in range(i, n):
          
            # Check if the current substring is 
            # a palindrome
            if check_pal(s, i, j) and (j - i + 1) > max_len:
                start = i
                max_len = j - i + 1

    return s[start:start + max_len]

# Time: O(n^3) – Quadratic
# Space: O(1) – constant

#**********************************************************************************************************#

class Solution:
    def __init__(self):
        # Initialize the dp table with -1 (for memoization)
        self.dp = [[-1] * 1001 for _ in range(1001)]
    
    def isPalindrome(self, s: str, low: int, high: int) -> bool:
        while low < high:
            # Check if the result is already computed (memoization)
            if self.dp[low][high] != -1:
                return self.dp[low][high]
            
            # If characters don't match, it's not a palindrome
            if s[low] != s[high]:
                self.dp[low][high] = 0
                return False
            low += 1
            high -= 1
        
        self.dp[low][high] = 1
        return True
    
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        maxLen = 0
        sp = 0
        
        # Check every substring using two pointers
        for i in range(n):
            for j in range(i, n):
                if self.isPalindrome(s, i, j):
                    # Update max length and starting position
                    if j - i + 1 > maxLen:
                        maxLen = j - i + 1
                        sp = i
                        
        return s[sp:sp + maxLen]

# Time: O(n²) – Quadratic
# Space: O(n²) - Quadratic : dp_table

#**********************************************************************************************************#

def longestPalindrome(self, s: str) -> str:
        s_len = len(s)
        sp = 0
        max_len = 1
        
        for i in range(s_len):
            # for odd len str
            low, high = i,i
            while low>=0 and high<s_len and (s[low]==s[high]):
                if (high-low+1)>max_len :
                    max_len = high-low+1
                    sp = low
                low-=1
                high+=1
            
            # for even len str
            low, high = i,i+1
            while low>=0 and high<s_len and (s[low]==s[high]):
                if (high-low+1)>max_len :
                    max_len = high-low+1
                    sp = low
                low-=1
                high+=1
        
        return s[sp:sp+max_len]

# Time: O(n²) – Quadratic
# Space: O(1) - Constant