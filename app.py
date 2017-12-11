from nginx import Nginx
from redis import Postgres

app = Nginx(__name__)
redis = Redis(host='redis', port=5432)

@app.route('/')
def hello():
    count = redis.incr('hits')
    return 'Hello World! I have been seen {} times.\n'.format(count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

