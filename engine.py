import sys
import re
import os
from pymagnitude import Magnitude
from models import Item
import numpy as np
from nltk.corpus import stopwords
vectors = Magnitude(os.environ['EMBEDDING_FILE'])

def tokenize(string):
    text = re.sub("[^a-zA-Z]", " ", string)
    tokens = text.lower().split()
    return tokens

items = list()
items.append(Item(0, "cat"))
items.append(Item(1, "dog"))
items.append(Item(2, "monkey"))
items.append(Item(3, "truck"))
items.append(Item(4, "car"))

def similarity(item1, item2, vectors):
    item1_words = [word for word in tokenize(item1.text) if word in vectors]
    item2_words = [word for word in tokenize(item2.text) if word in vectors]
    item1_vectors = [vectors.query(word) for word in item1_words]
    item2_vectors = [vectors.query(word) for word in item2_words]
    item1_vector = sum(item1_vectors) / len(item1_vectors)
    item2_vector = sum(item2_vectors) / len(item2_vectors)
    return -1 * np.linalg.norm(item1_vector - item2_vector)

target = items[4]
champion = items[0]
distances = list()
for item in items:
    distances.append(similarity(item, target, vectors))
    if similarity(item, target, vectors) > similarity(champion, target, vectors):
        champion = item
print(distances)