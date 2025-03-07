#Inducil, Raphael Clouiee A.
#BsCpE 1-2
#february 27, 2025
#DeepSeek Integration

#This program is a chatbot that uses the DeepSeek API to generate responses to user questions. The user can ask questions and the chatbot will generate a response using the DeepSeek API. The chatbot will continue to generate responses until the user decides to stop.
>>>>>>> 8b611eb (Updated commit with new changes)
import requests
import json

while True:
  Question = input(str("What is your question?"))

  response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
      "Authorization": "Bearer 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",

    },
    data=json.dumps({
      "model": "deepseek/deepseek-r1:free", 
      "messages": [ 

        {
          "role": "user",
          "content": Question
        }
      ]
    })
  )

  if response.status_code == 200:
            result = response.json()
            choices = result.get("choices", [])

            if choices and "message" in choices[0] and "content" in choices[0]["message"]:
                content = choices[0]["message"]["content"]
                if content.strip():
                    print("Response:", content)
                else:
                    print("No response generated.")
            else:
                print("Invalid response format.")
  else:
      print("Error")
      
  more_questions = input("Do you have another question? (yes/y or no/n): ").lower()
  if more_questions not in ["yes", "y"]:
    break