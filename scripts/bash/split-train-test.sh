#!/bin/bash

# Set directories
IMAGE_DIR="../damn-yankee-data/yolo/images"
LABEL_DIR="../damn-yankee-data/yolo/labels"
OUTPUT_DIR="../damn-yankee-data/yolo"
TRAIN_RATIO=0.8

# Create output directories
mkdir -p $OUTPUT_DIR/images/train $OUTPUT_DIR/images/val
mkdir -p $OUTPUT_DIR/labels/train $OUTPUT_DIR/labels/val

# Get list of image filenames (no extension)
FILES=($(ls "$IMAGE_DIR" | grep -Ei '\.(jpg|jpeg|png)$' | sed 's/\.[^.]*$//'))

# Shuffle files
shuf_files=($(shuf -e "${FILES[@]}"))

# Compute counts
total=${#shuf_files[@]}
train_count=$(( total * TRAIN_RATIO / 100 ))

# Split files
for i in "${!shuf_files[@]}"; do
    base="${shuf_files[$i]}"
    img_path=$(ls "$IMAGE_DIR"/"$base".* 2>/dev/null | head -n 1)
    img_ext="${img_path##*.}"
    label_file="$LABEL_DIR/$base.txt"

    if [ $i -lt $train_count ]; then
        cp "$img_path" "$OUTPUT_DIR/images/train/"
        cp "$label_file" "$OUTPUT_DIR/labels/train/"
    else
        cp "$img_path" "$OUTPUT_DIR/images/val/"
        cp "$label_file" "$OUTPUT_DIR/labels/val/"
    fi
done

echo "✅ Dataset split complete: $train_count training, $((total - train_count)) validation samples."
