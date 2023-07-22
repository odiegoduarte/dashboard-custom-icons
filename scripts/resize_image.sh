#!/bin/bash
#
# Autor:      Diego Duarte 2023
# Projeto:    https://github.com/odiegoduarte/dashboard-custom-icons
#
# Use o comando ./resize_image.sh pasta
#

if [ $# -ne 1 ]; then
    echo "Usage: $0 <input_folder>"
    exit 1
fi

input_folder="$1"
output_folder="${input_folder}_resized"

if [ ! -d "$input_folder" ]; then
    echo "Error: Input folder '$input_folder' not found."
    exit 1
fi

mkdir -p "$output_folder"

for image in "$input_folder"/*.png; do
    if [ -f "$image" ]; then
        output_image="$output_folder/$(basename $image)"
        convert "$image" -resize 300x300 "$output_image"
        echo "Image '$image' resized to 300x300 and saved as '$output_image'."
    fi
done