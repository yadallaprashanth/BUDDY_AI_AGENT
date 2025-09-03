from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from dotenv import load_dotenv
from livekit import agents
from livekit.agents import Agent, AgentSession, RoomInputOptions
from livekit.plugins import noise_cancellation
from prompts import AGENT_INSTRUCTION, SESSION_INSTRUCTION
from tools import get_weather, search_web, send_email

load_dotenv()
app = FastAPI()


# 🔹 Define request/response models
class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    reply: str


# 🔹 Assistant definition
class Assistant(Agent):
    def __init__(self) -> None:
        # Lazy import avoids plugin crash
        from livekit.plugins import google
        super().__init__(
            instructions=AGENT_INSTRUCTION,
            llm=google.beta.realtime.RealtimeModel(
                voice="Aoede",
                temperature=0.8,
            ),
            tools=[get_weather, search_web, send_email],
        )

    def run(self, message: str) -> str:
        # For demo purposes, just echo (replace with actual call to LiveKit session)
        return f"(LiveKit Assistant) You said: {message}"


assistant = Assistant()


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    reply = assistant.run(request.message)
    return ChatResponse(reply=reply)


if __name__ == "__main__":
    uvicorn.run("agent:app", host="0.0.0.0", port=8000, reload=False)
