import os
import json
from dotenv import load_dotenv

load_dotenv()

OPENAI_KEY = os.getenv("OPENAI_API_KEY", "")
if OPENAI_KEY:
    try:
        from openai import OpenAI
        client = OpenAI(api_key=OPENAI_KEY)
    except Exception:
        client = None
else:
    client = None

class LLMTool:
    def __init__(self):
        self.client = client
        self.mode = "real" if client else "mock"

    def complete(self, prompt: str):
        if self.mode == "mock":
            if "priority" in prompt or "suggest priority" in prompt:
                return {"priority": "Medium"}
            return {"tests": [{"name": "smoke_test", "steps": ["start app", "check health"]}]}
        resp = self.client.responses.create(model="gpt-4o-mini", input=prompt)
        text = getattr(resp, "output_text", None) or getattr(resp, "text", "")
        try:
            return json.loads(text)
        except Exception:
            return {"text": text}
