from django.shortcuts import render
from django.http import HttpResponse
import fopenaiAPI1 
import audioplay
import ThreadAPI
from openai import OpenAI
import time
import asyncio
import httpx
from django.shortcuts import redirect
import os
from dotenv import load_dotenv

# # .env 파일 로드
# load_dotenv('apikey.env')

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



def gamepage(request):
    thread = client.beta.threads.create()
    file1 = open("C:\\Users\\dbalf\\Downloads\\KDT_Project\\NLP\\Django\\game\\thread2.txt","w+")
    thread = str(thread.id)
    file1.write(thread)
    file1.close()

    if request.method == 'POST':
        # POST 요청일 때 입력된 데이터를 가져옴
        # 'user_input'은 form에서 사용된 input 요소의 name 속성
        user_input = request.POST.get('user_input', '') 
        # 여기서 user_input을 사용하여 필요한 작업 수행
        ans = fopenaiAPI1.qna(user_input)
        return render(request, 'GPTinput.html', {'Data':ans})
 
    # GET 요청일 때는 그냥 페이지를 렌더링
    return render(request, 'GPTinput.html')

def threadtest(request):
    thread = client.beta.threads.create()
    file1 = open("C:\\Users\\dbalf\\Downloads\\KDT_Project\\NLP\\Django\\game\\thread4.txt","w+")
    thread = str(thread.id)
    file1.write(thread)

    file1 = open("C:\\Users\\dbalf\\Downloads\\KDT_Project\\NLP\\Django\\game\\thread4.txt","r+")
    thread = file1.read()
    file1.close()
    thread1, run1 = ThreadAPI.create_thread_and_run("", thread)
    run1 = ThreadAPI.wait_on_run(run1, thread1)
    # 세션에서 대화 내역을 가져옴
    conversation = request.session.get('conversation', [])

    if request.method == 'POST':
        if request.POST.get('action') == 'create_image':
            # 이미지 생성 요청 처리
            if conversation:
                last_conversation = conversation[-1]
                last_answer = last_conversation.get('answer')
                
                # GPT의 응답에 추가 지시문을 더함
                modified_input = last_answer + " 이 시나리오에 맞는 흑백의 러프하고 해상도 낮춰서 콘티 이미지를 생성해줘"
                
                # 이미지 생성 API 호출 (여기는 예시로 작성, 실제 API 호출 방식에 맞게 수정 필요)
                image_url = fopenaiAPI1.create_image(modified_input)

                # 생성된 이미지 URL을 대화 내역에 추가
                last_conversation['image_url'] = image_url
                request.session.modified = True

                return render(request, 'GPTinput2.html', {'conversation': conversation})
            else:
                # 대화 내역이 없는 경우 처리
                return render(request, 'GPTinput2.html', {'conversation': conversation, 'error': 'No conversation history found.'})

        elif request.POST.get('action') == 'clear_conversation':
            # 대화 내역 삭제
            request.session['conversation'] = []
            request.session.modified = True
            return redirect('threadtest')

        user_input = request.POST.get('user_input', '')
        run2 = ThreadAPI.submit_message(TOUR_ASSISTANT_ID, thread1, user_input)
        run2 = ThreadAPI.wait_on_run(run2, thread1)
        ans = ThreadAPI.answer_print(ThreadAPI.get_response(thread1))

        conversation.append({'question': user_input, 'answer': ans})
        request.session['conversation'] = conversation

    # 기본 페이지 표시
    return render(request, 'GPTinput2.html', {'conversation': conversation})



# def threadtest(request):
#     thread = client.beta.threads.create()
#     file1 = open("C:\\Users\\dbalf\\Downloads\\KDT_Project\\NLP\\Django\\game\\thread3.txt","w+")
#     thread = str(thread.id)
#     file1.write(thread)

#     file1 = open("C:\\Users\\dbalf\\Downloads\\KDT_Project\\NLP\\Django\\game\\thread3.txt","r+")
#     thread = file1.read()
#     file1.close()
#     thread1, run1 = ThreadAPI.create_thread_and_run("부산에서 관광할 만한 다섯곳 추천해주세요", thread)
#     run1 = ThreadAPI.wait_on_run(run1, thread1)
    
#     conversation = request.session.get('conversation', [])

