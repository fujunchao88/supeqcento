# -*- coding: utf-8 -*-
import peewee

from supeqcento.bussiness.data.model import User, db_manager


class UserOperation:

    @staticmethod
    def get_user_by_id(uid):
        try:
            return User.select().where(User.uid == uid).get()
        except peewee.DoesNotExist:
            return None

    @staticmethod
    async def async_get_user_by_id(uid):
        try:
            return await db_manager.get(User.select().where(User.uid == uid))
        except peewee.DoesNotExist:
            return None
