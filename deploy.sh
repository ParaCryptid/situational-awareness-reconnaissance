#!/bin/bash
echo "Deploying situational-awareness-reconnaissance..."

# Navigate to the repository directory
cd /var/www/situational-awareness-reconnaissance

# Pull latest changes
git pull origin main

# Install dependencies (modify as per project needs)
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
elif [ -f "package.json" ]; then
    npm install
fi

# Restart service (modify based on actual setup)
sudo systemctl restart situational-awareness-reconnaissance.service

echo "situational-awareness-reconnaissance deployed successfully!"
