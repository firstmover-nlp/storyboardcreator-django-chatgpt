from openai import OpenAI
import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv('apikey.env')

def qna(question) :
   
    client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

    messages = [ {"role": "system", "content": "You are a intelligent assistant."} ]
    messages.append(
                {"role": "user", "content": question},
            )
    
    chat = client.chat.completions.create(
    model="gpt-3.5-turbo-1106", messages=messages )
    
    return chat.choices[0].message.content
        
        
# def create_image(question):
#     client = OpenAI(api_key='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')

#     # DALL-E를 사용해 이미지 생성 요청
#     response = client.images.generate(prompt=question)

#     # 응답에서 이미지 URL 추출
#     if response.data:
#         image_url = response.data[0].url
#         return image_url
#     else:
#         return None

def create_image(prompt):
    client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        n=1,
    )
    
    # 이미지 URL을 추출하는 방식 변경
    if response.data and len(response.data) > 0:
        return response.data[0].url
    else:
        return None