#     if request.method == 'POST':
#         if request.POST.get('action') == 'clear_conversation':
#             # 대화 내역 삭제
#             request.session['conversation'] = []
#             request.session.modified = True  # 세션 변경 강제화
#             return redirect('threadtest')
#         user_input = request.POST.get('user_input', '')
#         run2 = ThreadAPI.submit_message(TOUR_ASSISTANT_ID, thread1, user_input)
#         run2 = ThreadAPI.wait_on_run(run2, thread1)
#         ans = ThreadAPI.answer_print(ThreadAPI.get_response(thread1))

#         conversation.append({'question': user_input, 'answer': ans})
#         request.session['conversation'] = conversation
        
#         return render(request, 'GPTinput2.html', {'conversation': conversation})
    
#     return render(request, 'GPTinput2.html', {'conversation': conversation})

def denis(request):
    thread = client.beta.threads.create()
    file1 = open("C:\\Users\\dbalf\\Downloads\\KDT_Project\\NLP\\Django\\game\\denis.txt","w+")
    thread = str(thread.id)
    file1.write(thread)

    file1 = open("C:\\Users\\dbalf\\Downloads\\KDT_Project\\NLP\\Django\\game\\denis.txt","r+")
    thread = file1.read()
    file1.close()
    thread1, run1 = ThreadAPI.denis_create_thread_and_run("", thread)
    run1 = ThreadAPI.wait_on_run(run1, thread1)
    # 세션에서 대화 내역을 가져옴
    denis_conversation = request.session.get('denis_conversation', [])

    if request.method == 'POST':
        if request.POST.get('action') == 'create_image':
            # 이미지 생성 요청 처리
            if denis_conversation:
                last_denis_conversation = denis_conversation[-1]
                last_answer = last_denis_conversation.get('answer')
                
                # GPT의 응답에 추가 지시문을 더함
                modified_input = last_answer + " 이 시나리오에 맞는 흑백의 러프하고 해상도 낮춰서 콘티 이미지를 생성해줘"
                
                # 이미지 생성 API 호출 (여기는 예시로 작성, 실제 API 호출 방식에 맞게 수정 필요)
                image_url = fopenaiAPI1.create_image(modified_input)

                # 생성된 이미지 URL을 대화 내역에 추가
                last_denis_conversation['image_url'] = image_url
                request.session.modified = True

                return render(request, 'denis.html', {'denis_conversation': denis_conversation})
            else:
                # 대화 내역이 없는 경우 처리
                return render(request, 'denis.html', {'denis_conversation': denis_conversation, 'error': 'No conversation history found.'})

        elif request.POST.get('action') == 'clear_denis_conversation':
            # 대화 내역 삭제
            request.session['denis_conversation'] = []
            request.session.modified = True
            return redirect('denis')

        user_input = request.POST.get('user_input', '')
        run2 = ThreadAPI.submit_message(Denis_ASSISTANT_ID, thread1, user_input)
        run2 = ThreadAPI.wait_on_run(run2, thread1)
        ans = ThreadAPI.answer_print(ThreadAPI.get_response(thread1))

        denis_conversation.append({'question': user_input, 'answer': ans})
        request.session['denis_conversation'] = denis_conversation

    # 기본 페이지 표시
    return render(request, 'denis.html', {'denis_conversation': denis_conversation})

def remy(request):
    thread = client.beta.threads.create()
    file1 = open("C:\\Users\\dbalf\\Downloads\\KDT_Project\\NLP\\Django\\game\\remy.txt","w+")
    thread = str(thread.id)
    file1.write(thread)

    file1 = open("C:\\Users\\dbalf\\Downloads\\KDT_Project\\NLP\\Django\\game\\remy.txt","r+")
    thread = file1.read()
    file1.close()
    thread1, run1 = ThreadAPI.remy_create_thread_and_run("", thread)
    run1 = ThreadAPI.wait_on_run(run1, thread1)
    # 세션에서 대화 내역을 가져옴
    remy_conversation = request.session.get('remy_conversation', [])

    if request.method == 'POST':
        if request.POST.get('action') == 'create_image':
            # 이미지 생성 요청 처리
            if remy_conversation:
                last_remy_conversation = remy_conversation[-1]
                last_answer = last_remy_conversation.get('answer')
                
                # GPT의 응답에 추가 지시문을 더함
                modified_input = last_answer + " 이 시나리오에 맞는 흑백의 러프하고 해상도 낮춰서 콘티 이미지를 생성해줘"
                
                # 이미지 생성 API 호출 (여기는 예시로 작성, 실제 API 호출 방식에 맞게 수정 필요)
                image_url = fopenaiAPI1.create_image(modified_input)

                # 생성된 이미지 URL을 대화 내역에 추가
                last_remy_conversation['image_url'] = image_url
                request.session.modified = True

                return render(request, 'Remy.html', {'remy_conversation': remy_conversation})
            else:
                # 대화 내역이 없는 경우 처리
                return render(request, 'remy.html', {'remy_conversation': remy_conversation, 'error': 'No conversation history found.'})

        elif request.POST.get('action') == 'clear_remy_conversation':
            # 대화 내역 삭제
            request.session['remy_conversation'] = []
            request.session.modified = True
            return redirect('remy')

        user_input = request.POST.get('user_input', '')
        run2 = ThreadAPI.submit_message(Remy_ASSISTANT_ID, thread1, user_input)
        run2 = ThreadAPI.wait_on_run(run2, thread1)
        ans = ThreadAPI.answer_print(ThreadAPI.get_response(thread1))

        remy_conversation.append({'question': user_input, 'answer': ans})
        request.session['remy_conversation'] = remy_conversation

    # 기본 페이지 표시
    return render(request, 'remy.html', {'remy_conversation': remy_conversation})

