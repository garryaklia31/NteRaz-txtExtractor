#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6528420500:AAH0-q4m1mytX1rLdG2x-qJkPBdofzHo3fc")
    API_ID = int(os.environ.get("API_ID", "27498866"))
    API_HASH = os.environ.get("API_HASH", "96fbb6ad2e11ab04e83ca09ef3f42455")
    AUTH_USERS = os.environ.get("AUTH_USERS", "6488911325")
