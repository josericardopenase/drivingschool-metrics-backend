#!/bin/bash
git add .
git commit -m "Generated new deploy to heroku"
poetry export -f requirements.txt --output requirements.txt
git push origin master
git push heroku master:main