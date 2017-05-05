from django.db import models
import pymongo

client = pymongo.MongoClient('localhost',27017)
test_database1 = client['test_database1']
CV1 = test_database1['CV1']
finds = list(CV1.find())
finds_20 = finds[:20]
