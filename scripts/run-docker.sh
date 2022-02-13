#!/usr/bin/env bash
cd ..
upper=$(echo ${1} | tr a-z A-Z)

if [ "${1}" == "local" ] ; then
    credentials_start=$(grep -ne serverless-course-user ~/.aws/credentials | grep -o '[0-9][0-9]*')
    access_key_line=$(($credentials_start + 1))
    secret_key_line=$(($credentials_start + 2))
    export AWS_ACCESS_KEY_ID=$(sed -n "${access_key_line}s/^aws_access_key_id = \(.*\)/\1/p" ~/.aws/credentials)
    export AWS_SECRET_ACCESS_KEY=$(sed -n "${secret_key_line}s/^aws_secret_access_key = \(.*\)/\1/p" ~/.aws/credentials)
else
    echo "Supports only local deployment!"
fi

docker-compose build --force-rm serverless-deploy
docker-compose run \
    -e AWS_ACCESS_KEY_ID="${AWS_ACCESS_KEY_ID}" \
    -e AWS_SECRET_ACCESS_KEY="${AWS_SECRET_ACCESS_KEY}" \
    -e AWS_DEFAULT_REGION=eu-west-1 \
    --rm \
    serverless-deploy