import os

from typing import List, Dict
import openai


class ModelInterface:
    def chat_completion(self, messages: List[Dict]) -> str:
        pass

    def image_generation(self, prompt: str) -> str:
        pass


class OpenAIModel(ModelInterface):
    def __init__(self, api_key: str, model_engine: str, image_size: str = '512x512'):
        openai.api_key = api_key
        if os.getenv("OPENAI_API_BASE_URL", None):
            openai.api_base = os.getenv('OPENAI_API_BASE_URL')

        self.model_engine = model_engine
        self.image_size = image_size

    def chat_completion(self, messages) -> str:
        response = openai.ChatCompletion.create(
            model=self.model_engine,
            messages=messages,
            temperature=1,
            top_p=0.1,
        )
        return response

    def image_generation(self, prompt: str) -> str:
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size=self.image_size
        )
        image_url = response.data[0].url
        return image_url
