import json
campus_key = {
	'University of Michigan - Ann Arbor':'umich',
	'University of Pennsylvania':'penn',
	'Harvard University':'harvard',
	'University of California at Berkeley':'cal',
	'University of Massachusetts - Amherst':'umass',
	'Virginia Tech':'vt',
	'University of North Carolina - Chapel Hill':'unc',
	'University of Washington':'uw',
	'University of Texas - Austin':'utt',
	'University of Southern California':'usc',
	'University of California - Los Angeles':'ucla',
	'University of California - San Diego':'ucsd',
	'University of Illinois - Urbana-Champaign':'ill',
	'Purdue University':'purdue',
	'Princeton University':'princeton',
	'Massachusetts Institute of Technology':'mit',
	'Harvey Mudd College':'harveymudd',
	'Stanford University':'stanford',
	'Carnegie Mellon University':'carnegie',
	'Columbia University':'columbia',
	'Cornell University':'cornell',
	'Georgia Institute of Technology':'gt',
	'Rice University':'rice',
	'Rensselaer Polytechnic Institute':'rensselaer',
	'Brown University':'brown',
	'California Institute of Technology':'caltech',
	'California Polytechnic State University':'cp',
	'University of Maryland - College Park':'maryland',
	'University of Waterloo':'waterloo',
	'University of Wisconsin':'wisconsin'
}

cat_ref = ['Food', 'Bagels', 'Bakeries', 'Beer, Wine & Spirits', 'Breweries', 'Bubble Tea', 'Butcher', 'CSA', 'Coffee & Tea', 'Convenience Stores', 'Desserts', 'Do-It-Yourself Food', 'Donuts', 'Farmers Market', 'Food Delivery Services', 'Food Trucks', 'Gelato', 'Grocery', 'Ice Cream & Frozen Yogust', 'Internet Cafes', 'Juice Bars & Smoothies', 'Pretzels', 'Shaved Ice', 'Specialty Food', 'Candy Stores', 'Cheese Shops', 'Chocolatiers & Shops', 'Ethnic Food', 'Fruits & Veggies', 'Health Markets', 'Herbs & Spices', 'Meat Shops', 'Seafood Markets', 'Street Vendors', 'Tea Rooms', 'Wineries', 'Afghan', 'African', 'American (New)', 'American (Traditional)', 'Arabian', 'Argentine', 'Armenian', 'Asian Fusion', 'Australian', 'Austrian', 'Bangladeshi', 'Barbeque', 'Basque', 'Belgian', 'Brasseries', 'Brazilian', 'Breakfast & Brunch', 'British', 'Buffets', 'Burgers', 'Burmese', 'Cafes', 'Cafeteria', 'Cajun/Creole', 'Cambodian', 'Caribbean', 'Catalan', 'Cheesesteaks', 'Chicken Wings', 'Chinese', 'Comfort Food', 'Creperies', 'Cuban', 'Czech', 'Delis', 'Diners', 'Ethiopian', 'Fast Food', 'Filipino', 'Fish & Chips', 'Fondue', 'Food Court', 'Food Stands', 'French', 'Gastropubs', 'German', 'Gluten-Free', 'Greek', 'Halal', 'Hawaiian', 'Himalayan/Nepalese', 'Hot Dogs', 'Hot Pot', 'Hungarian', 'Iberian', 'Indian', 'Indonesian', 'Irish', 'Italian', 'Japanese', 'Korean', 'Kosher', 'Laotian', 'Latin American', 'Live/Raw Food', 'Malaysian', 'Meditteranean', 'Mexican', 'Middle Eastern', 'Modern European', 'Mongolian', 'Pakistani', 'Persian/Iranian', 'Peruvian', 'Pizza', 'Polish', 'Portuguese', 'Russian', 'Salad', 'Sandwiches', 'Scandinavian', 'Scottish', 'Seafood', 'Singaporean', 'Slovakian', 'Soul Food', 'Soup', 'Southern', 'Spanish', 'Steakhouses', 'Sushi Bars', 'Taiwanese', 'Tapas Bars', 'Tapas/Small Plates', 'Tex-Mex', 'Thai', 'Turkish', 'Ukranian', 'Vegan', 'Vegetarian', 'Vietnamese', 'Columbian', 'Salvadoran', 'Venezuelan', 'Egyptian', 'Lebanese', 'Dominican', 'Haitian', 'Puerto Rican', 'Trinidadian', 'Cantonese', 'Dim Sum', 'Shanghainese', 'Szechuan', 'Senegalese', 'South African', 'Restaurants'
]

businesses = {}
with open('/Users/johnnyyeo/Documents/MIDS/w209/209_final_project/209_FinalProject_Data/yelp_academic_dataset.json') as datafile:
	for i in datafile:
		data = json.loads(i)
		if data['type']=='business':
			good_cats = [x for x in data['categories'] if x in cat_ref]
			if good_cats:
				for school in data['schools']:
					if not businesses.get(campus_key[school]):
						businesses[campus_key[school]] = {}
						businesses[campus_key[school]][data['business_id']] = data
					else:
						businesses[campus_key[school]][data['business_id']] = data
with open('/Users/johnnyyeo/Documents/MIDS/w209/209_final_project/209_FinalProject_Data/food_businesses_by_campus.json', 'w') as f:
	json.dump(businesses,f)