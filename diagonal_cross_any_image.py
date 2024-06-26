import numpy as np
from PIL import Image

def main():
    with Image.open('img6.jpg') as imp_img:
        gray_image = imp_img.convert("L")
        gray_image.show()
        gray_image_array = np.array(gray_image)
        ratio = len(gray_image_array)/len(gray_image_array[0])#3*4 er 3/4

        for i in range(len(gray_image_array)):
            for j in range(len(gray_image_array[0])):
                if (i> ratio*j-25 and i< ratio*j+25) or ((i > len(gray_image_array) -25-ratio*j) and (i < len(gray_image_array) +25-ratio*j)):
                    gray_image_array[i][j]=0
        gray_image = Image.fromarray(gray_image_array)
        gray_image.show()
        gray_image.save('output_images/cross_any.jpg')


if __name__ == '__main__':
    main()
