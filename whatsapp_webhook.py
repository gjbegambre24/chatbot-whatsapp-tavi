from fastapi import FastAPI, Request

app = FastAPI()

VERIFY_TOKEN = "TAVI_TOKEN_123"  # usa el mismo token que configures en Meta

@app.get("/")
async def root():
    return {"message": "TAVI WhatsApp bot funcionando"}

@app.get("/webhook")
async def verify(request: Request):
    params = dict(request.query_params)
    if (
        params.get("hub.mode") == "subscribe"
        and params.get("hub.verify_token") == VERIFY_TOKEN
    ):
        return int(params.get("hub.challenge"))
    return "Error de verificación"

@app.post("/webhook")
async def receive_message(request: Request):
    data = await request.json()
    print("Mensaje entrante:", data)
    return {"status": "ok"}
