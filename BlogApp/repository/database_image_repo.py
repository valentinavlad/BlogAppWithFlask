import os
import uuid 
from repository.image_repo import ImageRepo

IMG_FOLDER_PATH = 'static/img/'

class DatabaseImageRepo(ImageRepo):
    @staticmethod
    def add(file_storage):
        if file_storage.filename != '':
            id = uuid.uuid1().hex
            filename = file_storage.filename
            file_storage.save(os.path.join(IMG_FOLDER_PATH, filename))
            renamed_file = id + "_" + filename

            os.rename(IMG_FOLDER_PATH + '{}'.format(filename), IMG_FOLDER_PATH + '{}'.format(renamed_file))
        return renamed_file

    def edit(cls, post):
        pass
 
    def delete(cls, filename):
        if os.path.isfile(IMG_FOLDER_PATH + '{}'.format(filename)):
            os.remove(IMG_FOLDER_PATH + '{}'.format(filename))
        else:
            print("Error: %s file not found" % filename)

    def get(cls, owner_id, records_per_page, offset):
        pass

    
    def upload_file():
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            uploaded_file.save(os.path.join('static/img/', uploaded_file.filename))
        return uploaded_file
