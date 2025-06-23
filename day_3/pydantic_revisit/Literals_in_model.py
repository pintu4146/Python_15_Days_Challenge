from pydantic import BaseModel
from typing import Literal


# used Literal from typing to simulate the choices of the variables

class LLMRequest(BaseModel):
    llm_model_types: Literal['gpt-3.5-turbo', 'gpt-4', 'llama-2']
    prompt: str


# valid cases
obj_llm_req = LLMRequest(llm_model_types='gpt-4', prompt='hello')
print(obj_llm_req)  # op -> llm_model_types='gpt-4' prompt='hello'

# invalid cases using diff choices than defined in the Literal List like gpt-5
try:
    invalid_choice = LLMRequest(llm_model_types='gpt-5', prompt='hello')
except ValueError as ve:
    print(f'value error occurred: {str(ve)}')
    """
    raised: value error occurred: 1 validation error for LLMRequest
llm_model_types
  Input should be 'gpt-3.5-turbo', 'gpt-4' or 'llama-2' [type=literal_error, input_value='gpt-5', input_type=str]
   
    For further information visit https://errors.pydantic.dev/2.11/v/literal_error
    """

# but what if when we will be dealing with the token cost of the model or context window of the model
