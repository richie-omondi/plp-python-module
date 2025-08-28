# File Read and Write with Exception Handling

filename = input("Enter the filename to read: ")

try:
    with open(filename, 'r') as infile:
        content = infile.read()
        # Example modification: convert content to uppercase
        modified_content = content.upper()
except FileNotFoundError:
    print("Error: The file does not exist.")
except IOError:
    print("Error: The file could not be read.")
else:
    new_filename = "modified_" + filename
    try:
        with open(new_filename, 'w') as outfile:
            outfile.write(modified_content)
        print(f"Modified content written to {new_filename}")
    except IOError:
        print("Error: Could not write to the new file.")

# Error Handling

filename = input("Enter the filename to read: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("Error: The file does not exist.")
except IOError:
    print("Error: The file could not be read.")


