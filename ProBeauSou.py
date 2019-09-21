
from bs4 import BeautifulSoup
import requests

result = requests.get("https://www.allrecipes.com/recipes/17235/everyday-cooking/allrecipes-magazine-recipes/")
print(result.status_code)
# print(result.headers)

src = result.content
soup = BeautifulSoup(src, features="html.parser")

urls = []
for h3_tag in soup.find_all("h3"):
    a_tag = h3_tag.find('a')
    # print(a_tag)
    if a_tag is not None:
        # print(a_tag)
        # print(a_tag.attrs['href'])
        urls.append(f"{a_tag.attrs['href']}")
        # urls.append(a_tag.attrs['href'])
        # print(a_tag.span)

print(urls)


print("\n-----\n")

n = 1
for url in urls:
    result2 = requests.get(url)
    # print(result2.status_code)
    src2 = result2.content
    soup2 = BeautifulSoup(src2, features="html.parser")
    recipe_name = soup.find_all("h1")
    print(recipe_name)

# urls.append(a_tag.attrs['href'])urls = []
# print(spans)

# for a_tag in soup.find_all("a"):
#     span = a_tag.find('span')
#     print(span)
#     #urls.append(a_tag.attrs['href'])

#print(urls)

# links = soup.find_all("a")
# links = soup.find_all("h3")
# print(links)

# spans = soup.find_all("span")

# for link in links:
#     #if "span" in link.text:
#         #print(link)
#         print(link.attrs)

# for span in spans:
#     if "Million" in span.text:
#         print(span.attrs)

