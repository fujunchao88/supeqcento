# -*- coding: utf-8 -*-
from supeqcento.bussiness.user.user_operation import UserOperation


class UserSerivce:

    def get_user_by_uid(self, uid):
        return UserOperation.get_user_by_id(uid)

    async def async_get_user_by_uid(self, uid):
        return await UserOperation.async_get_user_by_id(uid)


