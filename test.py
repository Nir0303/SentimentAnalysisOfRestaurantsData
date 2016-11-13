import requests
import json
import pprint
restaurantReview= "http://api.tripadvisor.com/api/partner/2.0/location/5777687/reviews?key=b245d5db-8cc1-4cb9-a499-90602105b49b".format(5777687)
reviewData=requests.get(restaurantReview)
reviewJson=json.loads(reviewData.text)
cnt=0
for j in reviewJson["data"]:
			#print(len(j))
			
			ReviewText,uName,uLocation= j["text"],j["user"]["username"],j["user"]["user_location"]["name"]
			cnt+=1
			print uName,uLocation
print cnt
