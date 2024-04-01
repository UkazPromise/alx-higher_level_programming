#!/bin/bash

# Check if a URL argument is provided
if [ -z "$1" ]; then
  echo "Error: Please provide a URL as an argument."
  exit 1
fi

# Extract the URL from the argument
url="$1"

# Send DELETE request and display the body of the response
curl -s -X DELETE "$url"
