import os
from PIL import Image

folder_in = "images"
folder_out = "resized_images"
target_width = 500

def resize_images(folder_in, folder_out, target_width):
    if not os.path.exists(folder_out):
        os.makedirs(folder_out)

    for file in os.listdir(folder_in):
        if file.lower().endswith(('jpg', 'jpeg', 'png', 'gif')):
            try:
                # open the image
                image_path = os.path.join(folder_in, file)
                img = Image.open(image_path)
                # convert the image to RGB if it's not
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                # get the original size
                original_width, original_height = img.size
                # calculate the aspect ratio
                aspect_ratio = original_width / original_height
                # calculate the new height after resizing
                new_height = int(target_width / aspect_ratio)
                # resize the image
                resized_img = img.resize((target_width, new_height), Image.LANCZOS)
                # save the resized image
                output_path = os.path.join(folder_out, file)
                resized_img.save(output_path)

                print(f'{file} was resized successfully')

            except Exception as e:
                print(f'Error resizing {file}: {str(e)}')

if __name__ == '__main__':
    resize_images(folder_in, folder_out, target_width)
    print(f'Successfully resized all images in {folder_in} folder')
