import pymongo

client = pymongo.MongoClient('localhost',27017)
database = client['database']
form = database['form']
'''
with open('walden.txt') as f:
    lines = f.readlines()
    for line,strings in enumerate(lines):
        data = {
            'line':line,
            'strings':strings,
            'words':len(strings.strip()),
        }
        form.insert_one(data)
'''
for line,data in enumerate(form.find({'line':{'$lte':5}})):
    print(data)