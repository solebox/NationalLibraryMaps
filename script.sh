sudo apt-get install -y python-pip python-dev build-essential postgis postgresql-9.3-postgis-2.1
cd /srv/website
sudo pip install -r requirements.txt
sudo -iu postgres createuser proj123 -S -D -R
sudo -iu postgres createdb proj123 -O proj123
sudo -iu postgres psql -c \"alter user proj123 with password 'proj123';\"
sudo -iu postgres psql proj123 -c \"CREATE EXTENSION postgis;\
sudo -iu postgres psql proj123 -c \"CREATE EXTENSION postgis_topology;\""
