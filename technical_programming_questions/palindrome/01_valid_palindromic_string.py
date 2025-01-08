# Write a function to determine if a string is a valid palindrome, ignoring non-alphanumeric characters.

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

def is_valid_palindrome(s: str) -> bool:
    """
    Determine if a given string is a valid palindrome, ignoring non-alphanumeric characters.

    :param s: Input string
    :return: True if the string is a palindrome, False otherwise
    """
    # Filter the string to include only alphanumeric characters and convert to lowercase
    filtered = ''.join(char.lower() for char in s if char.isalnum())
    # Check if the filtered string is equal to its reverse
    return filtered == filtered[::-1]

# Example usage
print(is_valid_palindrome("A man, a plan, a canal: Panama"))  # Output: True
print(is_valid_palindrome("race a car"))  # Output: False