def mylo(request):
    thread = client.beta.threads.create()
    file1 = open("C:\\Users\\dbalf\\Downloads\\KDT_Project\\NLP\\Django\\game\\mylo.txt","w+")
    thread = str(thread.id)
    file1.write(thread)

    file1 = open("C:\\Users\\dbalf\\Downloads\\KDT_Project\\NLP\\Django\\game\\mylo.txt","r+")
    thread = file1.read()
    file1.close()
    thread1, run1 = ThreadAPI.mylo_create_thread_and_run("", thread)
    run1 = ThreadAPI.wait_on_run(run1, thread1)
    # 세션에서 대화 내역을 가져옴
    mylo_conversation = request.session.get('mylo_conversation', [])

    if request.method == 'POST':
        if request.POST.get('action') == 'create_image':
            # 이미지 생성 요청 처리
            if mylo_conversation:
                last_mylo_conversation = mylo_conversation[-1]
                last_answer = last_mylo_conversation.get('answer')
                
                # GPT의 응답에 추가 지시문을 더함
                modified_input = last_answer + " 이 시나리오에 맞는 흑백의 러프하고 해상도 낮춰서 콘티 이미지를 생성해줘"
                
                # 이미지 생성 API 호출 (여기는 예시로 작성, 실제 API 호출 방식에 맞게 수정 필요)
                image_url = fopenaiAPI1.create_image(modified_input)

                # 생성된 이미지 URL을 대화 내역에 추가
                last_mylo_conversation['image_url'] = image_url
                request.session.modified = True

                return render(request, 'mylo.html', {'mylo_conversation': mylo_conversation})
            else:
                # 대화 내역이 없는 경우 처리
                return render(request, 'mylo.html', {'mylo_conversation': mylo_conversation, 'error': 'No conversation history found.'})

        elif request.POST.get('action') == 'clear_mylo_conversation':
            # 대화 내역 삭제
            request.session['mylo_conversation'] = []
            request.session.modified = True
            return redirect('mylo')

        user_input = request.POST.get('user_input', '')
        run2 = ThreadAPI.submit_message(Mylo_ASSISTANT_ID, thread1, user_input)
        run2 = ThreadAPI.wait_on_run(run2, thread1)
        ans = ThreadAPI.answer_print(ThreadAPI.get_response(thread1))

        mylo_conversation.append({'question': user_input, 'answer': ans})
        request.session['mylo_conversation'] = mylo_conversation

    # 기본 페이지 표시
    return render(request, 'mylo.html', {'mylo_conversation': mylo_conversation})

