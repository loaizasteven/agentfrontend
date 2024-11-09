from openai import OpenAI

client = OpenAI()

def vehicle_detail_summary(api_details: dict) -> str:
    completion = client.chat.completions.create(
        model="gpt-4o-2024-08-06",
        messages=[
            {"role": "system", "content": "Extract the vehicle information and summarize."},
            {"role": "user", "content": f"{api_details}"},
        ],
    )
    return completion.choices[0].message.content
