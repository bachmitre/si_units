SI Units
-

###To run:

The docker container can be run in 2 different modes, depending on how the environment variable `ENV` is set:

`ENV=debug` will start a flask debug server

`ENV=no-debug` will start a uwsgi server with 5 workers

Either way, the server will listen on port `8000`

---
Run using `docker compose`:

Start API:
 

```docker-compose up app```

Run the test cases:

```docker-compose run --rm tests``` 

----
Run using `docker`:
 
Build image:

```docker build .```

Start API:
 

```docker run --rm -v $(pwd):/app -e "ENV=debug" -p "8000:8000" <image_id> sh ./scripts/start_service.sh```

Run test cases:

```docker run --rm -v $(pwd):/app <image_id> pytest```

---

### Example api call

```curl "http://localhost:8000/units/si?units=(h*min)"```

Response:

```{"unit_name": "(s*s)", "multiplication_factor": 216000.0}```

---
###Files in this repo:

- scripts/start_service.sh: command run in docker container to start api
- service/main.py: conversion code and api
- service/wsgi.py: needed for the uwsgi server
- tests/test_conversion.py: test cases
- docker-compose.yml: docker run specifications
- Dockerfile: to create python3 environment with dependencies
- README.md: this file
- requirements.txt: dependencies 
