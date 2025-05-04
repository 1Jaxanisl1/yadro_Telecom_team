FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y \
        python3 \
        python3-pip \
        && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY http_requests.py requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "python3", "./http_requests.py" ]