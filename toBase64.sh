#!/bin/bash

echo "Converting $1 to base64"
base64 "$1" > "$1.b64"
if $2; then
    cat "$1.b64" | xclip -selection clipboard
    echo "copied to clipboard"
fi
