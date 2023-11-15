# APIAntiPatterns

## How to install

Clone from  the Github repository.
```
git clone git@github.com:matt1600/APIAntiPatterns.git
```

Run using Docker Compose
```
cd APIAntiPatterns
docker-compose up
```

Test the Flask App using CURL
```
curl 0.0.0.0:5000
```
POST using CURL
```
curl -X POST http://0.0.0.0:5000/notes -H 'Content-Type: application/json' -d '{"note_text":"test note"}'
```

