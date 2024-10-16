def is_harshad_number(n):
    # Convert the number to string to iterate over its digits
    digits = [int(digit) for digit in str(n)]
    # Calculate the sum of the digits
    digit_sum = sum(digits)
    # Check if the number is divisible by the sum of its digits
    return n % digit_sum == 0

# Example usage
number = int(input("Enter a number: "))
if is_harshad_number(number):
    print(f"{number} is a Harshad number.")
else:
    print(f"{number} is not a Harshad number.")
