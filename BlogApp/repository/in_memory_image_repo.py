import os
from repository.image_repo import ImageRepo
from encoding_file import encode_file, decode_file


IMG_FOLDER_PATH = 'static/img/'

class InMemoryImageRepo(ImageRepo):
    def add(self, file_storage):
        file_storage.save(os.path.join(IMG_FOLDER_PATH, file_storage.filename))
        return encode_file(file_storage.filename)

    def edit(self, old_filename, new_file):
        self.delete(old_filename)
        return self.add(new_file)

    def delete(self, filename):
        if os.path.isfile(IMG_FOLDER_PATH + '{}'.format(filename)):
            os.remove(IMG_FOLDER_PATH + '{}'.format(filename))
        else:
            print("Error: %s file not found" % filename)

    def get(self, filename):
        file = decode_file(filename)
        return os.path.join('img/', file)
