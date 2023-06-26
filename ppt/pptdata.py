"""

    ppt元素格式
      {
        type: 'shape',
        id: '4cbRxp',
        left: 0,
        top: 200,
        width: 546,
        height: 362.5,
        viewBox: [200, 200],
        path: 'M 0 0 L 0 200 L 200 200 Z',
        fill: '#5b9bd5',
        fixedRatio: false,
        opacity: 0.7,
        rotate: 0
      },

"""
from gpt import GPT
from ppt.ppt_element import PPTTextElement, PPTImageElement


class PPTData:
    def __init__(self):
        # 存储ppt元素格式
        self.elements = []

    # 添加主题数据
    def add_topic(self, topic_ppt):
        if 'title' in topic_ppt:
            self.add_text_element(content=topic_ppt['title']['content'],
                                  color=topic_ppt['title']['color'],
                                  id='1',
                                  left=topic_ppt['title']['left'],
                                  top=topic_ppt['title']['top'],
                                  width=topic_ppt['title']['width'],
                                  height=topic_ppt['title']['height'],
                                  rotate=topic_ppt['title']['rotate'],
                                  )
        if 'subtitle' in topic_ppt:
            self.add_text_element(content=topic_ppt['subtitle']['content'],
                                  color=topic_ppt['subtitle']['color'],
                                  id='2',
                                  left=topic_ppt['subtitle']['left'],
                                  top=topic_ppt['subtitle']['top'],
                                  width=topic_ppt['subtitle']['width'],
                                  height=topic_ppt['subtitle']['height'],
                                  rotate=topic_ppt['subtitle']['rotate'],
                                  )
        if 'image' in topic_ppt:
            image_elements = topic_ppt['image']
            ids=3
            for element in image_elements:
                self.add_image_element(id=ids,
                                       content=element['content'],
                                       left=element['left'],
                                       top=element['top'],
                                       width=element['width'],
                                       height=element['height'],
                                       rotate=element['rotate'],
                                       imageType=element['type'],
                                       )
                ids+=1

    def add_text_element(self, content, color, id, left, top, width, height, rotate):
        element = PPTTextElement(content=content,
                                 defaultFontName='Microsoft Yahei',
                                 defaultColor=color,
                                 id=id,
                                 left=left,
                                 top=top,
                                 width=width,
                                 height=height,
                                 rotate=rotate)
        self.elements.append(element)

    def add_image_element(self, content, id, left, top, width, height, rotate, imageType):
        src = GPT().image(content)
        element = PPTImageElement(id=id,
                                  left=left,
                                  top=top,
                                  width=width,
                                  height=height,
                                  rotate=rotate,
                                  src=src,
                                  imageType=imageType)
        self.elements.append(element)
