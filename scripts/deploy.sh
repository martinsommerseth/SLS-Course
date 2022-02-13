#!/usr/bin/env bash

template_folder=../resources/cfn-templates

deploy() {
  echo ""
  echo "------------------------"
  echo "- Deploying Serverless -"
  echo "------------------------"

  cd ..
  sls plugin install -n serverless-python-requirements
  sls deploy || exit 1
}

echo ""
echo "-----------------------------------"
echo "- Initializing deployment process -"
echo "-----------------------------------"
deploy $1