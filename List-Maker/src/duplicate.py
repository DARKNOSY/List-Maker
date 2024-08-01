import json
from collections import OrderedDict

def remove_duplicates(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        unique_lines = list(OrderedDict.fromkeys(lines))
        
        with open(file_path, 'w') as file:
            file.writelines(unique_lines)
        
        print("Duplicates removed successfully.")
    except FileNotFoundError:
        print("File not found.")

def main():
    try:
        with open("src/config.json", "r") as f:
            config = json.load(f)
    except FileNotFoundError:
        print("Config file not found.")
        return
    
    output_name = config["output_name"]
    if config.get("delete_duplicates"):
        remove_duplicates(f"output/{output_name}.txt")
    else:
        print("Duplicates removal option is not enabled.")

if __name__ == "__main__":
    main()
