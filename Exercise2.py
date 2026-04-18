filename = "notes.txt"

try:
    
    first_note = input("Enter your first note: ") + "\n"
    with open(filename, "w") as file:
        file.write(first_note)

    
    with open(filename, "r") as file:
        content = file.read()
    print("Current content in notes.txt:")
    print(content)

    
    second_note = input("Enter your second note: ") + "\n"
    with open(filename, "a") as file:
        file.write(second_note)

    
    with open(filename, "r") as file:
        updated_content = file.read()
    print("Updated content in notes.txt:")
    print(updated_content)

except FileNotFoundError:
    print("Error: The file was not found.")
except PermissionError:
    print("Error: Permission denied.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
