#!/bin/bash
echo "Installing situational-awareness-reconnaissance..."

# Move to appropriate directory
sudo mkdir -p /var/www/situational-awareness-reconnaissance
sudo chown $USER:$USER /var/www/situational-awareness-reconnaissance
cd /var/www/situational-awareness-reconnaissance

# Clone the repository
git clone https://github.com/ParaCryptid/situational-awareness-reconnaissance.git .

# Install dependencies
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
elif [ -f "package.json" ]; then
    npm install
fi

# Create systemd service file
sudo bash -c 'cat <<EOF > /etc/systemd/system/situational-awareness-reconnaissance.service
[Unit]
Description=situational-awareness-reconnaissance Service
After=network.target

[Service]
ExecStart=/var/www/situational-awareness-reconnaissance/start.sh
Restart=always
User=$USER
WorkingDirectory=/var/www/situational-awareness-reconnaissance

[Install]
WantedBy=multi-user.target
EOF'

# Enable and start service
sudo systemctl enable situational-awareness-reconnaissance.service
sudo systemctl start situational-awareness-reconnaissance.service

echo "situational-awareness-reconnaissance installed and running!"
