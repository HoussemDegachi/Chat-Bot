import openai
import tkinter

# Chat Class
class Chat:
    def __init__(self):
        self.messages = []
    
    def append(self, role, content):
        messages: list = self.messages
        messages.append({"role": role, "content": content})

    def get_response(self, request_question) -> dict:
        self.append("user", request_question)
        # call chatgpt
        messages = self.messages
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = messages 
        )
        response_message = response['choices'][0]['message']['content']
        self.append("assistant", response_message)

        # return response as string
        return response_message

# variables
chat = Chat()

def main() -> None:
    # variables
    global chat

    # pass api key
    openai.api_key = "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"

    # create window
    root = tkinter.Tk()
    root.title("Python Bot")
    root.iconbitmap("wave.ico")
    root.geometry("350x400")
    root.resizable(False, False)

    # layout
    messages_output = tkinter.Frame(root, height = 350)
    user_input = tkinter.Frame(root, bg = "#cccccc", height = 50)

    # user input layout
    user_input_field = tkinter.Entry(user_input, width = 40)
    input_submit = tkinter.Button(user_input, text = "Send", command = lambda: send_request(user_input_field, messages_output))

    # display user input layout
    user_input_field.grid(column = 0, row = 0, ipady = 3, padx=(20, 10), pady = 10)
    input_submit.grid(column = 1, row = 0, ipadx = 14, pady = 10)

    # display layout
    messages_output.pack(fill = "both")
    messages_output.pack_propagate(False)
    user_input.pack(fill = "x", ipady = 20, ipadx = 10)

    # display window
    root.mainloop()

def send_request(input_field, frame):
    user_input = input_field.get()
    if user_input:
        # global variables
        global chat
        # loading = tkinter.Label(frame, text = "Thinking...", bg = "#00FF00", fg = "#FFFFFF")
        # loading.pack(ipadx = 3, ipady = 3, anchor = "center", side = "bottom")

        input_field.delete(0, tkinter.END)

        # add user's data
        tkinter.Label(frame, text = user_input, bg = "#808080", fg = "#E6E6E6").pack(anchor = "e", ipadx = 3, ipady = 3, padx = 6, pady = 6)

        # get response
        response = chat.get_response(user_input)
        tkinter.Label(frame, text = response, bg = "#4D4D4D", fg = "#E6E6E6").pack(anchor = "w", ipadx = 3, ipady = 3, padx = 6, pady = 6)

        # loading.pack_forget()


if __name__ == "__main__":
    main()