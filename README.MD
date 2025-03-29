# Project setup guide

## First-time setup

### Start the project with Docker Compose:
```bash
docker-compose up --build
```

### Post-startup steps (open a second terminal)

#### Create a superuser:
```bash
docker-compose exec web python manage.py createsuperuser
```

#### Insert data from a file (e.g. .json):
```bash
docker-compose exec web python manage.py loaddata <datafile>
```

#### Run any python script (e.g. setting user passwords):
```bash
docker-compose exec web python <filename>.py
```

---

## Subsequent runs

### Start the project:
```bash
docker-compose up
```

### Stop and remove Docker Containers & Volumes:
```bash
docker-compose down --volumes
```

### Rebuilding the project will ask for permissions to database

#### Give permissions to database:
```bash
sudo chmod -R 755 ./data/db
```

#### Or delete the database:
```bash
sudo rm -r ./data/db
```

