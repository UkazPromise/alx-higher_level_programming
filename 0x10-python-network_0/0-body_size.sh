!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

HEADER_FILE=$(mktemp)
curl -s -D "$HEADER_FILE" -o /dev/null "$1"

HEADER_SIZE=$(wc -c < "$HEADER_FILE")
echo "Size of the HTTP response header for $1 is $HEADER_SIZE bytes"

rm "$HEADER_FILE"
