# -*- utf-8 -*-

import cv2.cv2 as cv2


class Deal:
    img = "C:/Users/k/gitme/python/w.jpeg"

    def binaryzation(self):
        im = cv2.imread(self.img)
        im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        th1 = cv2.adaptiveThreshold(im, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 1)
        cv2.imwrite(self.img, th1)
        return th1

    def clear_border(self):
        self.binaryzation()
        im = cv2.imread(self.img)
        h, w = im.shape[:2]
        for y in range(0, w):
            for x in range(0, h):
                if y < 2 or y > w - 2:
                    im[x, y] = 255
                if x < 2 or x > h - 2:
                    im[x, y] = 255
        cv2.imwrite(self.img, im)

    # 点降噪
    def interference_point(self):
        import numpy as np
        import matplotlib.pyplot as plt
        img = cv2.imread(self.img, 0)  # 直接读为灰度图像
        for i in range(2000):  # 添加点噪声
            temp_x = np.random.randint(0, img.shape[0])
            temp_y = np.random.randint(0, img.shape[1])
            img[temp_x][temp_y] = 255

        blur = cv2.medianBlur(img, 5)
        plt.subplot(1, 2, 1), plt.imshow(img, 'gray')  # 默认彩色，另一种彩色bgr
        plt.subplot(1, 2, 2), plt.imshow(blur, 'gray')

    def ocr(self):
        import pytesser3
        from PIL import Image
        tt = pytesser3.image_to_string(Image.open(self.img))
        print(tt)


if __name__ == '__main__':
    Deal().ocr()
