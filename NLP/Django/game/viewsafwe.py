from django.shortcuts import render
from django.http import HttpResponse
import fopenaiAPI1
import audioplay

# Create your views here.

def gamepage(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        
        # DALL-E를 사용하여 이미지 생성
        image_url = fopenaiAPI1.create_image(user_input)

        # GPT-4를 사용하여 텍스트 답변 생성
        ans = fopenaiAPI1.qna(user_input)

        # 템플릿에 전달할 컨텍스트 데이터
        context = {
            'Data': ans,
            'ImageUrl': image_url
        }
        return render(request, 'GPTinput.html', context)

    return render(request, 'GPTinput.html')

def datatest(request):
    context = {'Person1':'설렁탕', 'Person2': '비빔밥', 'Person3': '삼겹살'}
    return render(request, 'datatest.html', context)

def fortest(request):
    lst1 = ['banana', 'apple', 'orange']
    context = {'Person1':'설렁탕', 'Person2': '비빔밥', 'Person3': lst1}
    return render(request, 'fortest.html', context)

def mediatest(request):
    audioplay.play()
    lst1 = {'banana', 'apple', 'orange'}
    context = {'Person1':'설렁탕', 'Person2': '비빔밥', 'Person3': lst1}
    return render(request, 'fortest.html', context)

# Create your views here.
