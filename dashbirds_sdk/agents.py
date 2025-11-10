from langchain.agents import create_agent

from .prompts import CLEAR_TEXT_PROMPT
from .response_formats import ClearBlogTextResponse

clear_text_agent = create_agent(
    'openai:gpt-4o-mini',
    name='CLEAR_TEXT_AGENT',
    system_prompt=CLEAR_TEXT_PROMPT,
    response_format=ClearBlogTextResponse
)