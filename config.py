#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex


import os

class Config(object):

    # Get a bot token from botfather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5945869005:AAHQnHiudJbSMUA-B4znobmcF18DSmxRrE8")


    # Get from my.telegram.org (or @UseTGXBot)
    APP_ID = int(os.environ.get("APP_ID", "1954515"))
    API_HASH = os.environ.get("API_HASH", "9ff4a51876a555bdb530cd6a58baae87")


    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "800555393").split())
    
