import uuid
import base64
from repository.image_repo import ImageRepo
from repository.image_data import dummy_image
from encoding_file import encode_file

class InMemoryImageRepo(ImageRepo):
    def add(self, file_storage):
        img_id = uuid.uuid1().hex
        if self.is_base64(file_storage.filename):
            file = file_storage.filename
        else:
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
                break

    def get(self, filename):
        if filename.startswith('data:'):
            return filename
        img_content = self.find_by_name(filename)
        media_type = 'data:image/jpg'
        return media_type + ';base64,' + img_content

    def find_by_name(self, filename):
        img_content = None
        for img_list in dummy_image:
            if img_list[0] == filename:
                 img_content = img_list[1]
        return img_content

    def is_base64(self, sb):
        if isinstance(sb, str):
            sb_bytes = bytes(sb, 'ascii')
        elif isinstance(sb, bytes):
            sb_bytes = sb
        else:
            raise ValueError("Argument must be string or bytes")
        return base64.b64encode(base64.b64decode(sb_bytes)) == sb_bytes

    def check_img_extension(self, filename):
        return True