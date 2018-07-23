import requests
try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

search = 'http://www.imdb.com/search/title?count=250&num_votes=1000,&title_type=feature&view=simple&page={}&ref_=adv_nxt'
pages = 1
movies = {}
movie_ids = []
tags = []

for x in range(pages):
    print("Page", x+1)
    response = requests.get(search.format(x+1))
    parsed_html = BeautifulSoup(response.text)
    # parsed_html.body.find('div', attrs={'class':'lister-list'})
    for listed in parsed_html.body.findAll('span', attrs={'class':'lister-item-header'}):
        # if listed.find('a') > -1:
        mid = listed.find('a')['href'].split("/")[2]
        movie_ids.append(mid)
        movies[mid] = {}

rating_ages = [1,2,3,4]
rating_genres = ["male", "female"]

for movie_id in movie_ids:
    print(movie_id)
    print("Tags")
    url = 'http://www.imdb.com/title/{}/keywords?ref_=tt_stry_kw'.format(movie_id)
    response = requests.get(url)
    parsed_html = BeautifulSoup(response.text)
    for listed in parsed_html.body.findAll('td', attrs={'class':'soda sodavote'}):
        try:
            interesting = listed.find('div', attrs={'class': 'interesting-count-text'}).find('a').text.split()[0]
            if interesting.isdigit() and int(interesting) > 1:
                keyword = listed['data-item-keyword']
                if not keyword in tags:
                    tags.append(keyword)
                movies[movie_id].setdefault("tags", []).append(tags.index(keyword))
        except:
            import pdb; pdb.set_trace()
    print("Ratings")
    for age in rating_ages:
        for genre in rating_genres:
            try:
                url = 'http://www.imdb.com/title/{}/ratings-{}_age_{}'.format(movie_id, genre, age)
                response = requests.get(url)
                parsed_html = BeautifulSoup(response.text)
                listed = parsed_html.body.find('div', attrs={'id': 'tn15content'}).find('table').findAll('tr')
                movies[movie_id].setdefault("ratings", {})
                movies[movie_id]["ratings"]["{}{}".format(genre, age)] = {}
                for index in range(10):
                    movies[movie_id]["ratings"]["{}{}".format(genre, age)][10-index] = listed[index+1].find('td').text
            except:
                import pdb; pdb.set_trace()



import pdb; pdb.set_trace()
