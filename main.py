import cv2
import argparse
from read import *

def main():
	cam = cv2.VideoCapture(0)
	while True:
		ret, frame = cam.read()
		cv2.imshow('frame',frame)
		read_qr(frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	cam.release()
	cv2.destroyAllWindows()



if __name__ == "__main__":
	main()

#AIzaSyD6HrwbplASXSVexdZXvfbewCUybMEnxPE