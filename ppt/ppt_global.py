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
import uuid
import json
from gpt import GPT
from ppt.ppt_element import *


class PPTFont:
    def __init__(self, font, title, subtitle, body):
        self.font = font
        self.title = title
        self.subtitle = subtitle
        self.body = body


class PPTColor:
    def __init__(self, primary, secondary, tertiary, neutral):
        self.primary = primary
        self.secondary = secondary
        self.tertiary = tertiary
        self.neutral = neutral


"""
json格式参考：
        {
            "fonts": {
                "font": "Microsoft YaHei",
                "title": "50px",
                "subtitle": "30px",
                "body": "24px"
            },
            "color": {
                "primary": "#FF6666",
                "secondary": "#333333",
                "tertiary": "#CCCCCC",
                "neutral": "#FFFFFF"
            }
        }
"""


class PPTStyle:
    def __init__(self, j: str):
        d = json.loads(j.strip('\t\r\n'))

        self.fonts = PPTFont(d['fonts']['font'],
                             d['fonts']['title'],
                             d['fonts']['subtitle'],
                             d['fonts']['body'])

        self.color = PPTColor(d['color']['primary'],
                              d['color']['secondary'],
                              d['color']['tertiary'],
                              d['color']['neutral'])
        self.background = d['background']


class PPTSlide:
    def __init__(self):
        # 存储ppt元素格式
        self.elements = []
        self.background= '#fff'

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
            ids = 3
            for element in image_elements:
                self.add_image_element(id=ids,
                                       content=element['content'],
                                       left=element['left'],
                                       top=element['top'],
                                       width=element['width'],
                                       height=element['height'],
                                       rotate=element['rotate'],
                                       )
                ids += 1

    # 添加布局元素
    def add_layout(self, layout_data):
        text_elements = layout_data['text']
        for e in text_elements:
            self.add_text_element(content=e['content'],
                                  color=e['color'],
                                  id=str(uuid.uuid1()),
                                  left=e['left'],
                                  top=e['top'],
                                  width=e['width'],
                                  height=e['height'],
                                  rotate=e['rotate'])

        image_elements = layout_data['image']
        for e in image_elements:
            self.add_image_element(id=str(uuid.uuid1()),
                                   content=e['content'],
                                   left=e['left'],
                                   top=e['top'],
                                   width=e['width'],
                                   height=e['height'],
                                   rotate=e['rotate'], )

        shape_elements = layout_data['shape']
        for e in shape_elements:
            self.add_shape_elements(id=str(uuid.uuid1()),
                                    left=e['left'],
                                    top=e['top'],
                                    width=e['width'],
                                    height=e['height'],
                                    rotate=e['rotate'],
                                    path=e['path'],
                                    viewBox=e['viewBox'])

        chart_elements = layout_data['chart']
        for e in chart_elements:
            self.add_chart_elements(id=str(uuid.uuid1()),
                                    left=e['left'],
                                    top=e['top'],
                                    width=e['width'],
                                    height=e['height'],
                                    rotate=e['rotate'],
                                    chartType=e['chartType'],
                                    data=ChartData(e['data']['labels'], e['data']['legends'], e['data']['series']),
                                    themeColor=e['themeColor'])

        table_elements = layout_data['table']
        for e in table_elements:
            self.add_table_elements(id=str(uuid.uuid1()),
                                    left=e['left'],
                                    top=e['top'],
                                    width=e['width'],
                                    height=e['height'],
                                    rotate=e['rotate'],
                                    cellMinHeight=e['cellMinHeight'],
                                    colWidths=e['colWidths'],
                                    data=e['data'],
                                    outline=PPTElementOutline(e['outline']['style'], e['outline']['width'],
                                                              e['outline']['color']))

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

    def add_image_element(self, content, id, left, top, width, height, rotate):
        src = GPT().image(content)
        element = PPTImageElement(id=id,
                                  left=left,
                                  top=top,
                                  width=width,
                                  height=height,
                                  rotate=rotate,
                                  src=src)
        self.elements.append(element)

    def add_shape_elements(self, id, left, top, width, height, rotate, viewBox, path):
        element = PPTShapeElement(id=id,
                                  left=left,
                                  top=top,
                                  width=width,
                                  height=height,
                                  rotate=rotate,
                                  viewBox=viewBox,
                                  path=path)
        self.elements.append(element)

    def add_chart_elements(self, id, left, top, width, height, rotate, chartType, data, themeColor):
        element = PPTChartElement(id=id,
                                  left=left,
                                  top=top,
                                  width=width,
                                  height=height,
                                  rotate=rotate,
                                  chartType=chartType,
                                  data=data,
                                  themeColor=themeColor)
        self.elements.append(element)

    def add_table_elements(self, id, left, top, width, height, rotate, cellMinHeight, colWidths, data, outline):
        element = PPTTableElement(id=id,
                                  left=left,
                                  top=top,
                                  width=width,
                                  height=height,
                                  rotate=rotate,
                                  cellMinHeight=cellMinHeight,
                                  colWidths=colWidths,
                                  data=data,
                                  outline=outline)
        self.elements.append(element)
