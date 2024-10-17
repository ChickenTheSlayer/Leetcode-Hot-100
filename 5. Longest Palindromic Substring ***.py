class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        def expandFromCenter(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the palindrome substring that was found
            return s[left + 1:right]
        
        longest_palindrome = ""
        
        for i in range(len(s)):
            # Check for odd-length palindrome (center at i)
            odd_palindrome = expandFromCenter(i, i)
            # Check for even-length palindrome (center between i and i+1)
            even_palindrome = expandFromCenter(i, i + 1)
            
            # Update longest palindrome if necessary
            if len(odd_palindrome) > len(longest_palindrome):
                longest_palindrome = odd_palindrome
            if len(even_palindrome) > len(longest_palindrome):
                longest_palindrome = even_palindrome
        
        return longest_palindrome
