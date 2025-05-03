from fastapi import APIRouter, Depends, HTTPException
from services.google_gmail_services import (
    list_messages,
    get_message
)
from services.openai_services import get_openai_response

router = APIRouter(tags=["mail"])

@router.get("/messages", summary="List Gmail Messages")
async def list_gmail_messages(
    user_id: str = 'me',
    max_results: int = 1
):
    """List messages from the user's Gmail account"""
    try:
        messages = list_messages(user_id=user_id, max_results=max_results)
        email_list = []
        for message in messages:
            full_msg = get_message(user_id=user_id, msg_id=message['id'])
            res = await get_openai_response(full_msg['body'])
            email_list.append(res)
        return email_list
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to list messages: {str(e)}")