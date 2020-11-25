import uuid
from repository.image_repo import ImageRepo
from repository.image_data import dummy_image
from encoding_file import encode_file, decode_file

class InMemoryImageRepo(ImageRepo):
    def add(self, file_storage):
        img_id = uuid.uuid1().hex
        file = encode_file(file_storage.filename)
        file = img_id + '_' + file
        dummy_image.insert(0, file)
        return file

    def edit(self, new_file):
        file = self.add(new_file)
        return self.get(file)

    def delete(self, filename):
        file = filename.split(',')
        x = file[1]
        last_char = x[-5:]
        dummy_image.remove(file[1])

    def get(self, filename):
        if filename.startswith('data:'):
            return filename
        file = filename.split('_')
        media_type = 'data:image/jpg'
        return media_type + ';base64,' + file[1]
