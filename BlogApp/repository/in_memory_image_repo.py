import os
from repository.image_repo import ImageRepo
from repository.image_data import dummy_image
from encoding_file import encode_file, decode_file


IMG_FOLDER_PATH = 'static/img/'

class InMemoryImageRepo(ImageRepo):
    def add(self, file_storage):
        file = encode_file(file_storage.filename)
        dummy_image.insert(0, file)
        return file

    def edit(self, new_file):
        file = self.add(new_file)
        return self.get(file)

    def delete(self, filename):
        if os.path.isfile(IMG_FOLDER_PATH + '{}'.format(filename)):
            os.remove(IMG_FOLDER_PATH + '{}'.format(filename))
        else:
            print("Error: %s file not found" % filename)

    def get(self, filename):
        media_type = 'data:image/jpg'
        return media_type + ';base64,' + filename
