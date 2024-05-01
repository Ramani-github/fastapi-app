from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

# Define a GET endpoint for /health
@app.get("/health")
async def health():
    return {"status": "up"}

