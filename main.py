from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello Perfectus!"}

@app.get("/creative")
async def creative_message():
    return {"message": "Code is poetry written in the language of logic."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
