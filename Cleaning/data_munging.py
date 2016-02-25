import json

businesses = {}
reviews = {}
users = {}


with open('yelp_academic_dataset.json') as datafile:
	for i in datafile:	
		data = json.loads(i)
		if data['type']=='business':
			businesses[data['business_id']]=data
		elif data['type']=='review':
			reviews[data['business_id']+data['user_id']]=data
		elif data['type']=='user':
			users[data['user_id']]=data

with open('yelp_businesses.json', 'w') as f:
	json.dump(businesses,f)

with open('yelp_reviews.json', 'w') as f:
	json.dump(reviews,f)

with open('yelp_users.json', 'w') as f:
	json.dump(users,f)