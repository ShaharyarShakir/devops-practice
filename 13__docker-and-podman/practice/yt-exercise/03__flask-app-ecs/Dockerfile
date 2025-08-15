# Build stgae
FROM python:3.9 AS builder

WORKDIR /app 

# Install dependencies

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

# Production stage
FROM python:3.9-slim

WORKDIR /prod 

COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages

COPY . .

CMD ["python", "run.py"]
