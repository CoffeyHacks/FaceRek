import os
import shutil

# path to folder where the user can upload new images
upload_folder = '/path/to/upload/folder'

# path to folder where the program is looking for known faces
known_faces_folder = '/path/to/known/faces/folder'

# check for new images in the upload folder
for file in os.listdir(upload_folder):
    if file.endswith('.jpg'):
        # construct the full path to the file
        src_path = os.path.join(upload_folder, file)
        dst_path = os.path.join(known_faces_folder, file)

        # copy the new image to the known faces folder
        shutil.copy2(src_path, dst_path)

        # log the new image
        logging.info(f'{file} has been added to the known faces.')
