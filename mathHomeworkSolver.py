import requests
import json


def solveBasic():
    print("_ _ _")
    one = int(input("|_| _ _:  "))
    opr = input(str(one)+" |_| _  (+  - X ÷): ")
    two = int(input(str(one)+" "+opr+" |_|:  "))
    print(one,opr,two,"=",end=" ")
    if opr == "÷":
        print(one/two)
    elif opr == "X":
        print(one*two)
    elif opr == "-":
        print(one-two)
    elif opr == "+":
        print(one+two)
    else:
        print("Invalid Operation")



def solveWithLargeLangugeModels(q):
    # Welcome message
    #say("Welcome to ChatGPT, please ask your question:")
    #print("Welcome to ChatGPT, please ask your question:")

    # Record the voice command to an mp3 file using ffmpeg
    #audio_input()

    # Send the voice command mp3 to OpenAI Whisper for transcription
    #voice_to_text_WhisperAI('voice_cmd.mp3')

    print(q)
    #say(question)

    print("Answer:",end=" ")

    # Send the transcribed question to OpenAI's GPT-3.5 Turbo for a reply
    response = requests.post(
        'https://api.openai.com/v1/chat/completions',
        headers={
            'Authorization': 'Bearer sk-proj-8FgGmj7gL6UNLTtU4tpBT3BlbkFJ7rGJcj1a9DPpJxNnGwRo',
            'Content-Type': 'application/json'
        },
        data=json.dumps({
            'model': 'gpt-3.5-turbo',
            'messages': [{'role': 'user', 'content': q}]
        })
    )
    answer = response.json().get('choices', [])[0]['message']['content']

    print(answer)
    #say(answer)
solveWithLargeLangugeModels(input())
