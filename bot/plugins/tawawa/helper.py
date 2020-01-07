import base64


def get_b64_content(full_path):
    with open(full_path, 'rb') as f:
        b64 = base64.b64encode(f.read())

    b64 = str(b64, encoding='utf-8')

    b64 = 'base64://' + b64

    return b64
