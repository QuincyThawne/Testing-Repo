from openai import OpenAI

file=open("aimlapi_key.txt","r")
key=file.read()

base_url = "https://api.aimlapi.com/v1"
api_key = key
system_prompt = "You are a police officer and i have a few queries. Be helpful."

while True:
    user_prompt=input("User:")


    api = OpenAI(api_key=api_key, base_url=base_url)

    completion = api.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        # temperature=0.7,
        # max_tokens=10,
    )

    response = completion.choices[0].message.content

    print("AI:", response)