#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static
sudo apt update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'
sudo ufw enable

sudo mkdir -p /data/web_static/{shared,releases/test}
sudo chmod -R 755 /data/web_static/{shared,releases/test}
#sudo mkdir -p -m=755 /data/web_static/{releases/test,shared}

INDEX=\
"<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"
bash -c "echo -e '$INDEX' | sudo tee '/data/web_static/releases/test/index.html' > /dev/null"

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/

cp /etc/nginx/sites-available/default ./nginx_sites-available_default.backup

#target='location / {'
#insert='\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;}'
#sudo sed -i "$insert" /etc/nginx/sites-available/default
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx restart
exit 0
