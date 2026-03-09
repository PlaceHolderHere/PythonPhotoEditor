from PIL import Image, ImageFilter


def gray_scale(image):
    return image.convert("L")


def edge_detection(image):
    return image.filter(ImageFilter.FIND_EDGES)


def remove_background(image):
    pass


def flip_image(image):
    pass


def blur_image(image, intensity):  # Base Level is 2
    return image.filter(ImageFilter.GaussianBlur(radius=intensity))


def main():
    image_path = "input/test.JPG"
    output_name = "blur.JPG"
    output_path = f"output/{output_name}"
    image = Image.open(image_path)
    # output = gray_scale(image)  # Testing
    # output = edge_detection(image)  # Testing
    output = blur_image(image, 5)  # Testing
    output.save(output_path)


if __name__ == "__main__":
    main()
