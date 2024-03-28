#!/bin/bash
# Script that makes a request to causes an specific response
curl -H 'Origin: School' -X PUT -d "user_id=98" -sL "$(curl -X PUT -o /dev/null -s -w '%{redirect_url}' 0.0.0.0:5000/catch_me)"
