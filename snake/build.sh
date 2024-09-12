#!/bin/bash

if [ ! -d "venv" ]; then
	# first time build and run.
	python3 -m venv venv
	source venv/bin/activate
	pip install -r requirements.txt
	python3 main.py
else
	# activate and build.
	source venv/bin/activate
	python3 main.py
fi

