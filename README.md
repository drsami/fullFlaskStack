# fullFlaskStack

The goal of this project is to provide a docker compose deployment with several containers 
to quickly deploy Flask applications which require SSL and a backend DB. 


### Tasks
 
[ ] - Container for drop in Flask application with build for requirments.txt
[ ] - Container for Nginx and certbot for SSL
[ ] - Container for database (MySQL)
[ ] - Container for DB admin app (phpmyadmin?)

### Running the basic flask app, mysql and phpmyadmin - no SSL

```docker run --name mydb -e MYSQL_ROOT_PASSWORD=12345 -d mysql```

```docker run --name myadmin -d --link mydb:db -p 8080:80 phpmyadmin/phpmyadmin```

```docker run --name flask -it --rm -p 5000:5000 --link mydb:db -v "$pwd/app:/app"  tycon/flaskapp```