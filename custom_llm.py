import cohere
from typing import Any, List, Mapping, Optional

from langchain.callbacks.manager import CallbackManagerForLLMRun
from langchain.llms.base import LLM

co = cohere.Client('vJVaAxPgk9XYSuknSdmJBEtdSzl1uwAVsbizc7b8')  # This is your trial API key


class CustomLLM(LLM):
    model: str = '22dab3fa-06ed-40fa-b779-a86595ebbb92-ft'   # The custom model we used.
    @property
    def _llm_type(self) -> str:
        return "custom"

    def _call(self,prompt: str,stop: Optional[List[str]] = None,run_manager: Optional[CallbackManagerForLLMRun] = None,) -> str:
        """ This is where the main logic of the """
        if stop is not None:
            raise ValueError("stop kwargs are not permitted.")
        response = co.generate(model=self.model, prompt=f'{prompt}')

        return response.generations[0].text

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {"model_type": f'COHERE_CUSTOM-<{self.model}>'}


""" Now, this thing can be used as a custom LLM. Use it in the LLM Chain thing."""
