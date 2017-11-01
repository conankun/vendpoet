import urllib.request,json

# parse authors list

f = open('authors.json', 'r')
json_authors = f.readlines()
json_authors_str = ""
for line in json_authors:
	json_authors_str += line
f.close();

data_authors = json.loads(json_authors_str)

for author in data_authors['authors']:
	author = author.replace(" ", "%20")
	url = "http://poetrydb.org/author/"+author+"/title"
	print (url)
	response = urllib.request.urlopen(url)
	author = author.replace("%20", "_")
	f = open('poem/'+author+'.json', 'w')
	f.write(response.read().decode())
	f.close()
	