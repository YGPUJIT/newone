# USAGE
# python extract_embeddings.py --dataset dataset --embeddings output/embeddings.pickle \
#	--detector face_detection_model --embedding-model openface_nn4.small2.v1.t7

from imutils import paths
import numpy as np
import argparse
import imutils
import pickle
import cv2
import os

print("[INFO] loading face detector...")

class Embeddings():
	def __init__(self):
		self.protoPath = os.path.sep.join([os.path.dirname(__file__),'face_detection_model', "deploy.prototxt"])
		self.modelPath = os.path.sep.join([os.path.dirname(__file__),'face_detection_model',"res10_300x300_ssd_iter_140000.caffemodel"])
		self.detector = cv2.dnn.readNetFromCaffe(self.protoPath, self.modelPath)
		self.embedder = cv2.dnn.readNetFromTorch(os.path.sep.join([os.path.dirname(__file__),'openface_nn4.small2.v1.t7']))
		self.imagePaths = list(paths.list_images(os.path.sep.join([os.path.dirname(__file__),'dataset'])))
		self.knownEmbeddings = []
		self.knownNames = []
		self.total = 0

	
	def extract_embeddings(self):
		for (i, imagePath) in enumerate(self.imagePaths):
			name = imagePath.split(os.path.sep)[-2]
			image = cv2.imread(imagePath)
			# image = imutils.resize(image, width=350)
			# image=cv2.resize(image,(1920,1080))
			image = imutils.resize(image, width=600)
			# image=cv2.filter2D(image,-1,np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]]))
			(h, w) = image.shape[:2]
			imageBlob = cv2.dnn.blobFromImage(image, 1.0, (300, 300),
				(104.0, 177.0, 123.0), swapRB=False, crop=False)
			self.detector.setInput(imageBlob)
			detections = self.detector.forward()
			if len(detections) > 0:
				i = np.argmax(detections[0, 0, :, 2])
				confidence = detections[0, 0, i, 2]
				if confidence > 0.5:
					box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
					(startX, startY, endX, endY) = box.astype("int")
					face = image[startY:endY, startX:endX]
					(fH, fW) = face.shape[:2]
					if fW < 20 or fH < 20:
						continue
					faceBlob = cv2.dnn.blobFromImage(face, 1.0 / 255,(96, 96), (0, 0, 0), swapRB=True, crop=False)
					self.embedder.setInput(faceBlob)
					vec = self.embedder.forward()
					self.knownNames.append(name)
					self.knownEmbeddings.append(vec.flatten())
					self.total += 1
		print("DONE Embedding")
		data = {"embeddings": self.knownEmbeddings, "names": self.knownNames}
		p=os.path.sep.join([os.path.dirname(__file__),'output', "embeddings.pickle"])
		f = open(p, "wb")
		f.write(pickle.dumps(data))
		f.close()

