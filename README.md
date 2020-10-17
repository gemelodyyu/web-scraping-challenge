# Missions to Mars


This project build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. 


## Objectives


### Step 1 - Scraping


Initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.


#### NASA Mars News


* Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. 


#### JPL Mars Space Images - Featured Image


* Visit the url for JPL Featured Space Image.


* Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.


#### Mars Facts


* Visit the Mars Facts webpage and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.


* Use Pandas to convert the data to a HTML table string.


#### Mars Hemispheres


* Visit the USGS Astrogeology site to obtain high resolution images for each of Mar's hemispheres.


* Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys `img_url` and `title`.


* Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.


### Step 2 - MongoDB and Flask Application


Use MongoDB with Flask templating to create a HTML page that displays all of the information that was scraped from the URLs above.


#### Here is what the application looks like (2020/10/17): 

<img width="525" alt="final screenshot" src="https://user-images.githubusercontent.com/55970064/96352289-c6fc8780-1087-11eb-8552-7fb93e44fc3b.png">

