import json
from namuwiki.extractor import extract_text

with open('namu.json', 'r', encoding='utf-8') as input_file:
    namu_wiki = json.load(input_file)
f=open('namu.txt','wb')


for document in namu_wiki:
# document = namu_wiki[1]
    plain_text = extract_text(document['text'])
    f.write(plain_text.encode())

f.close()