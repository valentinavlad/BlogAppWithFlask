import uuid
from repository.image_repo import ImageRepo
from repository.image_data import dummy_image
from encoding_file import encode_file, decode_file

class InMemoryImageRepo(ImageRepo):
    def add(self, file_storage):
        img_id = uuid.uuid1().hex
        file = encode_file(file_storage.filename)
        img_list = [img_id, file]
        dummy_image.insert(0, img_list)
        return img_id

    def edit(self, new_file):
        img_id = self.add(new_file)
        img_content = self.get(img_id)
        return [img_id, img_content]
         

    def delete(self, filename):
        for img_list in dummy_image:
           if img_list[0] == filename:
                dummy_image.remove(img_list)
                break;

    def get(self, filename):
        if filename.startswith('data:'):
            return filename
        img_content = self.find_by_name(filename)
        media_type = 'data:image/jpg'
        return media_type + ';base64,' + img_content

    def find_by_name(self, filename):
        for img_list in dummy_image:
            if img_list[0] == filename:
                return img_list[1]
