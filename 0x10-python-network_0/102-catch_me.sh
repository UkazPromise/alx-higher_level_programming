#!/bin/bash

# Send a GET request to the target URL and check for "You got me!" in the response
if curl -s "http://0.0.0.0:5000/catch_me" | grep -q "You got me!"; then
  # Success: exit code 0 (no output)
  exit 0
else
  # Failure: exit code 1
  exit 1
fi
