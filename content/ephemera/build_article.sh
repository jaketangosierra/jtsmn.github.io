#!/bin/bash
LOWER=$(echo $1 | tr '[:upper:]' '[:lower:]')
DATE=$(date '+%Y-%m-%d')
NAME=$DATE-$LOWER.md
TITLE=$(echo $1 | sed 's/-/ /g');
echo "Title: $TITLE" >> $NAME
echo "Date: $DATE" >> $NAME
echo "Modified: $DATE" >> $NAME
echo "kind: article" >> $NAME
echo "author: Jacob Thebault-Spieker" >> $NAME
echo "statsu: draft" >> $NAME
