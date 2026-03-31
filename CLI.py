import image_functions
from PIL import Image
import os


def main():
    # Validating Input File Path
    input_file_path = input("Input File Path:")
    valid_file_extensions = {ex for ex, f in Image.registered_extensions().items() if f in Image.OPEN}
    if not os.path.exists(input_file_path):
        print(f"Invalid Input File. File Path Does not Exist.\nInput File Path Received: {input_file_path}")
        return -1

    input_file, input_ext = os.path.splitext(input_file_path)
    if input_ext.lower() not in valid_file_extensions:
        print(f"Invalid Input File. File type {input_ext} is unsupported.\nInput File Path Received: {input_file_path}")
        return -1

    # Checking if the output directory exists
    output_directory_path = input("Output Directory Path:")
    if not os.path.exists(output_directory_path):
        print(f"Invalid Output Path. Output Path Does not Exist. \nOutput Path Received: {output_directory_path}")
        return -1

    if not os.path.isdir(output_directory_path):
        print(f"Invalid Output Path. Output Path is not a Directory. \nOutput Path Received: {output_directory_path}")
        return -1

    # File Name Error Handling
    inputted_output_file_name = input("Output Name (With File Extension):")
    output_name, output_ext = os.path.splitext(inputted_output_file_name)
    # If the file name does not have a supported file type or any file type
    # Replace it to be the same as the input's file type
    if output_ext.lower() not in valid_file_extensions:
        inputted_output_file_name = output_name + input_ext

    # Return an error if there already exists a matching output file
    output_file_path = output_directory_path + "\\" + inputted_output_file_name
    if os.path.exists(output_file_path):
        print(
            f"Invalid Output Name. File Already Exists in Output Directory."
            f"\n Output File Path: {output_directory_path}\\{output_name}{output_ext}"
        )
        return -1

    # Image Effect Selection
    print("Input the number of the effect you would like to apply:\n"
          "1.Gray Scale\n"
          "2.Edge Detection\n"
          "3.Vertical Flip\n"
          "4.Horizontal Flip\n"
          "5.Gaussian Blur")
    function_type = int(input("Function type:"))

    # Image Processing
    input_image = Image.open(input_file_path)
    output_image = input_image

    if function_type == 1:
        output_image = image_functions.gray_scale(input_image)
    elif function_type == 2:
        output_image = image_functions.edge_detection(input_image)
    elif function_type == 3:
        output_image = image_functions.vertical_flip(input_image)
    elif function_type == 4:
        output_image = image_functions.horizontal_flip(input_image)
    elif function_type == 5:
        blur_intensity = int(input("Blur Intensity (1-100):"))
        output_image = image_functions.blur_image(input_image, blur_intensity)

    output_image.save(output_file_path)
    print(f"Successfully saved {inputted_output_file_name} to {output_file_path}")


if __name__ == "__main__":
    main()
