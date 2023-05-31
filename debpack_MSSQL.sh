wget -q -O- https://packages.microsoft.com/keys/microsoft.asc | \
    gpg --dearmor | sudo tee /usr/share/keyrings/microsoft.gpg > /dev/null 2>&1
echo "deb [signed-by=/usr/share/keyrings/microsoft.gpg arch=amd64,armhf,arm64] https://packages.microsoft.com/ubuntu/20.04/mssql-server-2019 focal main" | \
    sudo tee /etc/apt/sources.list.d/mssql-server-2019.list
