from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"perfectus": "Greetings from the Asynchronous Realm of FastAPI!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
