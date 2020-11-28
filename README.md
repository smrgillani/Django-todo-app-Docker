Instructions

step 1 : docker-compose build
step 2 : docker run web
step 3 : docker-compose run web python manage.py migrate
step 4 : docker-compose run -p 8000:8000 web
