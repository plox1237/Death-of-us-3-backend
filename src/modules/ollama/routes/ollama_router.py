from fastapi import APIRouter
from src.modules.ollama.controllers.ollama_controller import handle_ollama
from src.modules.ollama.schema.ollama_schema import OllamaRequest

ollama_router = APIRouter()

@ollama_router.post("/chat")
async def chat(data: OllamaRequest):
    return await handle_ollama(data.prompt)