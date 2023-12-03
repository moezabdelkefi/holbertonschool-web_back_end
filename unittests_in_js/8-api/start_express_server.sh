#!/bin/bash

# Change directory to the correct location containing api.js
cd ~/holbertonschool-web_back_end/unittests_in_js/

# Start the Express server
node 8-api/api.js &

# Wait for the server to start
sleep 2

# Make a request to the server and get the response length
LENGTH=$(curl -s http://localhost:7865 | wc -c)

# Output the length of the response
echo "[$LENGTH]"
