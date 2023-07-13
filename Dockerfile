FROM python:slim
RUN pip install openai pywebio
ADD positive-bot.py .
CMD python positive-bot.py
