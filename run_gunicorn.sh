#!/bin/sh

gunicorn -w4 -b${FLASK_ADDRESS} quizbutton:app
