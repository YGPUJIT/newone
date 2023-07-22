# USAGE
# python recognize_video.py --detector face_detection_model \
#	--embedding-model openface_nn4.small2.v1.t7 \
#	--recognizer output/recognizer.pickle \
#	--le output/le.pickle

# import the necessary packages
from imutils.video import VideoStream
from imutils.video import FPS
from PatientRegistration.models import Patient
import numpy as np
import argparse
import imutils
import pickle
import time
import cv2
import os
from concurrent.futures import ThreadPoolExecutor
from ...sendmail import sendMail



class Recognize:
	def __init__(self,data):
		self.protoPath = os.path.sep.join([os.path.dirname(__file__),'face_detection_model', "deploy.prototxt"])
		self.modelPath = os.path.sep.join([os.path.dirname(__file__),'face_detection_model',"res10_300x300_ssd_iter_140000.caffemodel"])
		self.detector = cv2.dnn.readNetFromCaffe(self.protoPath, self.modelPath)
		self.embedder = cv2.dnn.readNetFromTorch(os.path.sep.join([os.path.dirname(__file__),'openface_nn4.small2.v1.t7']))
		self.recognizer = None
		self.le = None
		# self.vs = VideoStream(src=0).start()
		self.vs = None
		self.timestamp=0.0
		self.executor=ThreadPoolExecutor(max_workers=2)
		self.d=data
		self.name=None
		self.id=None
		self.offender=dict()

	def capture_and_check(self):	
		# cv2.waitKey(100)
		self.recognizer = pickle.loads(open(os.path.sep.join([os.path.dirname(__file__),'output/recognizer.pickle']), "rb").read())
		self.le = pickle.loads(open(os.path.sep.join([os.path.dirname(__file__),'output/le.pickle']), "rb").read())
		
			#if camera
		# frame = self.vs.read()
			#if camera

			#if video played
		_,frame = self.vs.read()
		if(not _):
			self.vs.set(cv2.CAP_PROP_POS_FRAMES, 0)
			return np.zeros((10,10),np.uint8)
			#if video played


		# frame=cv2.resize(frame, (350,350))
		# frame = imutils.resize(frame, width=350)
		frame = imutils.resize(frame, width=600)
		frame1=frame
		# frame=cv2.filter2D(frame,-1,np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]]))
		(h, w) = frame.shape[:2]
		imageBlob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0, (300, 300),(104.0, 177.0, 123.0), swapRB=False, crop=False)
		self.detector.setInput(imageBlob)
		detections = self.detector.forward()

		for i in range(0, detections.shape[2]):
			confidence = detections[0, 0, i, 2]

			if confidence > 0.50:
				box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
				(startX, startY, endX, endY) = box.astype("int")
				face = frame[startY:endY, startX:endX]
				(fH, fW) = face.shape[:2]
				if fW < 20 or fH < 20:
					continue
				faceBlob = cv2.dnn.blobFromImage(face, 1.0 / 255,(96, 96), (0, 0, 0), swapRB=True, crop=False)
				self.embedder.setInput(faceBlob)
				vec = self.embedder.forward()
				preds = self.recognizer.predict_proba(vec)[0]
				j = np.argmax(preds)
				proba = preds[j]
				name = self.le.classes_[j]
				# if(name not in self.d):
				# 	return frame1
				text='unknown'
				if(name in self.d and proba>0.50 and name!='unknown'):
					I,N=name.split('-')
					patient=Patient.objects.get(pid=I.strip().upper())
					if patient.initiateTreatment:
						current=int(time.time())
						if((current-self.d[name])>120):
							self.executor.submit(sendMail,name,patient)
							self.d[name]=current
							if(I not in self.offender):
								timeNow=time.asctime( time.localtime(time.time()) )
								self.offender[I]=[timeNow,N]
							print(name,proba)
						text = "{}: {:.2f}%".format(name, proba * 100)
				# else:
				# 	name='Unknown'
				# 	proba=1.0-proba

				# text = "{}: {:.2f}%".format(name, proba * 100)
				y = startY - 10 if startY - 10 > 10 else startY + 10
				cv2.rectangle(frame1, (startX, startY), (endX, endY),
					(0, 0, 255), 2)
				cv2.putText(frame1, text, (startX, y),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
		return frame1

	def stop(self):
		cv2.destroyAllWindows()
		time.sleep(0.5)
		#if camera
		# self.vs.stream.release()
		#if camera

		#if video
		self.vs.release()
		#video


	def start(self):
		print("Camera starting...")
			#if camera played
		# self.vs = VideoStream(src=0).start()
			#if camera played
		
		#if video played
		self.vs=cv2.VideoCapture(os.path.join(os.path.dirname(__file__),'RealVideo','vid5.mp4'))
		#if video played
		print('Camera started')
		print(self.d)

	def details_offender(self):
		return self.offender

	def delete_offender(self,data):
		if(data in self.offender):
			del self.offender[data]


