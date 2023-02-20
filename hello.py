from flask import Flask
from repoScrape import scrape
import logging


app = Flask(__name__)


@app.route('/')
def hello():
	app.logger.info('Info')
	return scrape()



# for later
# @app.route('/users')
# def users():
#    users= User.query.all()
