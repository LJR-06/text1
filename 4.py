import numpy as np
import mnist
from PIL import Image

# 加载数据集
x_train = mnist.train_images()
t_train = mnist.train_labels()
x_test = mnist.test_images()
t_test = mnist.test_labels()

# 展示图片函数
def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()

# 取第一张图片
img = x_train[0]
label = t_train[0]
print("图片数字标签：", label)
print("二维图片尺寸：", img.shape)

# 弹出图片窗口
img_show(img)