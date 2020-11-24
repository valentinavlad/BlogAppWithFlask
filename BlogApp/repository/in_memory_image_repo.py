import base64
import os
from repository.image_repo import ImageRepo
from encoding_file import encode_file, decode_file


IMG_FOLDER_PATH = 'static/img/'

class InMemoryImageRepo(ImageRepo):
    def add(cls, file_storage):
        file_storage.save(os.path.join(IMG_FOLDER_PATH, file_storage.filename))
        f = encode_file(file_storage.filename)
        return encode_file(file_storage.filename)
    
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

