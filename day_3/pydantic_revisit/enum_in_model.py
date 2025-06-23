from enum import Enum
from pydantic import BaseModel


class ModelType(str, Enum):
    gpt35 = "gpt-3.5-turbo"
    gpt4 = "gpt-4"
    llama2 = "llama-2"

    def model_context_window(self):
        return {
            ModelType.gpt4: 4096,
            ModelType.gpt35: 8192,
            ModelType.llama2: 4096,
        }[self]

    def per_token_cost(self):
        return {
            ModelType.gpt4: 0.4,
            ModelType.gpt35: 0.3,
            ModelType.llama2: 0.2,
        }[self]


class LLMMRequest(BaseModel):
    model: ModelType
    prompt: str


req = {
    'model': 'gpt-3.5-turbo',
    'prompt': 'hellow dear',
}
obj = LLMMRequest(**req)
print(obj.model)
# print(ModelType.llama2.model_context_window())
# print(ModelType.llama2.per_token_cost())
