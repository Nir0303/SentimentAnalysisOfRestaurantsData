import requests
import json
import pprint
outfile="restaurantReviews.csv"
cityData={'troy':48739,'New York City':60763,'Boston MA':60745,'Jersey City NJ':46531,'Chicago IL':35805,'Albnay NY':29786,'Utica NY':48759,'Syracuse NY':48713,'Phily':60795,'Washington DC':28970,'Los Angeles':32655,'Seattle': 60878,'sandiego': 56612,'Phoenix': 31310,'portland oregon':52024,'oakland': 3281}
f=open(outfile,'a')
f.write("name~location_id~city~state~awards~ReviewText~uName~uLocation")
f.write('\n')
a=[]
#data= requests.get("http://api.tripadvisor.com/api/partner/2.0/map/42.729164,-73.678503/restaurants?key=b245d5db-8cc1-4cb9-a499-90602105b49b")
for c in cityData:
	url="http://api.tripadvisor.com/api/partner/2.0/location/{}/restaurants?key=b245d5db-8cc1-4cb9-a499-90602105b49b".format(cityData[c])
	data=requests.get(url)
	#print data.text

	#print data.text
	pp = pprint.PrettyPrinter(indent=4)

	jsonData= json.loads(data.text)
	#pp.pprint(jsonData["data"][0])
	
	try:
		for  i in  jsonData["data"]:
			try:
				name,location_id,city,state,awards=i["name"],i["location_id"] ,i["address_obj"]["city"],i["address_obj"]["state"],i["awards"][0]["display_name"]
			except:
				pass
			restaurantReview= "http://api.tripadvisor.com/api/partner/2.0/location/{}/reviews?key=b245d5db-8cc1-4cb9-a499-90602105b49b".format(location_id)
			reviewData=requests.get(restaurantReview)
			reviewJson=json.loads(reviewData.text)
			for j in reviewJson["data"]:
				ReviewText,uName,uLocation= j["text"],j["user"]["username"],j["user"]["user_location"]["name"]
				try:
					s=name+'~'+location_id+'~'+city+'~'+state+'~'+awards+'~'+ReviewText.replace('\n',' ')+'~'+uName+'~'+uLocation
					a.append(s)
				except:
					pass
		print c,len(a),cityData[c]
				
				#f.write(s)
	except:
		pass

a=list(set(a))
a.sort()
for i in range(len(a)):
	try:
		f.write(a[i])
		f.write('\n')
	except:
		pass
f.close()	


"""
for i in encoder.iterencode(data.text):
	print i
	break
"""