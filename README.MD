## If the containers' volumes, exist Before building & running the project we should give permissions to data/db
```bash
sudo chmod -R 755 ./data/db
```


# For the 1st time
## Starting the project with docker-compose
```bash
docker-compose up --build
```


## After we have start the project we need to create a superuser for our database (in another terminal)
```bash
docker-compose exec web python manage.py createsuperuser
```

## If we want to insert data from a file (like .json)
```bash
docker-compose exec web python manage.py loaddata <datafile>
```

## If we want to run any python file while the project is running (for example to set passwords for users)
```bash
docker-compose exec web python <filename>.py
```


# For the next times 
## To start the project we can simply run
```bash
docker-compose up
```

## To delete docker containers and volumes
```bash
docker-compose down --volumes
```


## To delete the database
```bash
sudo rm -r ./data/db
```