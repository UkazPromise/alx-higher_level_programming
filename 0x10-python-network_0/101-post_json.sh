#!/bin/bash

# Check if URL and file arguments are provided
if [ -z "$1" ] || [ -z "$2" ]; then
  echo "Error: Please provide both a URL and a file as arguments."
  exit 1
fi

# Extract the URL and file name from the arguments
url="$1"
file="$2"

# Check if the file exists
if [ ! -f "$file" ]; then
  echo "Error: File '$file' does not exist."
  exit 1
fi

# Send POST request with file contents in the body and capture the response
response=$(curl -s -X POST -H "Content-Type: application/json" --data "@$file" "$url")

# Check if the response contains "Valid JSON" or "Not a valid JSON"
if [[ "$response" == *"Valid JSON"* ]]; then
  echo "Valid JSON"
else
  echo "Not a valid JSON"
fi
