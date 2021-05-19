web: gunicorn -w 4 -b 0.0.0.0:$PORT -k gevent app:app
heroku ps:scale web=1
web: bundle exec rails server thin -p $PORT -e $RACK_ENV
web: java -Dspring.profiles.active=default -Dserver.port=$PORT -jar target/*.jar
heroku scale web=1
