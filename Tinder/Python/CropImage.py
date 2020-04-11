from PIL import Image
area=(950,155,1338,756)

def cropim(input):
        img= Image.open(input)
        cropped_img = img.crop(area)
        cropped_img.save(input)
        return 



