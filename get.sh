#!/bin/bash
curl 'https://api.checklistbank.org/dataset/272972/export.zip?format=ColDP' -L | bsdtar -xf - VernacularName.tsv
python parse.py
