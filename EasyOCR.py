import os
import easyocr
from pdf2image import convert_from_path, convert_from_bytes
import shutil

reader = easyocr.Reader(['fr'])

def get_jpg(file_path,filename):

    print(file_path)
    # images = convert_from_path('Attestation.pdf')
    if filename.endswith('.pdf'):
        images_from_path = convert_from_bytes(file_path)
        for idx, image in enumerate(images_from_path):
            img_name = f"image_{idx}.jpg"

            if os.path.isdir('./temps'):
                shutil.rmtree('./temps')
            
            os.makedirs('./temps')

            image.save('./temps/'+img_name, 'JPEG')
            img_path = os.getcwd() + '/temps/' + img_name
            
            return img_path
    
    else:
        return file_path
    


def easyocr_read(img_path):

    easyocr_output = reader.readtext(img_path, paragraph="True", detail = 0)
    easyocr_output = "\n".join(easyocr_output)

    return easyocr_output #Text
