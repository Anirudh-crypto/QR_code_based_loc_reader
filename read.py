import cv2
from geopy.geocoders import Nominatim
from datetime import datetime
import json
import urllib.request

def read_qr(frames):
	try:
		reader = cv2.QRCodeDetector()
		value, points, straight_qrcode = reader.detectAndDecode(frames)
		maps(value)
	except:
		return


def maps(loc):

	geoloc = Nominatim(user_agent="QRcode based reader")

	loc = loc.replace("'",'"')

	des = geoloc.geocode(loc)

	print(des.latitude,des.longitude)





