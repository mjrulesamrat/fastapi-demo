FROM python:3.7-slim
WORKDIR /app
ADD . ./
RUN pip install -r requirements.txt
EXPOSE 8000
CMD uvicorn main:app