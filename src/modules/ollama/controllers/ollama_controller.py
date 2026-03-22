from fastapi.responses import JSONResponse
from src.modules.ollama.services.ollama_service import ask_ollama


async def handle_ollama(prompt: str):
	try:
		response = await ask_ollama(prompt)
		return JSONResponse(
			content={
				"response": response
			},
			status_code=200
		)
	except Exception as e:
		return JSONResponse(
			content={
				"error": str(e)
			},
			status_code=500
		)
