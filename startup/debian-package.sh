#!/bin/bash

# Check if the package list file exists
if [ ! -f "$PACKAGE_LIST" ]; then
    exit 0
fi

# Update package lists
apt update

# Install packages from the list
while IFS= read -r package; do
    echo "Installing $package..."
    apt install -y "$package"
done < "$PACKAGE_LIST"

echo "All packages installed."