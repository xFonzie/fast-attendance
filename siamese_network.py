import cv2
import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import transforms
import os
import numpy as np


class SiameseNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 32, kernel_size=10)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=7)
        self.conv3 = nn.Conv2d(64, 64, kernel_size=4)
        self.conv4 = nn.Conv2d(64, 128, kernel_size=4)
        self.fc1 = nn.Linear(128 * 24 * 24, 1024)
        self.fc2 = nn.Linear(1024, 1)
        
    def forward_once(self, x):
        # print(x.shape)
        x = F.max_pool2d(F.relu(self.conv1(x)), kernel_size=2, stride=2)
        # print(x.shape)
        x = F.max_pool2d(F.relu(self.conv2(x)), kernel_size=2, stride=2)
        # print(x.shape)
        x = F.max_pool2d(F.relu(self.conv3(x)), kernel_size=2, stride=2)
        # print(x.shape)
        x = F.relu(self.conv4(x))
        # print(x.shape)
        x = x.view(x.size()[0], -1)
        # print(x.shape)
        x = F.relu(self.fc1(x))
        return x
    
    def forward(self, anchor, positive):
        output1 = self.forward_once(anchor)
        output2 = self.forward_once(positive)
        output = self.fc2(torch.abs(output1 - output2))
        return F.sigmoid(output)

model = SiameseNetwork()

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

best_model = SiameseNetwork()
best_model.load_state_dict(torch.load('models/best_model.pt'))
best_model.to(device)

transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5,0.5,0.5], std=[0.5,0.5,0.5])
])

def preprocess(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (250, 250))
    image = transform(image)
    image = image.unsqueeze(0)
    return image

def verify(image, dir):
    image = preprocess(image).to(device)
    results = []
    model.eval()
    with torch.no_grad():
        for file in os.listdir(dir):
            img = cv2.imread(os.path.join(dir, file))
            img = preprocess(img).to(device)
            
            output = best_model(image, img)
            results.append(output.item())
    print(dir, results)
    return np.mean(results)

def recognize(image):
    people = {}
    for dir in os.listdir('verification_data'):
        people[dir] = verify(image, f'verification_data/{dir}')
    people = {k: v for k, v in sorted(people.items(), key=lambda item: item[1], reverse=True)}
    return people