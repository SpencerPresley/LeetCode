def isPalindrome(s: str) -> bool:
    s = s.lower()
    s = ''.join(char for char in s if char.isalnum())
    return s == s[::-1]

# Runtime: 32ms (Beats 98.06%) | Memory: 17.72mb (Beats 30.34%)
"""
Explanation:

Convert string to lowercase
Iterate through string and only keep characters that are letters or numbers
Return value of the comparison of the string with the reversed string
"""

