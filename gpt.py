import numpy as np
import os
import cv2
import random
import matplotlib.pyplot as plt
DATA_DIR = 'data'
IMG_SIZE = 224


a="""## data/
  ├── class1/
  │   ├── img1.jpg
  │   ├── img2.jpg
  │   ├── ...
  ├── class2/
  │   ├── img1.jpg
  │   ├── img2.jpg
  │   ├── ...
  ├── ...### 
"""

def load_data(data_dir):
    images = []
    labels = []
    for class_name in os.listdir(data_dir):
        class_dir = os.path.join(data_dir, class_name)
        for img_name in os.listdir(class_dir):
            img_path = os.path.join(class_dir, img_name)
            img = cv2.imread(img_path)
            img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
            img = img.astype('float32') / 255.0
            images.append(img)
            labels.append(class_name)
    return np.array(images), np.array(labels)

    
def preprocess_image(img_path):
    img = cv2.imread(img_path)
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    img = img.astype('float32') / 255.0
    return img

def split_data(images, labels, test_size=0.2):
    data = list(zip(images, labels))
    random.shuffle(data)
    split_index = int(len(data) * test_size)
    test_data = data[:split_index]
    train_data = data[split_index:]
    train_images, train_labels = zip(*train_data)
    test_images, test_labels = zip(*test_data)
    return np.array(train_images), np.array(train_labels), np.array(test_images), np.array(test_labels)


class  MultiClassClassifier:
    def __init__(self, num_classes):
        self.num_classes = num_classes
        self.W = np.random.randn(IMG_SIZE * IMG_SIZE * 3, num_classes) / np.sqrt(IMG_SIZE * IMG_SIZE * 3)
        self.b = np.zeros((1, num_classes))

    def train(self, X, y, learning_rate=0.1, num_epochs=1000, batch_size=32):
        num_samples = X.shape[0]
        for epoch in range(num_epochs):
            epoch_loss = 0
            for i in range(0, num_samples, batch_size):
                X_batch = X[i:i+batch_size]
                y_batch = y[i:i+batch_size]
                scores = X_batch.reshape(batch_size, -1).dot(self.W) + self.b
                exp_scores = np.exp(scores)
                probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
                loss = -np.sum(np.log(probs[range(batch_size),y_batch])) / batch_size
                epoch_loss += loss
                dscores = probs
                dscores[range(batch_size),y_batch] -= 1
                dscores /= batch_size
                dW = X_batch.reshape(batch_size, -1).T.dot(dscores)
                db = np.sum(dscores, axis=0, keepdims=True)
                self.W -= learning_rate * dW
                self.b -= learning_rate * db
            epoch_loss /= num_samples
            if epoch % 100 == 0:
                print(f'Epoch {epoch}: loss = {epoch_loss:.4f}')

    def predict(self, X):
        scores = X.reshape(X.shape[0], -1).dot(self.W) + self.b
        return np.argmax(scores, axis=1)


def evaluate_classifier(images, labels, classifier):
    num_correct = 0
    num_total = 0
    for i in range(len(images)):
        img = images[i]
        label = labels[i]
        pred_label = classifier.predict(img.reshape(1, -1))[0]
        if pred_label == label:
            num_correct += 1
        num_total += 1
    accuracy = num_correct / num_total
    print(f'Accuracy = {accuracy:.4f}')


def evaluate_classifier(images, labels, classifier):
    num_correct = 0
    num_total = 0
    for i in range(len(images)):
        img = images[i]
        label = labels[i]
        pred_label = classifier.predict(img.reshape(1, -1))[0]
        if pred_label == label:
            num_correct += 1
        num_total += 1
    accuracy = num_correct / num_total
    print(f'Accuracy = {accuracy:.4f}')

data_dir = 'data'
num_classes = len(os.listdir(data_dir))

images, labels = load_data(data_dir)
train_images, train_labels, test_images, test_labels = split_data(images, labels, test_size=0.2)

classifier = MultiClassClassifier(num_classes)
classifier.train(train_images, train_labels)
evaluate_classifier(test_images, test_labels, classifier)
