from rich.emoji import Emoji

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
    api.add_resource(Confuse, '/confuse')
    api.add_resource(FlashBlind, '/flashblind')
    api.add_resource(Trance, '/trance')
    api.add_resource(Play, '/play')
    api.add_resource(ChaseTrain, '/chasetrain')
    api.add_resource(FunnyMirror, '/funnymirror')
    api.add_resource(GuiChu, '/guichu')
    api.add_resource(Punch, '/punch')
    api.add_resource(Kiss, '/kiss')
    api.add_resource(Rub, '/rub')

    return api
