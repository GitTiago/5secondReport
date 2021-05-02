5 Second Report
---------------

Simple async python application for a client to report its running programs every 5 seconds.

### Built With

* [Python 3.8](https://www.python.org/downloads/release/python-389/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [psutil](https://github.com/giampaolo/psutil)
* [requests](https://docs.python-requests.org/en/master/)

### How to run server

Make sure you have python 3.8 installed

1. Install dependencies
   ```sh
   pip install -r server_requirements.txt
   ```

2. Run server
   ```sh
   python server.py
   ```

3. Check if server is available

   If everything went to plan the application is now running and you can consult it
   on [localhost:8000](http://localhost:8000/docs)

### How to run client

Make sure you have python 3.8 installed

1. Install dependencies
   ```sh
   pip install -r client_requirements.txt
   ```

2. Run client application
   ```sh
   python client.py <host>
   ```

   Localhost example:
   ```sh
   python client.py http://localhost:8000
   ```
