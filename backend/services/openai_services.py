import re
import json
import os
import logging
from typing import Dict, Any, Optional
from fastapi import HTTPException
from dotenv import load_dotenv
from openai import OpenAI, OpenAIError

load_dotenv()
logger = logging.getLogger(__name__)

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    logger.critical("OPENAI_API_KEY environment variable is not set")
    raise RuntimeError("OPENAI_API_KEY environment variable is not set")

client = OpenAI(api_key=OPENAI_API_KEY)

async def get_openai_response(mail: str):
    """Get OpenAI response if mail content contains phishing attack"""
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a phishing detection assistant. Analyze the email content and determine if it contains a phishing attack. Format as JSON with 'is_phishing' key as boolean and 'reason' key as string."
                },
                {
                    "role": "user",
                    "content": mail
                }
            ],
        )
        
        content = response.choices[0].message.content
       
        # Extract JSON from the response
        match = re.search(r"```json\s*({[\s\S]*?})\s*```", content)
        if not match:
            match = re.search(r"({[\s\S]*?})", content)
        
        if not match:
            logger.warning(f"Could not extract JSON from OpenAI response: {content}")
            raise ValueError("JSON object not found in response.")

        event_data = json.loads(match.group(1))
        
        return {
            "mail": mail,
            "response": event_data,
        }
    except OpenAIError as e:
        logger.error(f"OpenAI API error: {e}")
        raise HTTPException(status_code=500, detail="OpenAI API error")