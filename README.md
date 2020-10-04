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
  
  In support of Robin in her effort to create a Mars related information web page, we have generated code to automatically scrape web sites of Mars data, using the resources and tools as shown below. Data in the forms of images, planet specifics and weather, are captured using web scraping tools and methods, and presented in a summary web page using tools for data base management and web page editing. 

   ### Purpose
   To prepare a new Mars information site in support of Robin and her aspirations to someday work for NASA, by using and learning tools used for web scraping, database, and web browser presentation. 
  
   The deliverables are: 
   - Deliverable 1: Scrape High-Resolution Mars Hemisphere Images and Titles
   - Deliverable 2: Update the Web App with Mars Hemisphere Images and Titles
   - Deliverable 3: Add 3 Bootstrap Components.
  
   
  
   ### Resources
  * Data/content sources: NASA, JPL and USGS Astopedia web content 
  * Software: Windows10, Python 3.8.3, Jupyter Notebook, VS Code 1.49.1, HTML, Splinter, BeautifulSoup 2.0.1, Flask 1.1.2, flask_pymongo 2.3.0, Bootstrap 3.3.7, MongoDB 4.4.1
  

--- 

## Results
  
  ### Deliverable 1  --  Scrape High-Resolution Mars Hemisphere Images and Titles 
    
   * Please see the file  Mission_to_Mars_Challenge.ipynb  to see 1) the code for retrieving the full-resolution image and title for each hemisphere, and 2) the code with for looping to scrape for the hemisphere images. 
    
    
   **In Figure-1, Confirmation of "Scraping Successful"**:  
  ![](https://github.com/larrydodson/Mission-to-Mars/blob/master/scrape_success.png)
  
  
  **Figure-2, Confirmation of dictionary items, for titles and hemisphere images**:   
  ![dictionary_items.png](https://github.com/larrydodson/Mission-to-Mars/blob/master/dictionary_items.png)
  
 
 .
 
  ### Deliverable 2 --  Update the Web App with Mars Hemisphere Images and Titles 
   
   **Figure-3, Confirmation and Status of Mongo Database - containing All Four of hemisphere titles and the full-resolution image URLs.**: 
  ![mongo_confirm.png](https://github.com/larrydodson/Mission-to-Mars/blob/master/mongo_confirm.png)
    
   
   
   
   **Figure-4, Copy of Mission To Mars web-page, with Bootstrap components added.**  The Page copy is showing as the "iPad Pro" screen. 
   ![MissionToMars_home_partial.png](https://github.com/larrydodson/Mission-to-Mars/blob/master/MissionToMars_home_partial.png)
 
 

.

  ### Deliverable 3  --  Three Bootstrap Components Added 
 1. **Tables**: Added these styles to both tables, "Facts" and "Weather": "table-striped", "table-bordered", "table-hover"
 2. **Responsive / Mobile-responsive**: for both tables, added "table-responsive"; and, Bootstrap is inherently "Responsive" and have confirmed responsiveness within Chrome "Inspect" tool.  The image above in Figure-4 showing the web-page is for the "iPad Pro" screen. 
 3. **Background(s)**: 1) Added web page black background and white text in the page's "body", with: body class="text-white" style="background-color:black;"; and 2) added an image background of a Mars horizon. 
 4. **Scrape New Data button**: Within the "Jumbotron" header "scraping button", have changed color and using white text to make it stand-out, with: class="btn btn-primary btn-lg text-white" style="background-color:#782a09;" href="/scrape" role="button" for Scrape New Data "Refresh".
 5. Added: extra line white spacing around Weather Table and the Hemispheres page areas for more separation.
 6. **Footer**:  Added a "Footer" to help indicate the end-of-page, and for customization.
 

---

.end 
