# Given a string s, return the number of palindromic substrings in it.
# A string is a palindrome when it reads the same backward as forward.
# A substring is a contiguous sequence of characters within the string.

def count_palindromic_substings(s:str) -> int:
    cnt =0

    for i in range(len(s)):
        # for odd len substr
        l,r = i,i
        while l>=0 and r<len(s) and s[l]==s[r]:
            cnt+=1;
            l-=1
            r+=1

        #  for even substr
        l,r = i,i+1
        while l>=0 and r<len(s) and s[l]==s[r]:
            cnt+=1;
            l-=1
            r+=1

    return cnt

