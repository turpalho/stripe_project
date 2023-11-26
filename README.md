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

Get stripe keys on your [Dashboard](https://dashboard.stripe.com/).
Assign the following environment variables in the .env file:
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


Create a superuser to use Django admin:

```
    docker exec -it --env PYTHONUNBUFFERED=1 stripe_container python manage.py createsuperuser
```