def eugene(request):
    thread = client.beta.threads.create()
    file1 = open("C:\\Users\\dbalf\\Downloads\\KDT_Project\\NLP\\Django\\game\\eugene.txt","w+")
    thread = str(thread.id)
    file1.write(thread)

    file1 = open("C:\\Users\\dbalf\\Downloads\\KDT_Project\\NLP\\Django\\game\\eugene.txt","r+")
    thread = file1.read()
    file1.close()
    thread1, run1 = ThreadAPI.eugene_create_thread_and_run("", thread)
    run1 = ThreadAPI.wait_on_run(run1, thread1)
    # 세션에서 대화 내역을 가져옴
    eugene_conversation = request.session.get('eugene_conversation', [])

    if request.method == 'POST':
        if request.POST.get('action') == 'create_image':
            # 이미지 생성 요청 처리
            if eugene_conversation:
                last_eugene_conversation = eugene_conversation[-1]
                last_answer = last_eugene_conversation.get('answer')
                
                # GPT의 응답에 추가 지시문을 더함
                modified_input = last_answer + " 이 시나리오에 맞는 흑백의 러프하고 해상도 낮춰서 콘티 이미지를 생성해줘"
                
                # 이미지 생성 API 호출 (여기는 예시로 작성, 실제 API 호출 방식에 맞게 수정 필요)
                image_url = fopenaiAPI1.create_image(modified_input)

                # 생성된 이미지 URL을 대화 내역에 추가
                last_eugene_conversation['image_url'] = image_url
                request.session.modified = True

                return render(request, 'eugene.html', {'eugene_conversation': eugene_conversation})
            else:
                # 대화 내역이 없는 경우 처리
                return render(request, 'eugene.html', {'eugene_conversation': eugene_conversation, 'error': 'No conversation history found.'})

        elif request.POST.get('action') == 'clear_eugene_conversation':
            # 대화 내역 삭제
            request.session['eugene_conversation'] = []
            request.session.modified = True
            return redirect('eugene')

        user_input = request.POST.get('user_input', '')
        run2 = ThreadAPI.submit_message(Eugene_ASSISTANT_ID, thread1, user_input)
        run2 = ThreadAPI.wait_on_run(run2, thread1)
        ans = ThreadAPI.answer_print(ThreadAPI.get_response(thread1))

        eugene_conversation.append({'question': user_input, 'answer': ans})
        request.session['eugene_conversation'] = eugene_conversation

    # 기본 페이지 표시
    return render(request, 'eugene.html', {'eugene_conversation': eugene_conversation})

def camila(request):
    thread = client.beta.threads.create()
    file1 = open("C:\\Users\\dbalf\\Downloads\\KDT_Project\\NLP\\Django\\game\\camila.txt","w+")
    thread = str(thread.id)
    file1.write(thread)

    file1 = open("C:\\Users\\dbalf\\Downloads\\KDT_Project\\NLP\\Django\\game\\camila.txt","r+")
    thread = file1.read()
    file1.close()
    thread1, run1 = ThreadAPI.camila_create_thread_and_run("", thread)
    run1 = ThreadAPI.wait_on_run(run1, thread1)
    # 세션에서 대화 내역을 가져옴
    camila_conversation = request.session.get('camila_conversation', [])

    if request.method == 'POST':
        if request.POST.get('action') == 'create_image':
            # 이미지 생성 요청 처리
            if camila_conversation:
                last_camila_conversation = camila_conversation[-1]
                last_answer = last_camila_conversation.get('answer')
                
                # GPT의 응답에 추가 지시문을 더함
                modified_input = last_answer + " 이 시나리오에 맞는 흑백의 러프하고 해상도 낮춰서 콘티 이미지를 생성해줘"
                
                # 이미지 생성 API 호출 (여기는 예시로 작성, 실제 API 호출 방식에 맞게 수정 필요)
                image_url = fopenaiAPI1.create_image(modified_input)

                # 생성된 이미지 URL을 대화 내역에 추가
                last_camila_conversation['image_url'] = image_url
                request.session.modified = True

                return render(request, 'camila.html', {'camila_conversation': camila_conversation})
            else:
                # 대화 내역이 없는 경우 처리
                return render(request, 'camila.html', {'camila_conversation': camila_conversation, 'error': 'No conversation history found.'})

        elif request.POST.get('action') == 'clear_camila_conversation':
            # 대화 내역 삭제
            request.session['camila_conversation'] = []
            request.session.modified = True
            return redirect('camila')

        user_input = request.POST.get('user_input', '')
        run2 = ThreadAPI.submit_message(Camila_ASSISTANT_ID, thread1, user_input)
        run2 = ThreadAPI.wait_on_run(run2, thread1)
        ans = ThreadAPI.answer_print(ThreadAPI.get_response(thread1))

        camila_conversation.append({'question': user_input, 'answer': ans})
        request.session['camila_conversation'] = camila_conversation

    # 기본 페이지 표시
    return render(request, 'camila.html', {'camila_conversation': camila_conversation})

