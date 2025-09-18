from fastapi import FastAPI
from pydantic import BaseModel

# A simple model for the chat request, as a placeholder
class ChatRequest(BaseModel):
    user_id: str
    message: str

app = FastAPI()

@app.get("/")
def read_root():
    """A root endpoint for health checks."""
    return {"status": "ok", "message": "Solar Recommender API is running."}

@app.post("/chat")
def chat(request: ChatRequest):
    """
    A placeholder chat endpoint.
    In the future, this will trigger the SuperAgent.
    """
    # For now, just echo the message back as a dummy response
    return {"response": f"Dummy response to your message: '{request.message}'"}
