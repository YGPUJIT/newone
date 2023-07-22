# USAGE
# python train_model.py --embeddings output/embeddings.pickle \
#	--recognizer output/recognizer.pickle --le output/le.pickle

# import the necessary packages
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
import argparse
import pickle
import os

class Train:
	def __init__(self):
		self.data = pickle.loads(open(os.path.join(os.path.dirname(__file__),'output/embeddings.pickle'), "rb").read())
		self.le = LabelEncoder()
		self.labels = None
		self.recognizer = SVC(C=10.0, kernel="rbf",gamma=1.0,random_state=0, probability=True)



	def train_model(self):
		print("train done")
		self.labels= self.le.fit_transform(self.data["names"])
		print(self.data["names"])
		self.recognizer.fit(self.data["embeddings"], self.labels)
		f = open(os.path.join(os.path.dirname(__file__),'output/recognizer.pickle'), "wb")
		f.write(pickle.dumps(self.recognizer))
		f.close()
		f = open(os.path.join(os.path.dirname(__file__),'output/le.pickle'), "wb")
		f.write(pickle.dumps(self.le))
		f.close()