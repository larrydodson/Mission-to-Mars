# Mission-to-Mars
UTMCC DataViz Module 10

---

## Contents 
  * Overview
    - Purpose
    - Resources
  * Results
  * Summary
 

---  

## Overview 
  
  In support of Robin in her effort to create a Mars related information web page, we have generated code to scrape web sites of Mars data, using the resources and tools as shown below. Data in the forms of images, planet specifics and weather, are captured using web scraping tools and methods, and presented in a summary web page using tools for data base management and editing. 

   ### Purpose
   To prepare new Mars information site in support of Robin and her aspirations to someday work for NASA. 
  
   The deliverables are: 
   - Deliverable 1: Scrape High-Resolution Mars Hemisphere Images and Titles
   - Deliverable 2: Update the Web App with Mars Hemisphere Images and Titles
   - Deliverable 3: Add 3 Bootstrap Components.
  
   
  
   ### Resources
  * Data/content sources: NASA, JPL and USGS Astopedia web content 
  * Software: Windows10, Python 3.8.3, Jupyter Notebook, VS Code 1.49.1, HTML, Splinter, BeautifulSoup 2.0.1, Flask 1.1.2, flask_pymongo 2.3.0, Bootstrap 3.3.7, MongoDB 4.4.1
  

--- 

## Results
  
  #### Deliverable 1
   **Scrape High-Resolution Mars Hemisphere Images and Titles** 
  
  ![](https://github.com/larrydodson/Mission-to-Mars/blob/master/scrape_success.png)
  
  
  ![dictionary_items.png](https://github.com/larrydodson/Mission-to-Mars/blob/master/dictionary_items.png)
  
  
  ![mongo_confirm.png](https://github.com/larrydodson/Mission-to-Mars/blob/master/mongo_confirm.png)
  
  
  #### Deliverable 2
   **Update the Web App with Mars Hemisphere Images and Titles** 
  
  ![MissionToMars_home_partial.png](https://github.com/larrydodson/Mission-to-Mars/blob/master/MissionToMars_home_partial.png)
 
  
  
  #### Deliverable 3
   **3 Bootstrap Components**
 1. Tables: Added styles to both tables, "Facts" and "Weather": "table-striped", "table-bordered", "table-hover"
 2. Responsive: for both tables, added "table-responsive"; and, Bootstrap is inherently "Responsive" and have confirmed respponsiveness within Chrome "Inspect" tool.
 3. Added web page black background and white text in the page's "body", with: <body class="text-white" style="background-color:black;">
 4. Within the "Jumbotron" header "scraping button", have changed color and white text to make it stand-out, with: <a class="btn btn-primary btn-lg text-white" style="background-color:#782a09;" href="/scrape" role="button">Scrape New Data <br> "Refresh"</a>
 5. Added extra line white spacing around Weather Table and the Hemispheres page areas for more separation.
 6. Added "Footer" to show end-of-page, and for customization.
 

.

---


## Summary



.

.end 
