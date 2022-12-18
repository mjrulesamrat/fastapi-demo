# Example FastAPI

- Run application using

  ```bash
  $ uvicorn main:app

  # build image
  $ docker build -t fastapi-demo .

  # run in local
  $ docker run -p 8080:8000 fastapi-demo

  # try out in local
  $ curl http:localhost:8080/
  ```
