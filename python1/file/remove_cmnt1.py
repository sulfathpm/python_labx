# Initialize the file variable
f = False

try:
    # Open the file in read and write mode
    f = open('b.txt', 'r+')

    # Read all lines from the file
    lines = f.readlines()

    # Create a new list excluding lines that start with '#'
    clines = [x for x in lines if not x.strip().startswith('#')]

    # Clear the entire content of the file
    f.truncate(0)

    # Move the file pointer to the beginning
    f.seek(0)

    # Write the non-comment lines back to the file
    f.writelines(clines)

    # Success message
    print("Removed the comments")

except Exception as e:
    # Print any error that occurs
    print(e)

finally:
    # Close the file if it was opened
    if f:
        f.close()
