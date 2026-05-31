FROM alpine:latest

WORKDIR /opt

COPY requirements.txt .
RUN apk update
RUN apk add python3 curl
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

# Command to start the service. Set in ECS task definition.
# CMD ["gunicorn", "-b0.0.0.0:8000", "app:app"]
