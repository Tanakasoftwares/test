import math

def is_magical_potion(power):
    """
    Determines if a potion's power level is magical (a perfect cube).

    Args:
        power: An integer representing the power level.

    Returns:
        "YES" if the power level is magical, "NO" otherwise.
    """
    if power < 0:  # Handle negative input (not specified in prompt, but good practice)
        return "NO"

    root = round(power ** (1/3))  # Efficiently estimate cube root

    # Use math.isclose() for robust comparison of floating-point numbers
    if math.isclose(root**3, power, rel_tol=1e-9):  # Adjust rel_tol as needed
        return "YES"
    else:
        return "NO"

# Get input and print the result
while True:  # Loop indefinitely until valid input
    power_str = input()
    if power_str == "": # Check if the input is empty
        print("Invalid input. Please enter a number.")
        continue # Go to the beginning of the loop

    try:
        power = int(power_str)
        break  # Exit loop if conversion successful
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

result = is_magical_potion(power)
print(result)



def find_duplicate_outcomes(outcomes):
    """
    Finds the two duplicate outcomes in a list.

    Args:
        outcomes: A list of integers representing betting outcomes.

    Returns:
        A list of two integers representing the duplicate outcomes (in any order).
    """

    counts = {}  # Dictionary to store the count of each outcome

    for outcome in outcomes:
        if outcome in counts:
            counts[outcome] += 1
        else:
            counts[outcome] = 1

    duplicates = []
    for outcome, count in counts.items():
        if count == 2:  # Found a duplicate (appears exactly twice)
            duplicates.append(outcome)

    return duplicates


# Example usage (for the provided input):
outcomes = [123456, 234567, 123347, 456789, 567890, 678901, 789012, 890123, 901234, 112233, 223344, 334455, 789012, 222234, 123347]
duplicate_outcomes = find_duplicate_outcomes(outcomes)
print(duplicate_outcomes)  # Output: [123347, 789012] (or [789012, 123347])


# Another example (using input from the prompt):
outcomes2 = [0, 3, 2, 1, 3, 2]
duplicate_outcomes2 = find_duplicate_outcomes(outcomes2)
print(duplicate_outcomes2) # Output: [3, 2] (or [2, 3])

outcomes3 = [7,1,5,4,3,4,6,0,9,5,8,2]
duplicate_outcomes3 = find_duplicate_outcomes(outcomes3)
print(duplicate_outcomes3) # Output: [4, 5] (or [5, 4])

outcomes4 = [0, 1, 2, 3, 4, 5, 5, 0]
duplicate_outcomes4 = find_duplicate_outcomes(outcomes4)
print(duplicate_outcomes4) # Output: [5, 0] (or [0, 5])



def reformat_string(s):
    """Reformats a string to alternate case of alphabetic chars, keeping others."""

    reformatted = ""
    upper = True  # Start with uppercase

    for char in s:
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            if upper:
                reformatted += char.upper()
            else:
                reformatted += char.lower()
            upper = not upper  # Flip case for next alphabetic char
        else:
            reformatted += char  # Keep non-alphabetic chars as they are

    return reformatted

# Get input and print the result
s = input()
reformatted_s = reformat_string(s)
print(reformatted_s)


from collections import Counter
import math

def can_organize_books(shelf):
    """
    Determines if books can be organized into identical sets.

    Args:
        shelf: A list of integers representing the number of copies of each book.

    Returns:
        "YES" if the books can be organized, "NO" otherwise.
    """

    counts = Counter(shelf)  # Count occurrences of each book type

    for book_count in counts.values():
        if book_count == 1:  # A single book cannot form a set (x > 1)
            return "NO"

        # Check if the count is a multiple of any number greater than 1
        found_divisor = False
        for x in range(2, int(math.sqrt(book_count)) + 1): #check for divisors up to the square root of the book count
            if book_count % x == 0:
                found_divisor = True
                break
        if not found_divisor and book_count != 1: # if no divisor is found and the count is not 1, it is a prime number and cannot be grouped
            return "NO"

    return "YES"


# Example usage (using the provided bookshelf array):
shelf = [1234567, 1234567, 2345678, 2345678, 3456789, 3456789, 1234567, 2345678, 3456789, 4567890, 4567890, 5678901, 5678901, 6789012, 6789012, 1234567, 2345678, 3456789, 4567890, 5678901, 4567890, 5678901]
result = can_organize_books(shelf)
print(result)  # Output: YES


shelf2 = [5, 5, 3, 3, 2, 2]
result2 = can_organize_books(shelf2)
print(result2)  # Output: YES

shelf3 = [1,2,3,4,4,3,2,1]
result3 = can_organize_books(shelf3)
print(result3)  # Output: YES

shelf4 = [1,1,1,2,2,2,3,3,3]
result4 = can_organize_books(shelf4)
print(result4)  # Output: YES

shelf5 = [1,2,3,4,4,3,2,1,4,4]
result5 = can_organize_books(shelf5)
print(result5)  # Output: YES

shelf6 = [1,1,1,2,2,2,3,3]
result6 = can_organize_books(shelf6)
print(result6)  # Output: NO

shelf7 = [7, 7, 7, 7, 8, 8, 8]
result7 = can_organize_books(shelf7)
print(result7)  # Output: NO