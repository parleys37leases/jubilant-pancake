#!/bin/bash
prefix="renamed_"
for file in *.txt; do
  mv "$file" "${prefix}${file}"
done
echo "✅ Files renamed with prefix '$prefix'"
