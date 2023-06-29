#!/bin/sh
# set -eu

chmod +x ./requirements.txt && pip install -r ./requirements.txt
echo

# Check if the "redis" container is running
if ! docker ps --filter "status=running" --format "{{.Names}}" | grep -q "redis"; then
  # If the "redis" container is not running, start it using docker-compose
  docker-compose -f ./docker-compose.yml up -d
else
  echo "The 'redis' container is already running."
fi

# Show plugin host url
export PLUGIN_HOSTNAME=https://$CODESPACE_NAME-8000.$GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN 

echo
echo "Once your app is running, use the following URL to use this plugin in the OpenAI Plugin store:"
echo $PLUGIN_HOSTNAME
