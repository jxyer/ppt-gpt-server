from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    SystemMessage,
    HumanMessage
)
import openai

import os

os.environ["OPENAI_API_KEY"] = "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"
openai.api_key = "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"

class GPT:
    def __init__(self):
        self.chat = ChatOpenAI()
        self.system_prompt = SystemMessage(content="""
            你是一个ppt设计师，可以设计出完美的ppt。
            按照一下要求设计：
                1. 设计幻灯片布局：选择适当的布局，以展示清晰的信息，并确保幻灯片的一致性。
                2. 使用适当的字体和字号：选择易于阅读的字体和适当的字号，以确保幻灯片上的文字易于阅读。
            请逐步分析，
            不要说多余的话。
        """)

    def result(self, prompt):
        human_prompt = HumanMessage(content=prompt)
        return self.chat([self.system_prompt, human_prompt])

    def image(self, content):
        response = openai.Image.create(prompt=content, n=1, size="256x256")
        return response['data'][0]['url']


"""
    1. 使用模板或自定义幻灯片主题：选择适合主题和受众的幻灯片主题，以增强幻灯片的视觉吸引力。
    2. 设计幻灯片布局：选择适当的布局，以展示清晰的信息，并确保幻灯片的一致性。
    3. 使用适当的字体和字号：选择易于阅读的字体和适当的字号，以确保幻灯片上的文字易于阅读。
    4. 使用图表和图像：使用适当的图表和图像来展示数据和信息，以帮助受众更好地理解幻灯片内容。
    5. 添加动画和转换效果：使用适当的动画和转换效果，以增强幻灯片的吸引力和视觉效果。
    6. 调整幻灯片顺序和结构：确保幻灯片的顺序和结构具有逻辑性，并能够有效地传达幻灯片的主要信息。
    7. 编辑和校对：检查幻灯片上的拼写、语法和标点符号等错误，并确保幻灯片上的文字和图像清晰、准确和易于理解。
"""