#!/usr/bin/env python
# -*- coding: utf-8 -*-

import redis

from django_demo import settings

class RedisPool(object):

    """
    redis帮助类
    """

    def __init__(self,db=None):
        redis_cfg = settings.REDIS_CFG
        if db is None:
            db = redis_cfg['db']
        pool = redis.ConnectionPool(host=redis_cfg["host"], port=redis_cfg["port"],db = db, decode_responses=True)
        self.conn = redis.StrictRedis(connection_pool=pool, charset="utf-8")

    def __del__(self):
        self.conn.connection_pool.disconnect()


