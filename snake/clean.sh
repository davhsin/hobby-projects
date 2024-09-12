#!/bin/bash

if [ -d "venv" ]; then
	source venv/bin/activate
	pip freeze > requirements.txt
	deactivate
	rm -r venv
fi
