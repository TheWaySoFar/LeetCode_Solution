#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
req = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})
print(req.url)