from facenet_pytorch import MTCNN
from PIL import Image

mtcnn = MTCNN(margin=50, keep_all=True, post_process=False)

def detect(img_file_buffer):
    img = Image.open(img_file_buffer)
    out = mtcnn(img)
    faces = []
    for face in out:
        faces.append(face.permute(1, 2, 0).int().numpy())
    return faces