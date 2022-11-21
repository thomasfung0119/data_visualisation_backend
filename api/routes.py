# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""


from functools import wraps

from flask import request
from flask_restx import Api, Resource, fields

from .models import db, Data

rest_api = Api(version="1.0", title="Users API")


"""
    Flask-Restx models for api request and response data
"""

parser = rest_api.parser()
parser.add_argument('country', type=str , help='Chosen Country')

@rest_api.route('/api/getAll')
class AllData(Resource):

    @rest_api.expect(validate=True)
    def get(self):
        data = Data.queryAll()
        returnList = [i.toCountryJSON() for i in data]

        return returnList, 200

@rest_api.route('/api/getData')
class MultiData(Resource):

    @rest_api.expect(parser, validate=True)
    def get(self):
        _country = request.args.get('country')

        data = Data.queryMultipleFromCountry(_country)
        returnList = [i.toFullJSON() for i in data]

        return returnList, 200

@rest_api.route('/api/getSumUpData')
class SumUpData(Resource):

    @rest_api.expect(parser, validate=True)
    def get(self):
        _country = request.args.get('country')

        data = Data.queryMultipleFromCountry(_country)
        returnList = [i.toFullJSON() for i in data]
        ConfirmedCase = sum([i['ConfirmedCase'] for i in returnList])
        MortalityCase = sum([i['DeathCase'] for i in returnList])
        VaccinatedDeathCase = sum([i['DeathWithVaccine'] for i in returnList])
        Correlation = round(VaccinatedDeathCase/MortalityCase, 4)*100

        return {'ConfirmedCase':ConfirmedCase, 'MortalityCase':MortalityCase, 'VaccinatedDeathCase':VaccinatedDeathCase, 'CorrelationInPercentage':Correlation}, 200
