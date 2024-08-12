#!/bin/bash

# Check if a URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <domain>"
    exit 1
fi

url=$1

# Create necessary directories if they don't exist
mkdir -p "$url/recon"

echo "[+] Harvesting subdomains with assetfinder...."
assetfinder "$url" >> "$url/recon/assets.txt"

# Filter unique subdomains and store in final.txt
grep "$url" "$url/recon/assets.txt" | sort -u > "$url/recon/final.txt"
rm "$url/recon/assets.txt"

# Uncomment below lines if you want to include Amass results
# echo "[+] Harvesting subdomains with Amass...."
# amass enum -d "$url" >> "$url/recon/amass.txt"
# sort -u "$url/recon/amass.txt" >> "$url/recon/final.txt"
# rm "$url/recon/amass.txt"

echo "[+] Probing for alive domains...."
cat "$url/recon/final.txt" | sort -u | httprobe -s -p https:443 | sed 's/https\?:\/\///' | tr -d ':443' > "$url/recon/alive.txt"
