import json
import os

def combine_files(input_files, output_folder, output_name, separate_files, delimiter_before, delimiter_after):
    output_file_path = os.path.join(output_folder, f"{output_name}.txt")
    with open(output_file_path, 'w') as output_file:
        for i, input_file in enumerate(input_files):
            with open(input_file, 'r') as file:
                content = file.read()
                
                if delimiter_before:
                    elements = content.split(delimiter_before)
                else:
                    elements = content.splitlines()

                for element in elements:
                    if delimiter_after:
                        sub_elements = element.split(delimiter_after)
                        for sub_element in sub_elements:
                            output_file.write(sub_element.strip())
                    else:
                        output_file.write(element.strip())

            if separate_files and i != len(input_files) - 1:
                output_file.write('\n' + '-' * 20 + f" {os.path.basename(input_file)} " + '-' * 20 + '\n')

    print(f"All input files combined into {output_file_path}")

def main():
    try:
        with open("src/config.json", "r") as f:
            config = json.load(f)
    except FileNotFoundError:
        print("Config file not found.")
        return

    input_files = config.get("input_files")
    output_name = config.get("output_name")
    output_folder = "output"
    separate_files = config.get("separate_files", False)
    delimiter_before = config.get("delimiter_before", None)
    delimiter_after = config.get("delimiter_after", None)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    if input_files and output_name:
        combine_files(input_files, output_folder, output_name, separate_files, delimiter_before, delimiter_after)
    else:
        print("Input files or output name not specified in the config.")

if __name__ == "__main__":
    main()
