import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion, AzureChatCompletion

class AIService:
    
    def __init__(self):
        api_key, org_id = sk.openai_settings_from_dot_env()
        self.kernel = sk.Kernel()
        self.kernel.add_chat_service("chat-gpt", OpenAIChatCompletion("gpt-3.5-turbo", api_key, org_id))
        
    def get_answer(self, question):
        prompt = self.kernel.create_semantic_function(f"{question}")
        # print(prompt())
        result = prompt()
        print(result)
        return result