# Exercise 1: File to List Converter

filename = input("Enter filename: ")

try:
    with open(filename, "r") as file:
        lines = file.readlines()

    cleaned_lines = [line.strip() for line in lines]
    print("Resulting list:", cleaned_lines)

except FileNotFoundError:
    print("Error: File does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")