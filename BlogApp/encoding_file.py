import base64
import uuid

def encode_file(file):
    with open('static/img/{}'.format(file), 'rb') as binary_file:
        binary_file_data = binary_file.read()
        base64_encoded_data = base64.b64encode(binary_file_data)
        base64_message = base64_encoded_data.decode('utf-8')

        return base64_message

def decode_filse(encoded_file, file):
    base64_img_bytes = encoded_file.encode('utf-8')
    with open('static/img/{}'.format(file), 'wb') as file_to_save:
        decoded_image_data = base64.decodebytes(base64_img_bytes)
        file_to_save.write(decoded_image_data)
        return decoded_image_data

def decode_file(encoded_file):
    base64_img_bytes = encoded_file.encode('utf-8')
    id = uuid.uuid1().hex
    file = 'test' + '_' + id + '.jpg'
    with open('static/img/{}'.format(file), 'wb') as file_to_save: # create a writable image and write the decoding resul
        decoded_image_data = base64.decodebytes(base64_img_bytes)
        file_to_save.write(decoded_image_data)
        return file
