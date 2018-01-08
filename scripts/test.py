from flask import Flask
from flask import request
import json
app = Flask(_name_)


@app.route('/')
def hello():
    return "Check Code of countries"

#Ubertas Test for searching country code run on address bar http://127.0.0.1:5000/country-name
@app.route('/api/v1/countries')
def iso_country():
    dict={'UK':'GB','Ireland':'IE','France':'FR','Spain':'ES'}
    country_name = request.args.get('name')
    return dict[country_name]

if _name_ == '_main_':
    app.run()
