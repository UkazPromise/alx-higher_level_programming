#!/bin/bash

# Check if a URL argument is provided
if [ -z "$1" ]; then
  echo "Error: Please provide a URL as an argument."
  exit 1
fi

# Extract the URL from the argument
url="$1"

# Send OPTIONS request and extract allowed methods
allowed_methods=$(curl -s -o /dev/null -I -w "%{http_code}\n" "$url" | grep -i '^allow:' | cut -d ':' -f2- | tr -d '\r')

# Check for successful status code (200)
if [ "$?" -eq 0 ]; then
  # Display allowed methods (remove leading/trailing spaces)
  echo "${allowed_methods%%  }"  # Remove leading spaces
else
  echo "Error: Status code $?" received.
fi

