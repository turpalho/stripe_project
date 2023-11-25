# stripe_project


INSTALLATION
------------

Copy the repository to your directory with the command:

```
    $ git clone https://github.com/turpalho/stripe_project.git
```

QUICK START
-----------



Make a copy of .env.dist and remove .dist:
```
    .env
    .env.dist
```

Get stripe keys in stripe dashboard [Dashboard](https://dashboard.stripe.com/).
Assign the token to a variable in the .env file and your user id to a vatiable "ADMINS":
```
    STRIPE_SECRET_KEY=your_public_key
    STRIPE_PUBLIC_KEY=your_secret_key
```


Run docker-compose

```
    $ docker-compose build
```
```
    $ docker-cimpose up -d
```


Create superuser to use Django admin:

```
    docker exec -it --env PYTHONUNBUFFERED=1 stripe_container python manage.py createsuperuser
```
