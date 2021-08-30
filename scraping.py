from facebook_scraper import get_posts
import locale

locale.setlocale(locale.LC_ALL , 'en_US')
page = "africacdc"
listposts = []
for post in get_posts(page, pages=3,options={'comments': True}):
    print(post['text'][:50])
    listposts.append(post)

print("Start..")
file_name = page+".txt"
with open(file_name, 'w', encoding='utf-8') as f:
    f.write(str(listposts))
f.close()
#f = open(file_name, "a")


print("Finish..")