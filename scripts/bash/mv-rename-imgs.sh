#!/bin/bash

SRC_DIR="$1"
DEST_DIR="$2"

if [[ -z "$SRC_DIR" || -z "$DEST_DIR" ]]; then
  echo "Usage: $0 <source_directory> <destination_directory>"
  exit 1
fi

mkdir -p "$DEST_DIR"

# Find image files (you can extend the list of extensions as needed)
find "$SRC_DIR" -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" -o -iname "*.gif" \) | while read -r file; do
  parent_dir=$(dirname "$file")
  grandparent_dir=$(basename "$(dirname "$parent_dir")")
  filename=$(basename "$file")
  new_filename="${grandparent_dir}_${filename}"
  cp "$file" "$DEST_DIR/$new_filename"
done
