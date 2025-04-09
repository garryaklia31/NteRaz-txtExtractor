#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6478073504:AAFVjJYFBPo_Qk7sMLwjNVAKBNyexSipc8A")
    API_ID = int(os.environ.get("API_ID", "28386099"))
    API_HASH = os.environ.get("API_HASH", "a0057fbf1ca49ce5e9d26fd4afd6e78b)
    AUTH_USERS = os.environ.get("AUTH_USERS", "1718738592")
