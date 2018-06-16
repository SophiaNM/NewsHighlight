from flask import render_template
from app import app
from .request import get_newsource,get_articles


# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    #Getting news sources
    general_newsource = get_newsource('general')
    technology_newsource = get_newsource('technology')
    entertainment_newsource = get_newsource('entertainment')
    sports_newsource = get_newsource('sports')
    business_newsource = get_newsource('business')
    science_newsource = get_newsource('science')

    title = 'Home | New Highlights'
    return render_template('index.html', title=title, general = general_newsource, technology = technology_newsource, entertainment = entertainment_newsource, sports = sports_newsource, business= business_newsource, science = science_newsource)

@app.route('/articles/<source_id>&<int:per_page>')
def articles(source_id,per_page):
    '''
    View article page function returns the articles based on a new source
    '''

    #Getting articles
    article_source = get_articles(source_id,per_page)

    title = f'{source_id} | All Articles'
    return render_template('article.html', title=title, name = source_id, articles = article_source)
