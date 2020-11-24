import base64
import os
from repository.image_repo import ImageRepo
from encoding_file import encode_file, decode_file

class InMemoryImageRepo(ImageRepo):
    def add(cls, file_storage):
        image_string = base64.b64encode(file_storage.read())
        return image_string
    
    def edit(cls, old_filename, new_file):
        cls.delete(old_filename)
        return cls.add(new_file)
        
    def delete(cls, filename):
        if os.path.isfile(IMG_FOLDER_PATH + '{}'.format(filename)):
            os.remove(IMG_FOLDER_PATH + '{}'.format(filename))
        else:
            print("Error: %s file not found" % filename)

    def get(cls, filename):
        file = decode_file(filename)
        return os.path.join('img/', file)

