# -*- coding: utf-8 -*-
from sanic.response import json
from sanic.views import HTTPMethodView

from supeqcento.bussiness.user.user_service import UserSerivce


# @user_module.get("/")
# async def test(request):
#     return json({'name': 'frank', 'age': 34})

class UserRoute(HTTPMethodView):
    async def get(self, request, uid):
        user = UserSerivce().get_user_by_uid(uid)
        return json(user.__dict__["_data"])


class AsyncUserRoute(HTTPMethodView):
    async def get(self, request, uid):
        user = await UserSerivce().async_get_user_by_uid(uid)
        return json(user.__dict__["_data"])


class SyncUserRoute(HTTPMethodView):
    def get(self, request, uid):
        user = UserSerivce().get_user_by_uid(uid)
        return json(user.__dict__["_data"])
