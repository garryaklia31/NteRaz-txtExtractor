#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6478073504:AAFVjJYFBPo_Qk7sMLwjNVAKBNyexSipc8A")
    API_ID = int(os.environ.get("API_ID", "21863630"))
    API_HASH = os.environ.get("API_HASH", "fcaec0e8a1e8d2675122068f40b76817")
    AUTH_USERS = os.environ.get("AUTH_USERS", "1718738592")
