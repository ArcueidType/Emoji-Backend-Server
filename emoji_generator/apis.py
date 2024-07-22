from .resources import *
from flask_restful import Api


def enable_all_apis(app):
    api = Api(app)

    api.add_resource(AddOp, '/add')
    api.add_resource(GrayWordMeme, '/graywordmeme')
    api.add_resource(BodySegment, '/bodysegment')
    api.add_resource(Always, '/always')
    api.add_resource(FightSunuo, '/fightsunuo')
    api.add_resource(AnimeGen, '/animegen')
    api.add_resource(AceAttorney, '/aceattorney')
    api.add_resource(Colorful, '/colorful')
    api.add_resource(ECNULion, '/ecnulion')
    api.add_resource(ECNUBlackboard, '/ecnublackboard')
    api.add_resource(CanNot, '/cannot')
    api.add_resource(LuXun, '/luxun')
    api.add_resource(BlueArchive, '/bluearchive')

    return api
