#!/usr/bin/env python3
prompt = "What you gotta say? : "
while True:
    answer = input(prompt)
    if answer == "STOP":
        break
    prompt = "I got that! Anything else? : "
