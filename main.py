from Classes.IO import IO
import os
import cv2

if __name__ == "__main__":
    images = os.listdir(IO.fpl2fp([".", "Origin"]))
    for item in images:

        image = cv2.imread(IO.fnl2fn([".", "Origin", item]), cv2.IMREAD_UNCHANGED)

        # Get the image channel information
        imageChannelCount = image.shape[2]

        # Judge if we need to convert the image format
        if imageChannelCount == 3:
            # JPG format, only have 3 channels
            # Then convert it into 4-channel PNG format
            image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
        elif imageChannelCount == 4:
            # image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGRA)
            pass
            pass
        else:
            raise BaseException("Unsupported Channel Number: " + str(imageChannelCount))

        # Assure that the image is in right format
        imageChannelCount = image.shape[2]
        assert imageChannelCount == 4

        count = 0
        for row in image:
            count += 1
            # print(count)
            for pixel in row:
                # print(pixel)
                alpha = pixel[3] / 255
                # print(alpha)
                pixel[0] = pixel[0] * alpha + 255 * (1 - alpha)
                pixel[1] = pixel[1] * alpha + 255 * (1 - alpha)
                pixel[2] = pixel[2] * alpha + 255 * (1 - alpha)

        image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
        cv2.imwrite(item[:-4] + ".jpg", image)
        print("Finished processing: " + item[:-4] + ".jpg")
