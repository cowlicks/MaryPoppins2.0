# Mary Poppins 2.0

Mary Poppins provides an API to talk to Noisebridge.

Test her out:
```
$ pip install pyttsx flask
$ ./run.py
# Then in another shell
$ curl -H "Content-Type: application/json" -X POST -d '{"phrase":"Hello world!"}' http://localhost:5000/say
```
