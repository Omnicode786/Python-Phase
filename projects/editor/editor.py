from PIL import Image, ImageEnhance,ImageFilter
import os


path = r"E:\Programming\Google  Python\Python-Phase\projects\editor\images"
out_path = r"E:\Programming\Google  Python\Python-Phase\projects\editor\editedimg"

openpath = os.listdir(path)

for index, file in enumerate(openpath):
    img = Image.open(f"{path}/{file}")
    #  by doing this the variable is not an object


    edit = img.filter(ImageFilter.SHARPEN).filter(ImageFilter.DETAIL).convert('L').rotate(90)
    #  the L in the convert converts it into a grayscale image

    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)

    # ImageEnhance.Contrast(img) doesn’t apply contrast right away—it just creates a "contrast tool" that we can use later with .enhance(factor) to actually apply contrast.
    
    
    edit = enhancer.enhance(factor).rotate(-90)


    edit.save(f"{out_path}/{index}_edited.jpg")

edit.show()