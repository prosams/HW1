import requests
import json
import html

# baseurl = "https://od-api.oxforddictionaries.com:443/api/v1/entries/en/ace/synonyms"
#
# params_diction = {}
# # params_diction["Accept"] = "application/json"
# params_diction["app_id"] = "aa397b2c"
# params_diction["app_key"] = "9a8c2f87bb0e376774a74f1763331be7"
# print(params_diction)
# fullurl = baseurl + "eat"
# makereq = requests.get(fullurl, params=params_diction)
# print(makereq.url)

# print(params_diction)
# print(makereq)


searchterm = "Luke"
baseurl = "https://swapi.co/api/people/?"
params_diction = {}
params_diction["search"] = searchterm
makereq = requests.get(baseurl, params = params_diction)

txt = makereq.text
python_obj = json.loads(txt)
print(python_obj)

pname = python_obj['results'][0]["name"]
phair = python_obj['results'][0]["hair_color"]
pgender = python_obj['results'][0]["gender"]
pworld = python_obj['results'][0]["homeworld"]
print(phair)
print(pgender)
print(pworld)


print(makereq)
