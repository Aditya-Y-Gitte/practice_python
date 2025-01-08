# Function |	Input	       |     Output	          |  Use Case
# ----------------------------------------------------------------------------------
# load	   | File object (JSON)| Python object	      |  Reading JSON from a file
# dump	   | Python object	   | File object (JSON)	  |  Writing JSON to a file
# loads	   | JSON string	   | Python object	      |  Parsing JSON from a string
# dumps	   | Python object	   | JSON string	      |  Converting to JSON string


import json

name = input("Enter Name: ")
age = input("Enter Age: ")

new_record = {"name": name, "age": age}

# File path
file_path = "data.json"

try:
    # Step 1: Read existing data
    with open(file_path, "r") as file:
        data = json.load(file)

    # Step 2: Append new data
    if isinstance(data, list):  # Ensure the file contains a list
        data.append(new_record)
    else:
        raise ValueError("JSON structure is not a list!")

    # Step 3: Write updated data back to the file
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

    print("Data appended successfully.")

    print( "*" *70)
    print("\n")
   
    for data in data:
        print(f"Name : {data["name"]}, Age: {data["age"]}")

except FileNotFoundError:
    # If the file doesn't exist, create it with the new record
    with open(file_path, "w") as file:
        json.dump([new_record], file, indent=4)
    print("File created with the new record.")

except json.JSONDecodeError:
    print("Error reading JSON file. Ensure it contains valid JSON.")

except ValueError as e:
    print(f"Value error: {e}")
