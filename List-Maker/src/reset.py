import json
import os

def reset():
    default_config = {
        "delete_lines": False,
        "delete_duplicates": False,
        "separate_files": False,
        "reset_config": False,
        "delimiter_before": "\n",
        "delimiter_after": "\n",
        "input_files": [],
        "output_name": "output"
    }

    with open("src/config.json", 'w') as file:
        json.dump(default_config, file, indent=4)

    os.system("rmdir /Q /S __pycache__")

if __name__ == "__main__":
    with open("src/config.json") as f:
        config = json.load(f)
    
    enable = config["reset_config"]

    if enable:
        reset()