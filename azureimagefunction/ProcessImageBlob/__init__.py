import azure.functions as func
from PIL import Image
import io

def resize_image(input_image, size):
    img = Image.open(input_image)
    img_resized = img.resize(size)
    # Save resized image to a bytes buffer
    img_byte_arr = io.BytesIO()
    img_resized.save(img_byte_arr, format='JPEG')
    img_byte_arr.seek(0)
    return img_byte_arr

def main(myblob: func.InputStream, outputBlob: func.Out[func.InputStream]):
    # Resize the uploaded image
    resized_image = resize_image(myblob, (600, 600))
    # Output the resized image to the output blob container
    outputBlob.set(resized_image)
