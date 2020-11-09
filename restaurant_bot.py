# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 22:08:18 2020

@author: rajvi.shah
"""

#importing libraries
import requests #to request data using zomato api
from autocorrect import Speller #to correct spelling to user's response - location and cuisine
import random #to select greeting response



#zomato code to get an access to use Zomato API
zomato_api = 'ZOMATO_ACCESS_CODE'

#function to get location details using zomato api
def get_location_details(query):

    headers = {
        'Accept': 'application/json',
        'user-key': zomato_api,
    }
    
    params = (
        ('query', query),
    )
    
    #requesting to get location details
    response = requests.get('https://developers.zomato.com/api/v2.1/locations', headers=headers, params=params)
    
    #converting response (class 'function') to json
    data = response.json()

    #to take location details - entity id and type from the collected data
    for loc in data['location_suggestions']:
        loc_id = loc['entity_id']
        loc_type = loc['entity_type']
        
    return loc_id, loc_type

#function to get restaurants id and type
def get_restaurants(ent_id, ent_type):

    headers = {
        'Accept': 'application/json',
        'user-key': zomato_api,
    }

    params = (
        ('entity_id', ent_id),
        ('entity_type', ent_type),
    )

    response = requests.get('https://developers.zomato.com/api/v2.1/search', headers=headers, params=params)

    return response.json()



#function to response a greeting to user
def greeting(sentence):
    # Keyword Matching
    greeting_inputs = ("hello", "hi", "greetings", "sup", "what's up","hey",)
    greeting_responses = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]

    """If user's input is a greeting, return a greeting response"""
    for word in sentence.split():
        if word.lower() in greeting_inputs:
            return random.choice(greeting_responses)
        

#function to suggest restaurants name and details based on location and cuisines preference        
def response():
    
    #taking input of location and cuisine(s) from the user
    prompt = '> '
    print('Enter location to search:')
    location = input(prompt)
    print()
    print('Enter cuisines (seperated by comma to search):')
    cuisines = input(prompt).split(' ')
    print()
    
    #to check spelling of location and cuisine(s)
    spell = Speller(lang = 'en')
    location = spell(location)
    
    new_cuisines = []
    for cui in cuisines:
        new_cui = spell(cui)
        new_cuisines.append(new_cui)
    
    #print(new_cuisines)
    #print(location)
    
    #calling functions - to get location and restaurants details
    entity_id, entity_type = get_location_details(location)
    data = get_restaurants(entity_id, entity_type)
    
    #print(data)
    
    print("Restaurants in " + location.title() + " --\n")
    #print(data['restaurants'])
    
   
    for restaurant in data['restaurants']:
        r = restaurant['restaurant']



        
        loc = r['location']

        
        rating = r['user_rating']

        
        cuisine = r['cuisines']

        #print(cuisine)
        for cui1 in new_cuisines:
            #print(cui1)
            cui1 = cui1.lower()

            
            if cui1 in cuisine.lower():
            
                
                print(r['name'].upper())
    
           
                print("Address - " + loc['address'])
        
                print("Rating - " + str(rating['aggregate_rating']))
            
                print("Cuisines - " + cuisine)
                
                print("More Details - "  + r['url'])
                
                
                break
            #else:
                #print('Please enter other nearby location or cuisine(s)...')
               # response()
if __name__=="__main__":               
    flag = True
    
    print("My name is foodie. I will suggest you restaurants based on location and cuisines. If you want to exit, type Bye!")
    print()
    print('Enter yes for restaurant suggestions!')
    
    while(flag == True):
        
        user_response = input()
        user_response = user_response.lower()
    
        
        if(user_response != 'bye' or user_response != 'bye!'):
        
            if(user_response == 'thanks' or user_response == 'thank you' ):
            
                flag = False
                
                print("You are welcome! Have a nice day.")
            
            elif (user_response == 'yes'):
                response()
                flag = False
            
            else:
                
                if(greeting(user_response) != None):
                
                    print(greeting(user_response))
                else:
                    print("I'm sorry. I don't understand you!")
        else:
            
            flag = False
            print("Bye! take care..")           
