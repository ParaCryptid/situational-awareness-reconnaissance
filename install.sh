#!/bin/bash
echo "Installing OSINT..."

# Move to appropriate directory
sudo mkdir -p /var/www/OSINT
sudo chown $USER:$USER /var/www/OSINT
cd /var/www/OSINT

# Clone the repository
git clone https://github.com/ParaCryptid/OSINT.git .

# Install dependencies
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
elif [ -f "package.json" ]; then
    npm install
fi

# Create systemd service file
sudo bash -c 'cat <<EOF > /etc/systemd/system/OSINT.service
[Unit]
Description=OSINT Service
After=network.target

[Service]
ExecStart=/var/www/OSINT/start.sh
Restart=always
User=$USER
WorkingDirectory=/var/www/OSINT

[Install]
WantedBy=multi-user.target
EOF'

# Enable and start service
sudo systemctl enable OSINT.service
sudo systemctl start OSINT.service

echo "OSINT installed and running!"
