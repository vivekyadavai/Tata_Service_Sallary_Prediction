web: gunicorn -w 4 -b 0.0.0.0:$PORT -k gevent app:app
heroku ps:scale web=1
web: bundle exec rails server thin -p $PORT -e $RACK_ENV
web: python myServer.py
port = int(os.environ.get('PORT', 5000))
