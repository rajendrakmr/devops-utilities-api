# stage 1
FROM python:3.12 AS builder 

WORKDIR /apps

COPY requirements.txt .

RUN apt-get update 

RUN pip install --no-cache-dir -r requirements.txt  --target=/install

COPY . .

# stage 2

FROM python:3.12-slim AS deployer

WORKDIR /apps

COPY --from=builder /install /usr/local/lib/python3.12/site-packages

# Copy application code
COPY --from=builder /apps /apps

EXPOSE 8000

CMD [ "python", "main.py" ]