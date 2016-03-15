###Parses json file and creates a business, review, and user datafile, and
###parses only for restaurants.

import json

businesses = {}
reviews = {}
users = {}

cat_ref = ['Food', 'Bagels', 'Bakeries', 'Beer, Wine & Spirits', 'Breweries', 'Bubble Tea', 'Butcher', 'CSA', 'Coffee & Tea', 'Convenience Stores', 'Desserts', 'Do-It-Yourself Food', 'Donuts', 'Farmers Market', 'Food Delivery Services', 'Food Trucks', 'Gelato', 'Grocery', 'Ice Cream & Frozen Yogust', 'Internet Cafes', 'Juice Bars & Smoothies', 'Pretzels', 'Shaved Ice', 'Specialty Food', 'Candy Stores', 'Cheese Shops', 'Chocolatiers & Shops', 'Ethnic Food', 'Fruits & Veggies', 'Health Markets', 'Herbs & Spices', 'Meat Shops', 'Seafood Markets', 'Street Vendors', 'Tea Rooms', 'Wineries', 'Afghan', 'African', 'American (New)', 'American (Traditional)', 'Arabian', 'Argentine', 'Armenian', 'Asian Fusion', 'Australian', 'Austrian', 'Bangladeshi', 'Barbeque', 'Basque', 'Belgian', 'Brasseries', 'Brazilian', 'Breakfast & Brunch', 'British', 'Buffets', 'Burgers', 'Burmese', 'Cafes', 'Cafeteria', 'Cajun/Creole', 'Cambodian', 'Caribbean', 'Catalan', 'Cheesesteaks', 'Chicken Wings', 'Chinese', 'Comfort Food', 'Creperies', 'Cuban', 'Czech', 'Delis', 'Diners', 'Ethiopian', 'Fast Food', 'Filipino', 'Fish & Chips', 'Fondue', 'Food Court', 'Food Stands', 'French', 'Gastropubs', 'German', 'Gluten-Free', 'Greek', 'Halal', 'Hawaiian', 'Himalayan/Nepalese', 'Hot Dogs', 'Hot Pot', 'Hungarian', 'Iberian', 'Indian', 'Indonesian', 'Irish', 'Italian', 'Japanese', 'Korean', 'Kosher', 'Laotian', 'Latin American', 'Live/Raw Food', 'Malaysian', 'Meditteranean', 'Mexican', 'Middle Eastern', 'Modern European', 'Mongolian', 'Pakistani', 'Persian/Iranian', 'Peruvian', 'Pizza', 'Polish', 'Portuguese', 'Russian', 'Salad', 'Sandwiches', 'Scandinavian', 'Scottish', 'Seafood', 'Singaporean', 'Slovakian', 'Soul Food', 'Soup', 'Southern', 'Spanish', 'Steakhouses', 'Sushi Bars', 'Taiwanese', 'Tapas Bars', 'Tapas/Small Plates', 'Tex-Mex', 'Thai', 'Turkish', 'Ukranian', 'Vegan', 'Vegetarian', 'Vietnamese', 'Columbian', 'Salvadoran', 'Venezuelan', 'Egyptian', 'Lebanese', 'Dominican', 'Haitian', 'Puerto Rican', 'Trinidadian', 'Cantonese', 'Dim Sum', 'Shanghainese', 'Szechuan', 'Senegalese', 'South African', 'Restaurants'
]



with open('/Users/johnnyyeo/Documents/MIDS/w209/209_FinalProject_Data/yelp_academic_dataset.json') as datafile:
    for i in datafile:
        data = json.loads(i)
        if data['type']=='business':
            good_cats = [x for x in data['categories'] if x in cat_ref]
            if good_cats:
                businesses[data['business_id']]=data
        elif data['type']=='review':
            reviews[data['business_id']+data['user_id']]=data
        elif data['type']=='user':
            users[data['user_id']]=data

with open('/Users/johnnyyeo/Documents/MIDS/w209/209_FinalProject_Data/yelp_businesses_food_only.json', 'w') as f:
    json.dump(businesses,f)

with open('/Users/johnnyyeo/Documents/MIDS/w209/209_FinalProject_Data/yelp_reviews.json', 'w') as f:
    json.dump(reviews,f)

with open('/Users/johnnyyeo/Documents/MIDS/w209/209_FinalProject_Data/yelp_users.json', 'w') as f:
    json.dump(users,f)