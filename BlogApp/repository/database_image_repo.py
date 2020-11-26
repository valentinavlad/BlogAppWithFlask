import os
import uuid

from repository.image_repo import ImageRepo

IMG_FOLDER_PATH = 'static/img/'
FILE_EXTENSIONS = ['.jpg', '.png', '.gif']
class DatabaseImageRepo(ImageRepo):

    def add(self, file_storage):
        if file_storage.filename != '':
            img_id = uuid.uuid1().hex
            filename = file_storage.filename
            file_storage.save(os.path.join(IMG_FOLDER_PATH, filename))
            renamed_file = img_id + "_" + filename
            os.rename(IMG_FOLDER_PATH + '{}'.format(filename),\
               IMG_FOLDER_PATH + '{}'.format(renamed_file))
        return renamed_file

    def edit(self, old_filename, new_file):
        self.delete(old_filename)
        return self.add(new_file)

    def delete(self, filename):
        if os.path.isfile(IMG_FOLDER_PATH + '{}'.format(filename)):
            os.remove(IMG_FOLDER_PATH + '{}'.format(filename))
        else:
            print("Error: %s file not found" % filename)

    def get(self, filename):
        return os.path.join('/'+IMG_FOLDER_PATH, filename)

    def check_img_extension(self, filename):
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in FILE_EXTENSIONS:
            return False
        return True