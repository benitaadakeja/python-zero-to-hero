# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 09:40:17 2026

@author: PERSONAL
"""
'''
Today, I'm learning about External data and JSON. Here's the task to be done:
CHALLENGE 1
1. Open a new file in Spyder and save it as day2_external_data.py.

2. import json at the top.

3. Create a variable called api_payload and assign it this exact raw string: '{"user": "Benita", "role": "DevOps", "active": true}'. (Use single quotes on the outside!)

4. Convert that string into a real dictionary using json.loads() and save it to a new variable called user_data.

5. Write an f-string print statement that extracts the "user" and "role" keys to say: "[User] has logged in as a [Role].".
'''
import json

api_payload = '{"user": "Benita", "role": "DevOps", "active": true}'
user_data = json.loads(api_payload)
print(f"{user} has logged in as {role}")
