import os
import uuid 
from flask import send_from_directory
from repository.image_repo import ImageRepo

IMG_FOLDER_PATH = 'static/img/'

class DatabaseImageRepo(ImageRepo):
    
    def add(cls, file_storage):
        if file_storage.filename != '':
            id = uuid.uuid1().hex
            filename = file_storage.filename
            file_storage.save(os.path.join(IMG_FOLDER_PATH, filename))
            renamed_file = id + "_" + filename
            os.rename(IMG_FOLDER_PATH + '{}'.format(filename), IMG_FOLDER_PATH + '{}'.format(renamed_file))
        return renamed_file
    
    def edit(cls, old_filename, new_file):
        cls.delete(old_filename)
        return cls.add(new_file)
        
    def delete(cls, filename):
        if os.path.isfile(IMG_FOLDER_PATH + '{}'.format(filename)):
            os.remove(IMG_FOLDER_PATH + '{}'.format(filename))
        else:
            print("Error: %s file not found" % filename)

    def get(cls, filename):
        return os.path.join('img/', filename)
