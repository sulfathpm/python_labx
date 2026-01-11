# Initialize file variable as False
# This helps to check later whether the file was opened successfully
f = False

try:
    # Open the file 'a.txt' in read and write mode
    f = open('a.txt', 'r+')

    # Read all lines from the file and store them in a list
    lines = f.readlines()

    # Ask the user to enter the line number to remove
    n = int(input("Enter the number of line to remove : "))

    # Check whether the entered line number is invalid
    # Line number must be between 1 and total number of lines
    if n < 1 or n > len(lines):
        print("Invalid line number")
    else:
        # Remove the specified line
        # (n-1 because list index starts from 0)
        lines.pop(n - 1)

        # Clear the entire content of the file
        f.truncate(0)

        # Move the file pointer back to the beginning
        f.seek(0)

        # Write the updated list of lines back to the file
        f.writelines(lines)

        # Confirmation message
        print("Line removed successfully")

except Exception as e:
    # Display any error that occurs during execution
    print(e)

finally:
    # Close the file if it was opened
    if f:
        f.close()
