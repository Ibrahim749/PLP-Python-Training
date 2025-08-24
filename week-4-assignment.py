def read_and_modify_file():
    try:
        # Ask user for input file name
        input_file = input("Enter the name of the file to read: ")

        # Try to open and read the file
        with open(input_file, "r") as file:
            content = file.read()

        # Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()

        # Write to a new file
        output_file = "modified_" + input_file
        with open(output_file, "w") as file:
            file.write(modified_content)

        print(f"Modified content written to '{output_file}'.")

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: You don't have permission to read this file.")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        print("Program execution complete.")

# Run the function
read_and_modify_file()
