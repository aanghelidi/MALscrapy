#!/usr/bin/bash

length=$1
out_file=$2

if [[ -z $length ]]; then
  echo "Specify a length"
elif [[ -z $out_file ]]; then
  echo "Specify an output file"
else
  openssl rand -base64 $length > $out_file
fi
