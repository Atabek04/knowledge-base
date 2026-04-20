#!/bin/bash
# Removes Anki ID comments (<!--ID: ...-->) from specified flashcard files
# Usage: ./remove-flashcard-ids.sh file1.md file2.md ...

if [ $# -eq 0 ]; then
  echo "Usage: $0 <file1.md> [file2.md ...]"
  echo "Example: $0 05-Flashcards/ml/fundamentals.md 05-Flashcards/ml/regression.md"
  exit 1
fi

for file in "$@"; do
  if [ ! -f "$file" ]; then
    echo "Skipped (not found): $file"
    continue
  fi
  sed -i '/^<!--ID: [0-9]*-->$/d' "$file"
  echo "Cleaned: $file"
done
