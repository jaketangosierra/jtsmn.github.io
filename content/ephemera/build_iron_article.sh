#!/bin/bash
LOWER=iron-blogging-$(echo $1 | tr '[:upper:]' '[:lower:]')
DATE=$(date '+%Y-%m-%d')
NAME=$DATE-$LOWER.md
TITLE=$(echo $1 | sed 's/-/ /g');
echo "Title: Iron Blogging - $TITLE" >> $NAME
echo "Date: $DATE" >> $NAME
echo "Modified: $DATE" >> $NAME
echo "kind: article" >> $NAME
echo "author: Jacob Thebault-Spieker" >> $NAME
echo "status: draft" >> $NAME

echo "> _This post is a part of the GroupLens Iron Blogging effort, so take that for what you will._" >> $NAME
