import cv2
import googlemaps
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

	# print(loc)

	apiKey = 'AjB9pn6eHrLFjt1njE1KBI8VIKZp8PW339kjtVFNjqZB9yu8NnN_ApJDJQRAq8qk'

	encodedLoc = urllib.parse.quote(loc,safe='')

	# src = geocoder.bing('me',key = apiKey)

	# print(src)

	# input()

	# des = geocoder.bing(encodedLoc,key = apiKey)

	# print(des)

	#route = http://dev.virtualearth.net/REST/V1/Routes?wp.0=37.779160067439079,-122.42004945874214&wp.1=32.715685218572617,-117.16172486543655&key=apiKey

	json_data = "http://dev.virtualearth.net/REST/v1/Locations?countryRegion=IN"+encodedLoc+"&key="+apiKey

	request_url = urllib.request.Request(json_data)

	response_data = urllib.request.urlopen(request_url)

	r = response_data.read().decode(encoding="utf-8")
	
	result = json.loads(r)

	print(result)

	input()

	# maps = googlemaps.Client(key="AIzaSyD6HrwbplASXSVexdZXvfbewCUybMEnxPE")

	# print(maps)

	# time = datetime.now()

	# geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

	# #direction = gmaps.directions(loc,mode='transit',departure_time=time)

	# print(geocode_result)


