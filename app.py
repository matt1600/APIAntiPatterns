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

@app.route('/notes', methods = ['POST', 'GET'])
def handle_notes():
	if request.method == 'GET':
		note = redis.get("note")
		return note.decode('utf-8') if note else "No Note Found"


	if request.method == 'POST':
		posted_note = request.data
		f = open("log.txt", "a")
		f.write(request.data.decode('utf-8'))
		f.close()
		redis.set("note", posted_note)
		return {"note_id": 0}

if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)