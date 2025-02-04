#!/bin/bash

if [ ! -d "/etc" ]; then
  echo "/etc не існує"
  exit 1
fi

count=$(find /etc -type f | wc -l)

echo "Кількість файлів у каталозі /etc (без директорій та посилань): $count"
