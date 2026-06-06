# 01_error_handling_practice.py
# ============================================================
# Python Error Handling Practice
# Goal: Read, recognize, and catch common exceptions.
# ============================================================


# ------------------------------------------------------------
# Example 1: Division by zero
# ------------------------------------------------------------
try:
    print("Example 1: Division")
    answer = 10 / 0
    print("Result:", answer)
except ZeroDivisionError:
    # TODO: Catch the specific error here and explain the problem to the student.
    pass


# ------------------------------------------------------------
# Example 2: Type mismatch
# ------------------------------------------------------------
try:
    print("\nExample 2: Type mismatch")
    message = "Age: " + 12
    print(message)
except TypeError:
    # TODO: Catch the specific error here and explain why the types do not match.
    pass


# ------------------------------------------------------------
# Example 3: Indexing an empty list
# ------------------------------------------------------------
try:
    print("\nExample 3: Empty list access")
    numbers = []
    first_item = numbers[0]
    print(first_item)
except IndexError:
    # TODO: Catch the specific error here and explain that the list has no items.
    pass


# ------------------------------------------------------------
# Example 4: Try / except / finally
# ------------------------------------------------------------
try:
    print("\nExample 4: try / except / finally")
    value = int("not-a-number")
    print("Converted value:", value)
except ValueError:
    # TODO: Catch the specific error here and tell the user the input was invalid.
    pass
finally:
    # TODO: Add a message here that always runs, no matter what happened above.
    pass


# ------------------------------------------------------------
# Bonus challenge for students
# ------------------------------------------------------------
try:
    print("\nBonus challenge")
    with open("missing_file.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    # TODO: Catch the specific error here and explain that the file was not found.
    pass

