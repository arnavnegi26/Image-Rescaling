import cv2
import numpy as np

image = cv2.imread(r'C:\Users\famil\Downloads\Wallpaper\daft punk.png')

def main():
    while True:
        print("1.Upscale Image")
        print("2.Downscale Image")
        print("3.Exit")
        choice1 = int(input("Enter choice  :  "))
        if(choice1 == 1):
            upscale()
        elif(choice1 == 2):
            downscale()
        elif(choice1 == 3):
            break














def upscale():
    up_width = int(input("Enter the desired width for new image  :  "))
    up_height = int(input("Enter the desired height for new image  :  "))
    up_points = (up_width, up_height)
    resized_up = cv2.resize(image, up_points, interpolation= cv2.INTER_LINEAR)
    cv2.imshow('Resized Up image by defining height and width', resized_up)
    cv2.waitKey()
    cv2.destroyAllWindows()

def downscale():
    down_width = int(input("Enter the desired width for new image  :  "))
    down_height = int(input("Enter the desired height for new image  :  "))
    down_points = (down_width, down_height)
    resized_down = cv2.resize(image, down_points, interpolation= cv2.INTER_LINEAR)
    cv2.imshow('Resized Down by defining height and width', resized_down)
    cv2.waitKey()
    cv2.destroyAllWindows()

main()