def dave(request):
    thread = client.beta.threads.create()
    file1 = open("C:\\Users\\dbalf\\Downloads\\KDT_Project\\NLP\\Django\\game\\dave.txt","w+")
    thread = str(thread.id)
    file1.write(thread)

    file1 = open("C:\\Users\\dbalf\\Downloads\\KDT_Project\\NLP\\Django\\game\\dave.txt","r+")
    thread = file1.read()
    file1.close()
    thread1, run1 = ThreadAPI.dave_create_thread_and_run("", thread)
    run1 = ThreadAPI.wait_on_run(run1, thread1)
    # 세션에서 대화 내역을 가져옴
    dave_conversation = request.session.get('dave_conversation', [])

    if request.method == 'POST':
        if request.POST.get('action') == 'create_image':
            # 이미지 생성 요청 처리
            if dave_conversation:
                last_dave_conversation = dave_conversation[-1]
                last_answer = last_dave_conversation.get('answer')
                
                # GPT의 응답에 추가 지시문을 더함
                modified_input = last_answer + " 이 시나리오에 맞는 흑백의 러프하고 해상도 낮춰서 콘티 이미지를 생성해줘"
                
                # 이미지 생성 API 호출 (여기는 예시로 작성, 실제 API 호출 방식에 맞게 수정 필요)
                image_url = fopenaiAPI1.create_image(modified_input)

                # 생성된 이미지 URL을 대화 내역에 추가
                last_dave_conversation['image_url'] = image_url
                request.session.modified = True

                return render(request, 'dave.html', {'dave_conversation': dave_conversation})
            else:
                # 대화 내역이 없는 경우 처리
                return render(request, 'dave.html', {'dave_conversation': dave_conversation, 'error': 'No conversation history found.'})

        elif request.POST.get('action') == 'clear_dave_conversation':
            # 대화 내역 삭제
            request.session['dave_conversation'] = []
            request.session.modified = True
            return redirect('dave')

        user_input = request.POST.get('user_input', '')
        run2 = ThreadAPI.submit_message(Dave_ASSISTANT_ID, thread1, user_input)
        run2 = ThreadAPI.wait_on_run(run2, thread1)
        ans = ThreadAPI.answer_print(ThreadAPI.get_response(thread1))

        dave_conversation.append({'question': user_input, 'answer': ans})
        request.session['dave_conversation'] = dave_conversation

    # 기본 페이지 표시
    return render(request, 'dave.html', {'dave_conversation': dave_conversation})

def creator(request):
    
    return render(request, 'creator.html')

# def threadtest(request):

#     file1 = open("C:\\Users\\dbalf\\Downloads\\KDT_Project\\NLP\\Django\\game\\thread2.txt","r+")
#     thread = file1.read()
#     file1.close()

#     thread1, run1 = ThreadAPI.create_thread_and_run(" ", thread)
#     run1 = ThreadAPI.wait_on_run(run1, thread1)

#     if request.method == 'POST':
#         user_input = request.POST.get('user_input', '') 
#         run2 = ThreadAPI.submit_message(TOUR_ASSISTANT_ID, thread1, user_input)
#         run2 = ThreadAPI.wait_on_run(run2, thread1)
#         ans = ThreadAPI.answer_print(ThreadAPI.get_response(thread1))
        
#         print("GPT 응답:", ans)
#         # modified_input = ans + " 이 시나리오에 맞는 흑백의 러프한 콘티 이미지를 장면 수 대로 생성해줘"
#         # image_url = fopenaiAPI1.create_image(modified_input)

#         # 이미지 URL과 GPT-4의 응답을 템플릿에 전달
#         return render(request, 'GPTinput2.html', {'Data': ans})
         
#     # GET 요청일 때는 그냥 페이지를 렌더링
#     return render(request, 'GPTinput2.html')




# def threadtest(request):
#     file1 = open("C:\\Users\\dbalf\\Downloads\\KDT_Project\\NLP\\Django\\game\\thread.txt", "r+")
#     thread = file1.read()
#     file1.close()

#     thread1, run1 = ThreadAPI.create_thread_and_run("", thread)
#     run1 = ThreadAPI.wait_on_run(run1, thread1)

#     if request.method == 'POST':
#         final_input = request.POST.get('final_input', '') # 수정된 부분

#         run2 = ThreadAPI.submit_message(TOUR_ASSISTANT_ID, thread1, final_input)
#         run2 = ThreadAPI.wait_on_run(run2, thread1)
#         ans = ThreadAPI.answer_print(ThreadAPI.get_response(thread1))
        
#         modified_input = ans + " 이 시나리오에 맞는 흑백의 러프하고 해생도 낮춰서 콘티 이미지를 생성해줘"
#         image_url = fopenaiAPI1.create_image(modified_input)

#         return render(request, 'GPTinput2.html', {'Data': ans, 'ImageUrl': image_url})

#     return render(request, 'GPTinput2.html')
