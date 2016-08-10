'''
Created by cpowers
cjpowers3@gmail.com
This is a simple code that pulls a recipie or food item from the top scoring links
page of /r/vegRecipes.
'''

import webbrowser, sys, bs4, requests, time
import numpy as np

def get_Recipe():
    res = requests.get('https://re.reddit.com/r/VegRecipes/top/?sort=top&t=all')
    vegSoup = bs4.BeautifulSoup(res.text)

    badResponse = "[<title>Too Many Requests</title>]"
    #reddit sends out a particular page when it gets too many requests in
    #a certain timeframe. This logic gets through it.
    # We must reinitialize the res and vegSoup with the appropriate webpage, rather than
    # reddit's response page.
    if str(vegSoup.select('title')) == badResponse:
        print("The reddit overlords have found us, we must wait a few seconds.")
        time.sleep(3)
        res = requests.get('https://re.reddit.com/r/VegRecipes/top/?sort=top&t=all')
        vegSoup = bs4.BeautifulSoup(res.text)

    recipes = vegSoup.select('.outbound')
    randomN = np.random.random_integers(0, len(recipes)-1)
    randomRecipe = recipes[randomN]
    link = randomRecipe.get('href')
    webbrowser.open(link)
