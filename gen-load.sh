#!/bin/bash

host=$1
happy_path="http://"$1":8080/"
error_path="http://"$1":8080/error-502"
error_5_path="http://"$1":8080/error-500"


duration=$2  # Duration in seconds

echo "host: $1"
echo "duration: $2"

echo "Paths to hit:"
echo "$happy_path"
echo "$error_path"
echo "$error_5_path"

end_time=$(( $(date +%s) + duration ))

while [ $(date +%s) -le $end_time ]; do
  curl -s -o /dev/null -w "%{http_code}\n" "$happy_path"
  sleep 1

  curl -s -o /dev/null -w "%{http_code}\n" "$error_path"
  sleep 1

  curl -s -o /dev/null -w "%{http_code}\n" "$happy_path"
  sleep 1

  curl -s -o /dev/null -w "%{http_code}\n" "$error_5_path"
  sleep 1
done
