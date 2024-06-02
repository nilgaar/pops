#!/bin/bash
echo "======================================="
echo "============= Subdomainer ============="
echo "======================================="
wordlistPath=$1
domain=$2
basePageSize=$3
protocol="http"
if [ -z "$wordlistPath" ]; then
    echo "Wordlist path is required"
    exit 1
fi
if [ -z "$domain" ]; then
    echo "Domain is required"
    exit 1
fi
if [ -z "$basePageSize" ]; then
    echo "Base page size is required"
    exit 1
fi

ffuf -u "${protocol}://${domain}" -w $wordlistPath -H "Host:FUZZ.$domain" -fs $basePageSize