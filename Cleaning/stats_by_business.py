import json, collections

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

cat_ref = ['Food', 'Bagels', 'Bakeries', 'Beer, Wine & Spirits', 'Breweries', 'Bubble Tea', 'Butcher', 'CSA', 'Coffee & Tea', 'Convenience Stores', 'Desserts', 'Do-It-Yourself Food', 'Donuts', 'Farmers Market', 'Food Delivery Services', 'Food Trucks', 'Gelato', 'Grocery', 'Ice Cream & Frozen Yogurt', 'Internet Cafes', 'Juice Bars & Smoothies', 'Pretzels', 'Shaved Ice', 'Specialty Food', 'Candy Stores', 'Cheese Shops', 'Chocolatiers & Shops', 'Ethnic Food', 'Fruits & Veggies', 'Health Markets', 'Herbs & Spices', 'Meat Shops', 'Seafood Markets', 'Street Vendors', 'Tea Rooms', 'Wineries', 'Afghan', 'African', 'American (New)', 'American (Traditional)', 'Arabian', 'Argentine', 'Armenian', 'Asian Fusion', 'Australian', 'Austrian', 'Bangladeshi', 'Barbeque', 'Basque', 'Belgian', 'Brasseries', 'Brazilian', 'Breakfast & Brunch', 'British', 'Buffets', 'Burgers', 'Burmese', 'Cafes', 'Cafeteria', 'Cajun/Creole', 'Cambodian', 'Caribbean', 'Catalan', 'Cheesesteaks', 'Chicken Wings', 'Chinese', 'Comfort Food', 'Creperies', 'Cuban', 'Czech', 'Delis', 'Diners', 'Ethiopian', 'Fast Food', 'Filipino', 'Fish & Chips', 'Fondue', 'Food Court', 'Food Stands', 'French', 'Gastropubs', 'German', 'Gluten-Free', 'Greek', 'Halal', 'Hawaiian', 'Himalayan/Nepalese', 'Hot Dogs', 'Hot Pot', 'Hungarian', 'Iberian', 'Indian', 'Indonesian', 'Irish', 'Italian', 'Japanese', 'Korean', 'Kosher', 'Laotian', 'Latin American', 'Live/Raw Food', 'Malaysian', 'Meditteranean', 'Mexican', 'Middle Eastern', 'Modern European', 'Mongolian', 'Pakistani', 'Persian/Iranian', 'Peruvian', 'Pizza', 'Polish', 'Portuguese', 'Russian', 'Salad', 'Sandwiches', 'Scandinavian', 'Scottish', 'Seafood', 'Singaporean', 'Slovakian', 'Soul Food', 'Soup', 'Southern', 'Spanish', 'Steakhouses', 'Sushi Bars', 'Taiwanese', 'Tapas Bars', 'Tapas/Small Plates', 'Tex-Mex', 'Thai', 'Turkish', 'Ukranian', 'Vegan', 'Vegetarian', 'Vietnamese', 'Columbian', 'Salvadoran', 'Venezuelan', 'Egyptian', 'Lebanese', 'Dominican', 'Haitian', 'Puerto Rican', 'Trinidadian', 'Cantonese', 'Dim Sum', 'Shanghainese', 'Szechuan', 'Senegalese', 'South African', 'Restaurants'
]

#average review for each business
rev_by_biz = {}
businesses = {}
with open('/Users/johnnyyeo/Documents/MIDS/w209/209_final_project/209_FinalProject_Data/yelp_academic_dataset.json') as datafile:
	for i in datafile:
		data = json.loads(i)
		if data['type']=='business' and data['review_count'] > 15:
			good_cats = [x for x in data['categories'] if x in cat_ref]
			if good_cats:
				businesses[data['business_id']] = data
		elif data['type'] == 'review':
			if not rev_by_biz.get(data['business_id']):
				rev_by_biz[data['business_id']] = {'review':0, 'count':0}
				rev_by_biz[data['business_id']]['review'] += data['stars']
				rev_by_biz[data['business_id']]['count'] += 1
			else:
				rev_by_biz[data['business_id']]['review'] += data['stars']
				rev_by_biz[data['business_id']]['count'] += 1
averages = 0
counts = 0
for biz in rev_by_biz:
	averages += rev_by_biz[biz]['review']
	counts += rev_by_biz[biz]['count']
averages = round(averages*1.0/counts,2)

#average review for each campus
with open('/Users/johnnyyeo/Documents/MIDS/w209/209_final_project/209_FinalProject_Data/campus_star_stats.json') as datafile:
	for i in datafile:
		data = json.loads(i)
		revs_by_campus = data

#average review for each category
rev_by_cat = {}
for cats in cat_ref:
	rev_by_cat[cats] = {'reviews':0, 'count':0}
for biz in businesses:
	for cat in businesses[biz]['categories']:
		if cat in cat_ref:
			rev_by_cat[cat]['reviews'] += businesses[biz]['stars']
			rev_by_cat[cat]['count'] += 1
for cat in rev_by_cat:
	if rev_by_cat[cat]['reviews'] == 0:
		rev_by_cat[cat]['average'] = 0
	else:
		rev_by_cat[cat]['average'] = round(rev_by_cat[cat]['reviews']*1.0/rev_by_cat[cat]['count'],2)



final_rev = {}
for biz in rev_by_biz:
	if businesses.get(biz):
		for cat in businesses[biz]['categories']:
			if cat in cat_ref:
				cat_marker = rev_by_cat[cat]['average']
		final_rev[biz] = [
			{"title": "All Businesses", "subtitle": str(round(rev_by_biz[biz]['review']*1.0/rev_by_biz[biz]['count'],2)) + " vs " + str(averages), "ranges": [5], "measures": [rev_by_biz[biz]['review']*1.0/rev_by_biz[biz]['count']], "markers": [averages]},
			{"title": "All Campus", "subtitle": str(round(rev_by_biz[biz]['review']*1.0/rev_by_biz[biz]['count'],2)) + " vs " + str(revs_by_campus[campus_key[businesses[biz]['schools'][0]]][0]['measures'][0]), "ranges": [5], "measures": [rev_by_biz[biz]['review']*1.0/rev_by_biz[biz]['count']], "markers": revs_by_campus[campus_key[businesses[biz]['schools'][0]]][0]['markers']},
			{"title": "Category (" + str(businesses[biz]['categories'][0]) + ")", "subtitle": str(round(rev_by_biz[biz]['review']*1.0/rev_by_biz[biz]['count'],2)) + " vs " + str(cat_marker), "ranges": [5], "measures": [rev_by_biz[biz]['review']*1.0/rev_by_biz[biz]['count']], "markers": [cat_marker]}
			]

with open('/Users/johnnyyeo/Documents/MIDS/w209/209_final_project/209_FinalProject_Data/stats_by_business.json', 'w') as f:
	json.dump(final_rev,f)
with open('/Users/johnnyyeo/Documents/MIDS/w209/judofighter25.github.io/209_FinalProject_Data/rev_by_biz.json', 'w') as f:
	json.dump(rev_by_biz,f)