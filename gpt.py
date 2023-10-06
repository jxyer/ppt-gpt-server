from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    SystemMessage,
    HumanMessage,
    AIMessage
)
from langchain.text_splitter import TextSplitter

import openai

import os

os.environ["OPENAI_API_KEY"] = "sk-x"
openai.api_key = "sk-x"


class GPT:
    def __init__(self):
        self.chat = ChatOpenAI(model_name="gpt-3.5-turbo-16k")
        self.history = []
        system_prompt = SystemMessage(content="""
            你是一个ppt设计师，可以设计出漂亮美观的ppt。
            PPT的宽度为1000像素、高度为562.5像素。
            对于每页幻灯片，确保幻灯片中不同页面的布局保持一定的一致性，使用相似的字体、颜色和图标等元素，使幻灯片整体看起来更加统一和专业。。
        """)
        self.history.append(system_prompt)

    def chat_result(self, prompt):
        human_prompt = HumanMessage(content=prompt)
        self.history.append(human_prompt)
        chat = self.chat(self.history)
        self.history.append(AIMessage(content=chat.content))
        return chat

    def image(self, content):
        response = openai.Image.create(prompt=content, n=1, size="256x256")
        return response['data'][0]['url']


# print(GPT().chat_result("你好").content)
"""
    1. 使用模板或自定义幻灯片主题：选择适合主题和受众的幻灯片主题，以增强幻灯片的视觉吸引力。
    2. 设计幻灯片布局：选择适当的布局，以展示清晰的信息，并确保幻灯片的一致性。
    3. 使用适当的字体和字号：选择易于阅读的字体和适当的字号，以确保幻灯片上的文字易于阅读。
    4. 使用图表和图像：使用适当的图表和图像来展示数据和信息，以帮助受众更好地理解幻灯片内容。
    5. 添加动画和转换效果：使用适当的动画和转换效果，以增强幻灯片的吸引力和视觉效果。
    6. 调整幻灯片顺序和结构：确保幻灯片的顺序和结构具有逻辑性，并能够有效地传达幻灯片的主要信息。
    7. 编辑和校对：检查幻灯片上的拼写、语法和标点符号等错误，并确保幻灯片上的文字和图像清晰、准确和易于理解。
"""
