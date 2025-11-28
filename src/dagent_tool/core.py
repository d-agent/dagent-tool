import httpx

from dagent_tool.config import get_api_key, get_cookies
from dagent_tool.models import Requirement

API_URL = "https://api.dagent.dev/dagent"

async def run_api(requirements: Requirement, text: str, is_new_session: bool = False) -> dict:

    # get cookies from the user's project
    agent_id = get_cookies().get('agent_id')
    api_key = get_api_key()
    if not api_key:
        raise ValueError("DAGENT_API_KEY is missing. Add it in your .env file.")
        
    if not agent_id:
        payload = {
        "requirements": requirements.model_dump(),
        "text": text,
        "is_new_session": is_new_session
        }
    else:
        payload = {
            "text": text,
            "agent_id": agent_id
        }
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "x-api-key":api_key
    }

    # Use extended timeout for AI agent API calls which may take longer to process
    timeout = httpx.Timeout(
        connect=10.0,    # Time to establish connection
        read=120.0,      # Time to wait for response data
        write=10.0,      # Time to send request data
        pool=10.0        # Time to acquire connection from pool
    )
    
    async with httpx.AsyncClient(timeout=timeout) as client:
        res = await client.post(API_URL, json=payload, headers=headers)
        res.raise_for_status()
        return res.json()

