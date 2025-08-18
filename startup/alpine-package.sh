#!/bin/sh

# Check if the package list file exists
if [ ! -f "$PACKAGE_LIST" ]; then
    
    exit 0
fi

# Update package lists
apk update

# Install packages from the list
while IFS= read -r package; do
    echo "Installing $package..."
    apk add --no-cache "$package"
done < "$PACKAGE_LIST"

echo "All packages installed."