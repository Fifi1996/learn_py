'''
python imaging liibrary
是平台事实上的图像处理标准库
PIL支持py2.7，
3.x兼容Pillow

'''
#操作图像
from PIL import Image,ImageFilter
#打开一个jpg图像,当前路径
im=Image.open('1.jpg')
#获取图像尺寸
w,h=im.size
print('Original image size: %sx%s' % (w, h))
#缩放到50%
im.thumbnail((w/2,h/2))
print('Resize image to: %sx%s' % (w//2, h//2))
# 把缩放后的图像用jpeg格式保存:
im.save('thumbnail.jpg', 'jpeg')

#其他功能如切片，旋转，滤镜，输出文字，，，，

#模糊效果
im=Image.open('1.jpg')
#应用模糊滤镜
im2 = im.filter(ImageFilter.BLUR)
im2.save('2.jpg','jpeg')


#ImageDraw提供了一系列绘画方式，让我们可以直接绘图
#比如生成字母验证码图片
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random
#随机字母
def rndChar():
    return chr(random.randint(65,90))
#随机颜色1
def rndColor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))
#240*60
width=60*4
height=60
image=Image.new('RGB',(width,height),(255,255,255))
#创建font对象
font = ImageFont.truetype('C:\Windows\Fonts/Arial.ttf', 36)
#创建Draw对象
draw=ImageDraw.Draw(image)
#填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=rndColor())
#输出文字
for t in range(4):
    draw.text((60*t+10,10),rndChar(),font=font,fill=rndColor2())
#模糊
image=image.filter(ImageFilter.BLUR)
image.save('code.jpg','jpeg')