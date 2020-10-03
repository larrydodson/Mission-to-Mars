# Tools
from flask import Flask, render_template
from flask_pymongo import PyMongo
import scraping

# set up Flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Define flask route for HTML home page
@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)

# add the next route and function
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update_many({}, mars_data, upsert=True)
   return "Scraping Successful!"

# run Flask
if __name__ == "__main__":
    app.run()