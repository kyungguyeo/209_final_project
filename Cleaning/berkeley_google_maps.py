import json
businesses = {}
with open('yelp_academic_dataset.json') as datafile:
	for i in datafile:	
		data = json.loads(i)
		if data['type']=='business' and "University of California at Berkeley" in data['schools']:
			businesses[data['business_id']]=data
with open('berkeley_businesses.json', 'w') as f:
	json.dump(businesses,f)
