###Conditional Lists: Perform the following tasks to mimic how a website ensures everyone has a unique username.
#1.	Create a list named web_users that contains five or more user names.  
web_users = ["wolverine", "storm", "cyclops", "jeangrey", "beast"]
#2.	Create a second list with another five user names called new_users.  Ensure that two user names in new_users also exist in web_users, but the other three do not.
new_users = ["wolverine", "storm", "magneto", "professor x", "nightcrawler"]
##3. Create a loop to check if each user name in new_users has already been used in web_users. If the user name exists in both lists, print the message: 
#This user name is already in use. Please choose a different user name.
for user in new_users:
    if user.lower() in web_users:
        print(f"{user}: This user name is already in use. Please choose a different user name.")
#If the user name does not already exist, print the message: #This user name is available.
    else: 
        print(f"{user}: This user name is available.")


### Nested Dictionaries:
#1.	Create a new dictionary called cities.  Plan to use three distinct city names as keys in your dictionary.
#2.	For each city, create a dictionary that includes:
    #a.	The key country that specifies the country the city is in.
    #b.	The key population that includes the approximate population as an integer.
    #c.	The key fact that specifies one fact about the city.
#3.	Add each of these cities to the original dictionary cities.
#4.	Print the information in the following format:
#City: <Name>
	#Country: <Name>
	#Population: <Count>
	#Fact: <A fact about the city.>
#City: <Name>
	#Country: <Name>
	#Population: <Count>
	#Fact: <A fact about the city.>
#City: <Name>
	#Country: <Name>
	#Population: <Count>
	#Fact: <A fact about the city.>#

cities = {
    "dublin": {
        "country": "Ireland",
        "population": 592000,
        "fact": "The Guinness Storehouse and Trinity College are located in Dublin. Vikings founded Dublin in the 9th century as a settlement called 'Dubh Linn', meaning 'black pool'."
    },
    "cork": {
        "country": "Ireland",
        "population": 224000,
        "fact": "Blarney Castle contains the Blarney Stone or Stone of Eloquence, which visitors kiss while hanging upside down to receive the 'gift of gab'."
    },
    "galway": {
        "country": "Ireland",
        "population": 83000,
        "fact": "Galway is considered the cultural heart of Ireland and has one of the highest percentages of Irish language speakers in an urban area. Galway has a fantastic Arts Festival and trad music scene."
    }
}

for city, info in cities.items():
    print(f"City: {city.title()}")
    print(f"\tCountry: {info['country']}")
    print(f"\tPopulation: {info['population']}")
    print(f"\tFact: {info['fact']}")


