class Config:
    '''
    General configuration parent class
    '''
    SOURCE_API_BASE_URL ='https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    EVERYTHING_SOURCE_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&pageSize={}&apiKey={}'
    TOP_HEADLINES_BASE_URL = 'https://newsapi.org/v2/top-headlines?language=en&pageSize=40&apiKey={}'
    EVERYTHING_BASE_URL = 'https://newsapi.org/v2/everything?sources=bbc-news,al-jazeera-english,cnn,independent,google-news,the-telegraph,mashable,the-lad-bible,buzzfeed,bloomberg,engadget,espn,fortune&sortBy=publishedAt&pageSize=40&apiKey={}'



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
