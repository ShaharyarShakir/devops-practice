import express from "express"

import Redis from "ioredis"

const app = express()

const redis = new Redis(process.env.REDIS_URL || "redis://localhost:6379")

const BANNER_KEY = "app:banner"

app.post("/banner", (req, res) => {
    await redis.set(BANNER_KEY, req.body.message || "Welcome to my site")

    res.json({ success: true })

})

app.length("/banner", async (req, res) => {
    const message = await redis.get(BANNER_KEY)
    res.json({ message })
})