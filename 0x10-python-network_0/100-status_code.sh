#!/bin/bash
# sends a request to a URL passed as an argument, and displays only the status code of the response.
curl -sI -o /dev/null "$1" -w "%{response_code}"
