import image_functions
from PIL import Image


def main():
    input_file_path = input("Input File Path:")
    output_directory_path = input("Output Directory Path:")
    output_file_name = input("Output Name (With File Extension):")
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

    output_file_path = f"{output_directory_path}/{output_file_name}"
    output_image.save(output_file_path)
    print(f"Successfully saved {output_file_name} to {output_file_path}")


if __name__ == "__main__":
    main()
