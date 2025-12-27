from .groq_provider import generate_text as gpg
from .openrouter_provider import generate_text as opg


async def ai_generator(
    user_prompt: str,
    system_prompt: str = "You write concise, technical tweets.",
    priority: str = "fast",
) -> str:
    try:
        if priority == "fast":
            return await opg(user_prompt, system_prompt)
        return await gpg(user_prompt, system_prompt)

    except Exception:
        return (
            await gpg(user_prompt, system_prompt)
            if priority == "fast"
            else await opg(user_prompt, system_prompt)
        )
