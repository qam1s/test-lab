from fastapi import FastAPI, Response

app = FastAPI(title="App", version="1.0.0")


@app.get("/health")
def health():
    return Response(status_code=200)
