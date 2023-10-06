import re

from bs4 import BeautifulSoup


# 解析ppt摘要
def parser_ppt_summary(text):
    soup = BeautifulSoup(text, 'html.parser')
    ppts = soup.find_all('ppt')
    ppt_summary = []
    for ppt in ppts:
        title = ppt['title']
        content = ppt.get_text(strip=True)
        ppt_summary.append((title, content))
    return ppt_summary


# 截取```json 内容
def extract_json(text):
    if text.find("```") != -1:
        pattern = r"```(.*?)```"
        content = re.findall(pattern, text, re.DOTALL)
        if content:
            return content[0].strip()
    return text
