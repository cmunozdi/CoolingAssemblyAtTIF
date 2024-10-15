import os
import shutil

# Function to get files sorted by name (ascending or descending order)
def get_files_by_name(directory, start_point):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    if start_point == "outlet":  # Start from CP1 (ascending order)
        files = sorted(files)
    elif start_point == "inlet":  # Start from CP2 (descending order)
        files = sorted(files, reverse=True)
    return files

# Function to parse user input for cooling plate codes
def parse_codes(input_codes):
    # Splitting the input string by spaces and extracting the first part (e.g., CP2_043 from CP2_043 (BN2))
    codes = [part.split()[0].replace('_', '-') for part in input_codes.split('\t')]
    return codes

# Function to copy and rename files
def copy_and_rename_files(directory_in, directory_out, image_type, pipe_number, codes, date, start_point):
    files = get_files_by_name(directory_in, start_point)
    
    if len(files) != len(codes):
        print("The number of files in the input folder doesn't match the number of provided codes (must be 6).")
        return

    # Create output directory if it doesn't exist
    if not os.path.exists(directory_out):
        os.makedirs(directory_out)

    output_files = []

    # Copy and rename files
    for i, file in enumerate(files):
        code = codes[i]
        file_extension = os.path.splitext(file)[1]  # Get the file extension
        
        # Build the new file name
        if image_type == "TIM":
            new_name = f"TIM_loop{pipe_number}_{code}_{date}{file_extension}"
        elif image_type == "RTG":
            new_name = f"RTG_loop{pipe_number}_{code}_{date}{file_extension}"
        else:
            new_name = f"loop{pipe_number}_{code}_{date}{file_extension}"
        
        # Get full path to copy the files
        src = os.path.join(directory_in, file)
        dst = os.path.join(directory_out, new_name)
        
        # Copy file
        shutil.copyfile(src, dst)
        output_files.append(new_name)
        print(f"File copied: {file} --> {new_name}")

    # Return the list of renamed files for Excel
    return output_files

# User input
image_type = input("Enter the image type (TIM, RTG, or leave blank): ").strip()
pipe_number = input("Enter the pipe number (2-digit format): ").zfill(2)
codes_input = input("Enter the cooling plate codes (format: CP2_043 (BN2) CP3_107 (BN2) ...; just copy the 6 cells from the excel sheet): ")
codes = parse_codes(codes_input)  # Parse the user's input into the required format
date = input("Enter the date in DD-MM-YY format: ")
start_point = input("Did you start taking photos from the inlet (CP2) or outlet (CP1)? (type 'inlet' or 'outlet'): ").strip().lower()

# Directories
input_directory = "inputs/"
output_directory = "outputs/"

# Copy and rename files
output_files = copy_and_rename_files(input_directory, output_directory, image_type, pipe_number, codes, date, start_point)

# Print the list of output files for Excel
if output_files:
    print("\nFiles copied to 'outputs/' directory (ready to copy to Excel):")
    print("\n".join(output_files))

