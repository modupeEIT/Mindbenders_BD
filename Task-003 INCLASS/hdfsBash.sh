#!usr/bin/bash



service=$(jps)
if [[ $service == *"DataNode"* ]]; then
    echo "SERVICE RUNNING" 
else
    echo "SERVICE NOT RUNNING.... STARTING UP SERVICE "
    eval "start-all.sh"
    echo "SERVICE STARTED"
fi
