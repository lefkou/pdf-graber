#!/bin/sh

# alvinalexander.com
# a shell script used to download a specific url.
# this is executed from a crontab entry every day.

DIR = ~/Workspace/pdf-graber/

INPUT=pdf_links.csv
OLDIFS=$IFS
IFS=,
[ ! -f $INPUT ] && { echo "$INPUT file not found"; exit 99; }
while read flname dob ssn tel status
do
	$wget $flname
done < $INPUT
IFS=$OLDIFS
