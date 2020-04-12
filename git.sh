#!/bin/bash

read -r -p 'Commit message: ' commitMsg
git add .
git commit -m "$commitMsg"
git push