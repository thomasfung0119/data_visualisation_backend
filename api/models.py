# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from datetime import datetime

import json

from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Data(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    Date = db.Column(db.String(32), nullable=False)
    Country = db.Column(db.String(32), nullable=False)
    ConfirmedCase = db.Column(db.Integer())
    DeathCase = db.Column(db.Integer())
    DeathWithVaccine = db.Column(db.Integer())
    DeathWithSmoke = db.Column(db.Integer())
    DeathWithExercise = db.Column(db.Integer())

    @classmethod
    def queryMultipleFromCountry(cls, country):
        return cls.query.filter_by(Country=country).all()

    @classmethod
    def queryAll(cls):
        return_dict = {}
        countries = ["Fiji", "Tanzania", "W. Sahara", "Canada", "United States of America", "Kazakhstan", "Uzbekistan", "Papua New Guinea", "Indonesia", "Argentina", "Chile", "Dem. Rep. Congo", "Somalia", "Kenya", "Sudan", "Chad", "Haiti", "Dominican Rep.", "Russia", "Bahamas", "Falkland Is.", "Norway", "Greenland", "Fr. S. Antarctic Lands", "Timor-Leste", "South Africa", "Lesotho", "Mexico", "Uruguay", "Brazil", "Bolivia", "Peru", "Colombia", "Panama", "Costa Rica", "Nicaragua", "Honduras", "El Salvador", "Guatemala", "Belize", "Venezuela", "Guyana", "Suriname", "France", "Ecuador", "Puerto Rico", "Jamaica", "Cuba", "Zimbabwe", "Botswana", "Namibia", "Senegal", "Mali", "Mauritania", "Benin", "Niger", "Nigeria", "Cameroon", "Togo", "Ghana", "Cu7e6bte d'Ivoire", "Guinea", "Guinea-Bissau", "Liberia", "Sierra Leone", "Burkina Faso", "Central African Rep.", "Congo", "Gabon", "Eq. Guinea", "Zambia", "Malawi", "Mozambique", "eSwatini", "Angola", "Burundi", "Israel", "Lebanon", "Madagascar", "Palestine", "Gambia", "Tunisia", "Algeria", "Jordan", "United Arab Emirates", "Qatar", "Kuwait", "Iraq", "Oman", "Vanuatu", "Cambodia", "Thailand", "Laos", "Myanmar", "Vietnam", "North Korea", "South Korea", "Mongolia", "India", "Bangladesh", "Bhutan", "Nepal", "Pakistan", "Afghanistan", "Tajikistan", "Kyrgyzstan", "Turkmenistan", "Iran", "Syria", "Armenia", "Sweden", "Belarus", "Ukraine", "Poland", "Austria", "Hungary", "Moldova", "Romania", "Lithuania", "Latvia", "Estonia", "Germany", "Bulgaria", "Greece", "Turkey", "Albania", "Croatia", "Switzerland", "Luxembourg", "Belgium", "Netherlands", "Portugal", "Spain", "Ireland", "New Caledonia", "Solomon Is.", "New Zealand", "Australia", "Sri Lanka", "China", "Taiwan", "Italy", "Denmark", "United Kingdom", "Iceland", "Azerbaijan", "Georgia", "Philippines", "Malaysia", "Brunei", "Slovenia", "Finland", "Slovakia", "Czechia", "Eritrea", "Japan", "Paraguay", "Yemen", "Saudi Arabia", "Antarctica", "N. Cyprus", "Cyprus", "Morocco", "Egypt", "Libya", "Ethiopia", "Djibouti", "Somaliland", "Uganda", "Rwanda", "Bosnia and Herz.", "Macedonia", "Serbia", "Montenegro", "Kosovo", "Trinidad and Tobago", "S. Sudan"]
        for country in countries:
            temp = cls.query.filter_by(Country=country).all()
            tempList = [i.toFullJSON() for i in temp]
            ConfirmedCase = sum([i['ConfirmedCase'] for i in tempList])
            MortalityCase = sum([i['DeathCase'] for i in tempList])
            return_dict[country] = {'ConfirmedCase':ConfirmedCase, 'MortalityCase':MortalityCase}
        return return_dict

    def toFullJSON(self):
        temp = {}
        temp['Date'] = self.Date
        temp['ConfirmedCase'] = self.ConfirmedCase
        temp['DeathCase'] = self.DeathCase
        temp['DeathWithVaccine'] = self.DeathWithVaccine
        temp['DeathWithSmoke'] = self.DeathWithSmoke
        temp['DeathWithExercise'] = self.DeathWithExercise
        return temp
    
    def toCountryJSON(self):
        temp = {}
        temp['Date'] = self.Date
        temp['Country'] = self.Country
        temp['ConfirmedCase'] = self.ConfirmedCase
        temp['DeathCase'] = self.DeathCase
        temp['DeathWithVaccine'] = self.DeathWithVaccine
        temp['DeathWithSmoke'] = self.DeathWithSmoke
        temp['DeathWithExercise'] = self.DeathWithExercise
        return temp


