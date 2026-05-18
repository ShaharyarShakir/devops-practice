import { Router } from "express";
import Redis from "ioredis"
import mongoose from "mongoose";

const router = Router()

const redis = new Redis(process.env.REDIS_URL || "redis://localhost:6379")
const url = process.env.MONGO_URL || "mongodb://localhost:27017/mongo_redis_db"

router.get("/redis", async (req, res) => {
    const reply = await redis.ping()
    res.json({ redis: reply })
})

router.get("/mongo", async (req, res) => {
    if (mongoose.connection.readyState === 0) await mongoose.connect(url)


    res.json({ mongo: "connected", database: mongoose.connection.name })

})

export default router
