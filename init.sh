mv -T stepik-web-course web
sudo unlink /etc/nginx/sites-enabled/default
sudo rm /etc/nginx/nginx.conf
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/nginx.conf
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/etc/gunicorn-django.conf /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart
#sudo /etc/init.d/mysql start