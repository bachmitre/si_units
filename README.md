SI Units
-

### To run:

The docker container can be run in **production** mode or in **debug** mode, depending on how the environment variable `ENV` is set:

 - per **default** a wsgi server with 5 workers will be started (number of workers can be adjusted with `WORKERS` env variable)
 - with `ENV=debug` a single threaded flask debug server will be started


Either way, the server will listen on port `8000`

Since the response of the api for any specific input does not change, once calculated it will be cached for future responses instead of re-calculated.
The size of the cache can be controlled by setting the environment variable `CACHE_SIZE`. If not set the cache size will default to 10000. 

In addition the response includes cache control headers to allow intermediate http caching. 

---
 
Build image:

```docker build .```

Start API in **production** mode:
 
```docker run --restart=always -d -p "8000:8000" <image_id>```


Start API in **production** mode with 20 workers:

```docker run --restart=always -d -e WORKERS=20 -p "8000:8000" <image_id>```

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
- service/cache_utils.py: utility function for http cache control
- service/conversion.py: conversion code
- service/main.py: api code
- service/wsgi.py: needed for gunicorn
- tests/test_conversion.py: test cases
- Dockerfile: to create python3 environment with dependencies
- README.md: this file
- requirements.txt: dependencies 
