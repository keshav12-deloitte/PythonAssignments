sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
#---creating  a new key value and storing with city key value and deleting th key value---
# sampleDict["location"]=sampleDict["city"]
# del sampleDict["city"]
#----using pop for deleting the key city before that storing the value of key----
sampleDict["location"]=sampleDict.pop("city")

print(sampleDict)