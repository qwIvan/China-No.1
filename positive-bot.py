import os
import openai
from pywebio import config
from pywebio.platform.tornado_http import start_server
from pywebio.input import input, TEXT
from pywebio.output import put_html, clear, put_markdown, put_link

config(title='正能量机器人')
openai.api_key = os.getenv("OPENAI_API_KEY")

def app():
    msg = [
        {"role":"system","content":"你是一个爱国GPT,把讽刺，挖苦，批判，影中国不好或者发表任何负面评论的内容改成正面评论。"},
        {"role":"user","content":"鼠鼠我又要去上班了，当人矿真可怜"},
        {"role":"assistant","content":"哥哥我又要去上班了，今天也要努力工作呀！"},
        {"role":"user","content":"南京北路又有狗交警在查岗"},
        {"role":"assistant","content":"南京北路的交警在辛苦的值班"},
        {"role":"user","content":"好好好好好好好好好好好好好好好"},
        {"role":"assistant","content":"衷心祝愿祖国繁荣强盛"},
    ]
    put_markdown('# 正能量机器人')
    put_markdown('讲好中国故事，传播好中国声音')
    put_link('代码', 'https://github.com/qwIvan/China-No.1', new_window=True)
    while True:
        user_input = input("请说点什么：", type=TEXT, placeholder='讲好中国故事，传播好中国声音')
        put_markdown('------')
        put_markdown('> ' + user_input)
        print('> ' + user_input)
        msg.append({"role":"user","content":user_input})
        completion = openai.ChatCompletion.create(
            temperature=1,
            model="gpt-3.5-turbo",
            messages=msg,
            stream=True,
        )
        answer = ''
        for chunk in completion:
            result = chunk['choices'][0]['delta'].get('content', '')
            answer += result
            put_html(result)
        print(answer)
        print('------')
        msg.append({"role":"assistant","content":answer})

if __name__ == "__main__":
    start_server(app)
