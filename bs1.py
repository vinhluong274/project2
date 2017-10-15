import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
url = "/Users/vinhluong/Desktop/206project2/opinion.html"
soup = BeautifulSoup(open(url), 'html.parser')# Retrieve all of the anchor tags
# tags = soup('ol')
# print(soup.findAll('ol'))
# print(tags.find('a')
# for tag in tags:
	# print()
ol_tag = soup.ol
for child in ol_tag.children:
	anchor = child.next_sibling
	print(anchor)

print(type(anchor))




# print(soup.ol.li.a)

# for i in soup.findAll('ol'):
	# print(i.descendents)
