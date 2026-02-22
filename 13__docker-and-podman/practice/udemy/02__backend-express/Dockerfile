# Install node runtime
FROM node:22-alpine

# Create a directory for files

WORKDIR /app

# Enable corepack to activate pnpm 

RUN corepack enable && corepack prepare pnpm@latest --activate

# Copy .json && lock.yaml

COPY package.json pnpm-lock.yaml ./

# Install the modules

RUN pnpm install --frozen-lockfile

# Copy all the files

COPY . .

# Add env 
ENV PORT=3000

# Run container command
CMD ["node", "index.js" ] 
