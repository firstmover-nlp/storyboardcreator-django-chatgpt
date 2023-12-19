from openai import OpenAI
import time
import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv('apikey.env')

client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))
#https://platform.openai.com/assistants 이 사이트에서 Assistant 관리
# tour_assistant_id = 'asst_1RJLGQL89XLqAhC6S3oziglU'
TOUR_ASSISTANT_ID = os.getenv("Tour_assistant_id")  
Denis_ASSISTANT_ID = os.getenv("Denis") 
Remy_ASSISTANT_ID = os.getenv("Remy") 
Mylo_ASSISTANT_ID = os.getenv("Mylo") 
Eugene_ASSISTANT_ID = os.getenv("Eugene") 
Camila_ASSISTANT_ID = os.getenv("Camila") 
Dave_ASSISTANT_ID = os.getenv("Dave") 



#최초 thread를 만들고 메시지를 연결한 후 답을 구한다 
def create_thread_and_run(user_input, thread):
    #thread = client.beta.threads.create()
    run = submit_message(TOUR_ASSISTANT_ID, thread, user_input)
    return thread, run

def denis_create_thread_and_run(user_input, thread):
    #thread = client.beta.threads.create()
    run = submit_message(Denis_ASSISTANT_ID, thread, user_input)
    return thread, run

def remy_create_thread_and_run(user_input, thread):
    #thread = client.beta.threads.create()
    run = submit_message(Remy_ASSISTANT_ID, thread, user_input)
    return thread, run

def mylo_create_thread_and_run(user_input, thread):
    #thread = client.beta.threads.create()
    run = submit_message(Mylo_ASSISTANT_ID, thread, user_input)
    return thread, run

def eugene_create_thread_and_run(user_input, thread):
    #thread = client.beta.threads.create()
    run = submit_message(Eugene_ASSISTANT_ID, thread, user_input)
    return thread, run

def camila_create_thread_and_run(user_input, thread):
    #thread = client.beta.threads.create()
    run = submit_message(Camila_ASSISTANT_ID, thread, user_input)
    return thread, run

def dave_create_thread_and_run(user_input, thread):
    #thread = client.beta.threads.create()
    run = submit_message(Dave_ASSISTANT_ID, thread, user_input)
    return thread, run

#해당 메시지를 대화 thread에 연결시키고 메시지의 답을 구한다.
def submit_message(assistant_id, thread, user_message):
    client.beta.threads.messages.create(
        thread_id=thread, role="user", content=user_message
#        thread_id=thread.id, role="user", content=user_message
    )
    return client.beta.threads.runs.create(
        thread_id=thread,
#        thread_id=thread.id,

        assistant_id=assistant_id,
    )

#현재 thread의 메시지 전체를 출력한다
def get_response(thread):
    return client.beta.threads.messages.list(thread_id=thread, order="asc")
#    return client.beta.threads.messages.list(thread_id=thread.id, order="asc")


# Pretty printing helper
def pretty_print(messages):
    file1 = open("C:\\Python\\django\\templates\\MyFile1.txt","a")
    print("# Messages")
    str =""
    for m in messages:
        str = str + m.role + ' : ' + m.content[0].text.value + "\n"
        print('Msg :' , str)
        #print(f"{m.role}: {m.content[0].text.value}")
        #file1.write(m.role + ':' + m.content[0].text.value)
    file1.write(str)     
    file1.close()
    return str


def answer_print(messages):
    #print(type(messages))
    for m in messages :
        pass

    return m.content[0].text.value

def record_image_to_thread(thread_id, image_url):
    message_content = f"Generated Image: {image_url}"
    client.beta.threads.messages.create(
        thread_id=thread_id, 
        role="system", 
        content=message_content
    )


#답을 가져올 때까지 기다리는 함수
def wait_on_run(run, thread):
    while run.status == "queued" or run.status == "in_progress":
        run = client.beta.threads.runs.retrieve(
            thread_id=thread,
#            thread_id=thread.id,
            run_id=run.id,
        )
        time.sleep(0.5)
    return run

'''thread1, run1 = create_thread_and_run(
    "부산에서 관광할 만한 다섯곳 추천해주세요"
)
run1 = wait_on_run(run1, thread1)
pretty_print(get_response(thread1))

run2 = submit_message(TOUR_ASSISTANT_ID, thread1, "첫번째 장소를 추천한 이유는?")
run2 = wait_on_run(run2, thread1)
pretty_print(get_response(thread1))
'''