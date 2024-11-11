from PIL import Image

# 打开 PNG 图像文件
img = Image.open('build/logo.png')

# 转换并保存为 ICO 文件
img.save('logo.ico', format='ICO', sizes=[(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])
