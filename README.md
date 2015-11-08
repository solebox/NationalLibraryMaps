# National Library Maps Project



## Development
---
There is a vagrantfile you can use.
First clone the project, then type `vagrant up` to get and install the virtual machine - this will also install pip and the libraries and depencies into the virtual machine.

After that runs, type `vagrant ssh` to login and then you can
`cd /srv/website` and `python manage.py runserver 0.0.0.0:8000`
