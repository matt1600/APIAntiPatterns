# APIAntiPatterns

## How to install

Clone from  the Github repository.
```
git clone git@github.com:matt1600/APIAntiPatterns.git
```

Run using Docker Compose.
```
cd APIAntiPatterns
docker-compose up
```

Test welcome page in browser.
```
http://0.0.0.0:5000
```

Open a new shell window, but leave previous one running. 

POST using curl. This simulates user data being entered into Redis.

Insert a username into the JSON field.

In this example, the username is mattwalravens.
```
curl -X POST 'http://0.0.0.0:5000/notes' -H 'Content-Type: application/json' -d '{"mattwalravens"}'
```

Repeat this command 2x with different usernames.

In browser, simulate hacker guessing ID number and retrieving username.
```
http://0.0.0.0:5000/notes?user=user1
```
Do the same for user2 and user3.

POST using CURL again. 

Hacker successfully changes user1 data within Redis.
```
curl -X POST 'http://0.0.0.0:5000/notes?user=user1'  -H 'Content-Type: application/json' -d 'hacker changed this'
```

Check browser to see that hacker succeeded.
```
http://0.0.0.0:5000/notes?user=user1
```





