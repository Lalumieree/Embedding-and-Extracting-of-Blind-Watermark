import cv2
import numpy as np
import random

def main():

    ori = 'ori.png'
    img = 'res.png'
    res = 'extracted.png'
    alpha = 5
    decode(ori, img, res, alpha)


def decode(ori_path, img_path, res_path, alpha):
    ori = cv2.imread(ori_path)
    img = cv2.imread(img_path)
    ori_f = np.fft.fft2(ori)
    img_f = np.fft.fft2(img)
    height, width = ori.shape[0], ori.shape[1]
    watermark = (ori_f - img_f) / alpha
    watermark = np.real(watermark)
    res = np.zeros(watermark.shape)
    random.seed(height + width)
    x = list(range(int(height / 2)))
    y = list(range(width))
    random.shuffle(x)
    random.shuffle(y)
    for i in range(int(height / 2)):
        for j in range(width):
            res[x[i]][y[j]] = watermark[i][j]
    #for i in range(int(height / 2)):
    #   for j in range(width):
    #       res[height - 1 - i][width - 1 - j] = res[i][j]
    cv2.imwrite(res_path, res, [int(cv2.IMWRITE_JPEG_QUALITY), 100])


if __name__ == '__main__':
    main()