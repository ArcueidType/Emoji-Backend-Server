from .resources import *
from flask_restful import Api


def enable_all_apis(app):
    api = Api(app)

    api.add_resource(AddOp, '/add')
    api.add_resource(BodySegment, '/bodysegment')

    return api
