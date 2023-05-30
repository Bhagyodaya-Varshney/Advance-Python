from rembg import remove
from PIL import Image
input_path = r'Input Image Path'
output_path = 'New1.jpeg'
input = Image.open(input_path)
output = remove(input)
output.save(output_path)
