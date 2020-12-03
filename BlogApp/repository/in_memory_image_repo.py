import uuid
import base64
from repository.image_repo import ImageRepo
from repository.image_data import dummy_image

class InMemoryImageRepo(ImageRepo):

    def add(self, file_storage):
        img_id = uuid.uuid1().hex
        file = self.encode_file(file_storage)
        file = 'data:' + file_storage.mimetype + ';base64,' + file
        img_list = [img_id, file]
        dummy_image.insert(0, img_list)
        return img_list

    def edit(self, filename, file_storage):
        self.delete(filename)
        img_list = self.add(file_storage)
        return img_list

    def delete(self, filename):
        for img_list in dummy_image:
            if img_list[0] == filename:
                dummy_image.remove(img_list)
                break

    def get(self, filename):
        img_content = None
        for img_list in list(dummy_image):
            if img_list[0] == filename:
                img_content = img_list[1]
        return img_content

    @staticmethod
    def encode_file(file_storage):
        image_string = base64.b64encode(file_storage.read())
        image_string = image_string.decode('utf-8')

        return image_string
