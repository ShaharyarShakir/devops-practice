# ---- Stage 1 ---- Build Stage
FROM node:22-alpine AS builder

WORKDIR /app

RUN corepack enable && corepack prepare pnpm@latest --activate

COPY package.json pnpm-lock.yaml ./

RUN pnpm install

COPY . .

# ---- Stage 2 ---- Production Stage
FROM node:22-alpine

WORKDIR /prod

COPY --from=builder /app /prod

EXPOSE 3000

ENV PORT=3000

CMD ["node", "index.js"]
