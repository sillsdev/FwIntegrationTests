#!/bin/bash

kill `pidof mono`

ps cax | grep mono > /dev/null
echo "helpers/restart_flex.sh"
if [ $? -eq 0 ]; then
  echo "Process is running."
  sudo killall mono # kill all mono if more than one ~ Ryan
else
  echo "Process is not running."
fi
/home/vagrant/FwIntegrationTests/scripts/memory_clean.sh

fieldworks-flex &
disown %1
