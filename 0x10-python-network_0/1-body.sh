#!/bin/bash

# Check if a URL argument is provided
if [ -z "$1" ]; then
  echo "Error: Please provide a URL as an argument."
  exit 1
fi

# Extract the URL from the argument
url="$1"

# Send GET request and capture response with status code
response=$(curl -s -w "%{http_code}" "$url")

# Extract status code from response
status_code=$(echo "$response" | tail -n 1)

# Check for successful status code (200)
if [ "$status_code" -eq 200 ]; then
  # Extract and display the body (remove status code line)
  body=$(echo "$response" | head -n -1 | tail -n +2)
  echo "$body"
else
  echo "Error: Status code $status_code received."
fi
