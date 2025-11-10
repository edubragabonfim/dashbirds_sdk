from pydantic_core import BaseModel, Field


class ClearBlogTextResponse(BaseModel):
    """Response from LLM, return in JSON format"""
    texto_limpo: str = Field(description="Texto limpo após a atuação do agente.")
    