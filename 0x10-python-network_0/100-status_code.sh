#!/bin/bash

# Check if a URL argument is provided
if [ -z "$1" ]; then
  echo "Error: Please provide a URL as an argument."
  exit 1
fi

# Extract the URL from the argument
url="$1"

# Send the request and capture the status code directly in a variable
status_code=$(curl -s -w "%{http_code}" "$url")

# Print the status code
echo "$status_code"

