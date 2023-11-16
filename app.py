from flask import Flask, request, session
from redis import Redis

app = Flask(__name__)
app.secret_key = 'super secret key'
SESSION_TYPE = 'filesystem'
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
	redis.incr('hits')
	counter = str(redis.get('hits'),'utf-8')
	return "Welcome to this webpage!, This webpage has been viewed "+counter+" time(s)"

@app.before_request
@app.route('/notes', methods = ['POST', 'GET'])
def handle_notes():
	app.logger.debug('Body: %s', request.get_data())
	if request.method == 'GET':
		user = request.args.get("user")
		app.logger.debug("user: " + user)
		note = redis.get(user)
		app.logger.debug("redis key: " + user)
		return note.decode('utf-8') if note else "No Note Found"

	if request.method == 'POST':
		#each time post is called, increment the user count
		redis.incr('posthits')
		postCounter = str(redis.get('posthits'),'utf-8')
		user = "user" + postCounter

		# This code creates a vunerability
		# It allows an attacker to modify any user's data
		if request.args.get("user") is not None:
			user = request.args.get("user")

		posted_note = request.data.decode('utf-8')
		#set userID to the the data given in post
		#EX: user3 = mwalravens
		redis.set(user, posted_note)
		app.logger.debug("redis key: " + user)
		app.logger.debug("redis value: " + posted_note)
		return {"ID": "user" + postCounter}


if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)