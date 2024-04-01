Bash
#!/bin/bash

# Check if a URL argument is provided
if [ -z "$1" ]; then
  echo "Error: Please provide a URL as an argument."
  exit 1
fi

# Extract the URL from the argument
url="$1"

# Set email and subject variables
email="test@gmail.com"
subject="I will always be here for PLD"

# Send POST request with body and display response
curl -s -X POST -d "email=$email&subject=$subject" "$url" | grep -v '^HTTP'

