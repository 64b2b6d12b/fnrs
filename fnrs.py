"""Food Network recipe scraper"""
from requests import get
from bs4 import BeautifulSoup as bs
from json import loads


def scraper(url):
    """Downloads the web page using Requests' 'get' method.
    BeautifulSoup finds the first script with type='application/ld+json
    and the json module converts that to a dict object."""
    res = get(url)
    soup = bs(res.text, 'html.parser')
    recipe = loads(soup.find_all('script', type='application/ld+json')[0].text)
    recipe_name = recipe['name']
    print(f'\nYour are about to cook {recipe_name}!!\n')
    print('You will need: \n')
    for ingredient in recipe['recipeIngredient']:
        print(ingredient)
    print('\nThe method is: \n')
    for instruction in recipe['recipeInstructions']:
        print(f'{instruction}\n')

url = input("Please enter the url of the recipe you would like to save: ")

if __name__ == '__main__':
    scraper(url)
