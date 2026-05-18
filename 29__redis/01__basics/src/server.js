import express from "express"
import healthRoute from './index.js'

const app = express()

app.use(healthRoute)

app.listen(3000, () => {
    console.log("Server running on port 3000");

})