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
    def querySumFromCountry(cls, country):
        return cls.query.filter_by(Country=country)
    @classmethod
    def queryCaseFromCountry(cls, country):
        return cls.query.filter_by(Country=country)

    @classmethod
    def queryMultipleFromCountry(cls, country):
        return cls.query.filter_by(Country=country)

    def toFullJSON(self):
        temp = {}
        temp['Date'] = self.Date
        temp['ConfirmedCase'] = self.ConfirmedCase
        temp['DeathCase'] = self.DeathCase
        temp['DeathWithVaccine'] = self.DeathWithVaccine
        temp['DeathWithSmoke'] = self.DeathWithSmoke
        temp['DeathWithExercise'] = self.DeathWithExercise
        return temp

