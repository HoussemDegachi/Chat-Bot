from colorama import Fore
import openai

# Chat Class
class Chat:
    def __init__(self):
        self.messages = []
    
    def append(self, role, content):
        messages: list = self.messages
        messages.append({"role": role, "content": content})

def main() -> None:
    # variables
    chat = Chat()

    # pass api key
    openai.api_key = "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"

    # forever
    while True:
        # gets a request question from user and append it to messages
        request_question: str = input(Fore.WHITE + "User: ")
        chat.append("user", request_question)
        
        # gets response message for that request question
        response: dict = get_response(chat.messages)
        response_message: str = response['choices'][0]['message']['content']

        # append response to messages
        chat.append("assistant", response_message)

        # validate response message
        response_status: str = response["choices"][0]["finish_reason"]
        if response_status == "content_filter":
            print("Question not awnsered due to content filtering\ntry to ask an appropriate question")
            pass

        # print awnser
        if response_status == "stop":
            print(Fore.RED + f"Assistant: {response_message}")

def get_response(messages: list) -> dict:
    # call chatgpt
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages 
    )
    # return response as dict
    return response


if __name__ == "__main__":
    main()