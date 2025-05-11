'''
Task: 01
'''

filename = "Sample.txt"

try:
    with open(filename, 'r') as file:
        print("Reading file content:\n")
        for line_number, line in enumerate(file, start=1):
            print(f"Line {line_number}: {line.strip()}")
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")

'''
Task: 02
'''

filename = "output.txt"
text_to_write = input("Enter text to write to the file: ")
try:
    with open(filename, 'w') as file:
        file.write(text_to_write + "\n")
    print(f"Data successfully written to {filename}.")
except Exception as e:
    print("An error occurred while writing:", e)

text_to_append = input("\nEnter additional text to append: ")
try:
    with open(filename, 'a') as file:
        file.write(text_to_append + "\n")
    print("Data successfully appended.")
except Exception as e:
    print("An error occurred while appending:", e)

print("\nFinal content of output.txt:")
try:
    with open(filename, 'r') as file:
        content = file.read()
        print(content)
except Exception as e:
    print("An error occurred while reading:", e)


##########################################################################################################################

###########

##########################################################################################################################

'''
Task: 01
'''

filename = "Sample.txt"                                                      # Enter the filename to read.

try:
    with open(filename, 'r') as file:                                        # File opening.
        print("Reading file content:\n")                                     # Displays the file content.
        for line_number, line in enumerate(file, start=1):                   # Displays the line number.
            print(f"Line {line_number}: {line.strip()}")                     # Prints each line number.
except FileNotFoundError:                                                    # Handle the error "FileNotFoundError"
    print(f"Error: The file '{filename}' was not found.")                    # Hits this message if file is not found.

'''
Task: 02
'''

filename = "output.txt"                                                      # Enter the filename to write.
text_to_write = input("Enter text to write to the file: ")                   # Enter the information to store in the file.
try:
    with open(filename, 'w') as file:                                        # Writes the content into the file.
        file.write(text_to_write + "\n")
    print(f"Data successfully written to {filename}.")                       # Shows the message that the data is successfully written.
except Exception as e:
    print("An error occurred while writing:", e)

text_to_append = input("\nEnter additional text to append: ")                # Enter the information to append.
try:
    with open(filename, 'a') as file:                                        # Appends the content into the file.
        file.write(text_to_append + "\n")
    print("Data successfully appended.")
except Exception as e:
    print("An error occurred while appending:", e)

print("\nFinal content of output.txt:")
try:
    with open(filename, 'r') as file:
        content = file.read()
        print(content)
except Exception as e:
    print("An error occurred while reading:", e)

