from flask import Flask, request, session
from redis import Redis

app = Flask(__name__)
app.secret_key = 'super secret key'
SESSION_TYPE = 'filesystem'
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
	return "Welcome!"

@app.route('/notes', methods = ['POST', 'GET'])
def handle_notes():
	#this statement returns user information if it has already been entered with curl post
	#returns "no note found" otherwise
	if request.method == 'GET':
		user = request.args.get("user")
		note = redis.get(user)
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
		#set userID to the the data given in the post comm
		#EX: user1 = mattwalravens
		redis.set(user, posted_note)
		return {"ID": "user" + postCounter}


if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)

	

