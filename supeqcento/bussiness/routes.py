# -*- coding: utf-8 -*-
from sanic import Blueprint

from supeqcento.bussiness.user.user_route import SyncUserRoute, AsyncUserRoute,\
    UserRoute

user_module = Blueprint("user", url_prefix="{}/users".format("/api/v1"))

user_module.add_route(UserRoute.as_view(), "/<uid>")
user_module.add_route(AsyncUserRoute.as_view(), "/async/<uid>")
user_module.add_route(SyncUserRoute.as_view(), "/sync/<uid>")
