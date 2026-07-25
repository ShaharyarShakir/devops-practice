import express from "express"
import Redis from "ioredis"

const app = express()
app.use(express.json())

const redis = new Redis(process.env.REDIS_URL || "redis://localhost:6379")

function OPTKey(phone) {
    return `opt:${phone}`
}

app.post('/opt', async (req, res) => {
    const { phone } = req.body
    const opt = Math.floor(100000 + Math.random() * 900000).toString()

    await redis.set(OPTKey(phone), opt, 'EX', 30) // OTP expires in 30 seconds
    res.json({ message: "OTP sent", opt })
})