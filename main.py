from PIL import Image


def gray_scale(image):
    return image.convert("L")


def edge_detection(image):
    pass


def remove_background(image):
    pass


def flip_image(image):
    pass


def blur_image(image):
    pass


def main():
    image_path = "input/test.JPG"
    output_path = "output/test.JPG"
    image = Image.open(image_path)
    output = gray_scale(image)
    output.save(output_path)


if __name__ == "__main__":
    main()
