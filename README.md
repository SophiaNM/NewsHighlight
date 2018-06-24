# News Highlights
This is the fourth Independent project for Moringa Core, June 22nd 2018.

## Description

News Highlights is a web application that will help users list and preview news articles from various sources. It is a web application that is meant to catch up hard workers on current affairs happening all over the world.

## Features
- The home page allows users to see various news sources sorted based on categories and select their preference.
- Once selected, a list of all articles for that news source with image description and time of posting article is shown.
- User can click on an article and read it fully from the news source.
- Users can additionally click top headlines to see top headline articles.
- Users can also search for specific articles.

## Behavior Driven Development
| Behavior            | Input                         | Output                        |
| ------------------- | ----------------------------- | ----------------------------- |
| View All News Sources | Default Home Page | Displays all news sources |
| View Categories of news sources<br>(Technology, entertainment, sports etc)| Click on `Categories` drop down then on specific category e.g. `Technology` | Scrolls down to Technology news sources|
|View Top Headlines | Click on `Top Headlines` button | Redirects to the Top Headlines article page  |
| View All Articles | Click on  `All Articles`| Redirects to the All Articles page |
| Search for an article by keyword | Type any keyword in `search bar` e.g. `Jack Ma`| Redirects to search page with all the search results for Jack Ma|

## View Live Site here
View the complete site [here](https://newshighlight-sophia.herokuapp.com/)


## Technologies Used
    - Python 3.6
    - Flask Framework
    - HTML, CSS and Bootstrap
    - JavaScript


## Set-up and Installation
    1. Clone or download the Repo
    2. Create a virtual environment
    3. Read the specs and requirements files and Install all the requirements.
    4. Edit the start.sh file with your api key from the news.org website   
    6. Run chmod a+x start.py
    7. Run ./start.py
    8. Access the application through `localhost:5000`

## Known bugs
No known bugs so far. If found drop me an email.

## Contributors
    - Sophia Murage

### Contact Information
njerimurage92@gmail.com | snmurage1@gmail.com
