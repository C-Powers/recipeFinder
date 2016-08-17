'''
Created by cpowers
cjpowers3@gmail.com
This is a simple code that pulls a recipie or food item from the top scoring links
page of /r/vegRecipes.
'''

import webbrowser, sys, bs4, requests, time
import numpy as np

def scrapeSite():
    url = 'https://re.reddit.com/r/VegRecipes/top/?sort=top&t=all'
    header = {'Accept-Encoding': 'gzip, deflate, sdch',
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
              'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}
    res = requests.get(url, headers = header)
    if res.status_code == 200:
        print("status code 200!!!")
        return res
    else:
        return

def get_Recipe():
    request = scrapeSite()
    for i in range(0, 5):
        if request == None:
            print("failed to scrape site, trying again. Try" + i + "/4")
            time.sleep(3)
            scrapeSite()
        else:
            pass

    vegSoup = bs4.BeautifulSoup(request.text, "html.parser")
    recipes = vegSoup.select('.outbound')
    randomN = np.random.random_integers(0, len(recipes)-1)
    randomRecipe = recipes[randomN]
    link = randomRecipe.get('href')
    print('link', link)
    return link
