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
            image = cv2.cvtColor(image, cv2.COLOR_RGB2RGBA)

        # Assure that the image is in right format
        imageChannelCount = image.shape[2]
        assert imageChannelCount == 4

        # Get the alpha channel of the image
        alpha_channel = image[:, :, 3]

        # Get the mask
        _, mask = cv2.threshold(alpha_channel, 254, 255, cv2.THRESH_BINARY)  # binarize mask

        # Get the color channels of the image
        color = image[:, :, :3]

        # Mask it up
        image = cv2.bitwise_not(cv2.bitwise_not(color, mask=mask))

        cv2.imshow("Window", image)
        cv2.waitKey(0)

        # # cv2.imwrite(item[:-4] + ".jpg", image)
