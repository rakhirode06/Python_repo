def str_to_int(s):
    # Handle negative numbers
    is_negative = False
    if s[0] == '-':
        is_negative = True
        s = s[1:]  # Remove the negative sign for processing
    
    result = 0
    # Convert string to integer by processing each character
    for char in s:
        # Manually convert each character to its integer value
        digit = ord(char) - ord('0')  # '0' is 48 in ASCII, so '9' is 57
        result = result * 10 + digit  # Shift left by 10 (like in base 10)
    
    return -result if is_negative else result

def decimal_subtraction(a_str, b_str):
    # Convert the string inputs to integers
    a_int = str_to_int(a_str)
    b_int = str_to_int(b_str)
    
    # Perform subtraction
    return a_int - b_int

# Example usage
a = "200"  # First number
b = "73"   # Second number

result = decimal_subtraction(a, b)
print(f"Result of {a} - {b} is: {result}")

