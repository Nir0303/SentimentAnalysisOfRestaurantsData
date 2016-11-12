import requests
import json
import pprint
#data= requests.get("http://api.tripadvisor.com/api/partner/2.0/map/42.729164,-73.678503/restaurants?key=b245d5db-8cc1-4cb9-a499-90602105b49b")
data=requests.get("http://api.tripadvisor.com/api/partner/2.0/location/48739/restaurants?key=b245d5db-8cc1-4cb9-a499-90602105b49b")
#print data.text

#print data.text
pp = pprint.PrettyPrinter(indent=4)

jsonData= json.loads(data.text)
#pp.pprint(jsonData["data"][0])
outfile="resturantReviews.csv"
f=open(outfile,'w')
f.write("name~location_id~city~state~awards~ReviewText~uName~uLocation")
f.write('\n')
for  i in  jsonData["data"]:
	try:
		name,location_id,city,state,awards=i["name"],i["location_id"] ,i["address_obj"]["city"],i["address_obj"]["state"],i["awards"][0]["display_name"]
	except:
		pass
	restaurantReview= "http://api.tripadvisor.com/api/partner/2.0/location/{}/reviews?key=b245d5db-8cc1-4cb9-a499-90602105b49b".format(location_id)
	#print restaurantReview
	reviewData=requests.get(restaurantReview)
	reviewJson=json.loads(reviewData.text)
	
	#pp.pprint(reviewJson["data"])
	for j in reviewJson["data"]:
		ReviewText,uName,uLocation= j["text"],j["user"]["username"],j["user"]["user_location"]["name"]
		try:
			s=name+'~'+location_id+'~'+city+'~'+state+'~'+awards+'~'+ReviewText.replace('\n',' ')+'~'+uName+'~'+uLocation
			f.write(s)
			f.write('\n')
		except:
			pass
		
		#f.write(s)
f.close()	
encoder = json.JSONEncoder()


"""
for i in encoder.iterencode(data.text):
	print i
	break
"""