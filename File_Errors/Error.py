import os
import shutil

class FileNotFoundError(Exception):
    pass
class InvalidInputDataError(Exception):
    pass
class DiskSpaceFullError(Exception):
    pass

# step-2 read input data from the file
def read_input_file(file_path):
    # check if file exist or not
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Error: The file '{file_path}' was not found!")
    # open the file reading the data
    with open(file_path , 'r', encoding='utf-8') as file:
        data = file.read()
    # check if data is a string
    if not isinstance(data, str):
        raise InvalidInputDataError(f"The Input data is not a valid string!")
    return data

# step-3 process data
def process_text_data(data):
    try:
        if data == "":
            raise InvalidInputDataError("The input data is an empty string!")
        words = data.split()
        word_count = len(words)
        char_frequency = {}
        for char in data:
            if char.isalpha():
                char_frequency[char] = char_frequency.get(char, 0)+1

        # palceholder for generating word count (text-based representation)
        word_cloud = f"Word Cloud (Words: {word_count}, Unique Characters : {len(char_frequency)})"

        return {
            'word_count' : word_count,
            'char_frequency' : char_frequency,
            'word_cloud' : word_cloud
        }
    except Exception as e:
        raise InvalidInputDataError(f"Error while processing text data : {str(e)}")


# Step 4: Write processed data to an output file
def write_output_file(output_path, results):
    """Write processed results to the output file."""
    try:
        # Simulate disk space check
        if not check_disk_space():
            raise DiskSpaceFullError("Error: Insufficient disk space to write the output file.")
        
        # Write data to the output file
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write("Word Count: " + str(results['word_count']) + "\n")
            file.write("Character Frequencies: " + str(results['char_frequency']) + "\n")
            file.write("Word Cloud: " + results['word_cloud'] + "\n")
    
    except IOError as e:
        raise DiskSpaceFullError(f"Error writing to file '{output_path}': {str(e)}")


# Step 5: Simulate a check for disk space
def check_disk_space():
    total, used, free = shutil.disk_usage("/")
    return free > 0.5 * 1024 * 1024  # Return True if more than 1MB free

# Step 6: Main function to bring everything together
def main():
    try:
        # Get user input for the input and output file paths
        input_file = input("Enter the input file path: ")
        output_file = input("Enter the output file path: ")

        # Step 1: Read the input data
        input_data = read_input_file(input_file)

        # Step 2: Process the text data
        results = process_text_data(input_data)

        # Step 3: Store the processed results
        write_output_file(output_file, results)

        print("Text processing completed successfully.")
    
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except InvalidInputDataError as inv_error:
        print(inv_error)
    except DiskSpaceFullError as dsf_error:
        print(dsf_error)
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

# Step 7: Run the main function
if __name__ == "__main__":
    main()
