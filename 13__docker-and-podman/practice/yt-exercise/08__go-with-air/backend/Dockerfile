FROM golang:1.25-alpine

WORKDIR /app

# Install air
RUN go install github.com/air-verse/air@latest

# Copy go mod files
COPY go.mod  ./
RUN go mod download

# Copy source code
COPY . .

# Create tmp directory
RUN mkdir -p tmp

EXPOSE 5000

# Run as root
CMD ["/go/bin/air", "-c", ".air.toml"]
