from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from config import password

app = Flask(__name__)

app.config['MONGO_URI'] = f'mongodb+srv://{username}:{password}@cluster0-wadjd.mongodb.net/test?retryWrites=true&w=majority'
mongo = PyMongo(app)


@app.route("/scrape")
def scraper():
    import scrape_mars
    mars_db = mongo.db.mars
    mars_data = scrape_mars.scrape()
    mars_db.update({}, mars_data, upsert=True)
    return redirect("/", code=302)

@app.route("/")
def index():
    mars_data = mongo.db.mars.find_one()
    return render_template('index.html', mars_data = mars_data)


if __name__ == "__main__":
    app.run(debug=True)
