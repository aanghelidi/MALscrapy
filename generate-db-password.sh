#!/usr/bin/bash

length=$1

if [[ -z $length ]]; then
  echo "Specify a length"
else
  openssl rand -base64 $length > postgres_db_password.txt
fi
