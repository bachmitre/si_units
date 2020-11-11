SI Units
-

### To run:

The docker container can be run in 2 different modes, depending on how the environment variable `ENV` is set:

 - per **default** a uwsgi server with 5 workers will be started (number of workers can be adjusted with `WORKERS` env variable)
 - with `ENV=debug` a single threaded flask debug server will be started


Either way, the server will listen on port `8000`

---
 
Build image:

```docker build .```

Start API in **production** mode:
 
```docker run --restart=always -d -p "8000:8000" <image_id>```


Start API in **production** mode with 20 workers:

```docker run --rm -it -e WORKERS=20 -p8000:8000 <image_id>```

Start API in **debug** mode:
 
```docker run --rm -it -e ENV=debug -p "8000:8000" <image_id>```

Run **test cases**:

```docker run --rm -it <image_id> pytest```

---

### Example api call

```curl "http://localhost:8000/units/si?units=(h*min)"```

Response:

```{"unit_name": "(s*s)", "multiplication_factor": 216000.0}```

---

###         Files in this repo:

- scripts/start_service.sh: command run in docker container to start api
- service/main.py: conversion code and api
- service/wsgi.py: needed for the uwsgi server
- tests/test_conversion.py: test cases
- Dockerfile: to create python3 environment with dependencies
- README.md: this file
- requirements.txt: dependencies 
