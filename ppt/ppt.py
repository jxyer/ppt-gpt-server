from gpt import GPT
import json

from ppt.pptdata import PPTData
from util.xml import parser_ppt_summary


class PPT:
    def __init__(self, topic):
        # 构建ppt副标题
        # subtitle = self.generate_subtitle(topic)
        # 构建ppt摘要
        # ppt_each_summary = self.generate_ppt_summary(topic, subtitle)
        # 获取每个摘要的内容
        ppt_each_summary = """
                <ppt title="介绍主题">
            本次演讲将探讨为什么越来越多的年轻人不愿意结婚，其中一个重要原因是婚姻观念的改变。
        </ppt>
        <ppt title="婚姻观念的变化">
            近年来，随着社会的发展和人们思想观念的改变，越来越多的年轻人开始抵触传统的婚姻观念，他们更加追求个性化和自由化的生活方式。
        </ppt>
        <ppt title="经济压力">
            除了婚姻观念的改变，经济压力也是年轻人不愿意结婚的原因之一。现如今，房价高涨、生活成本增高等因素使得年轻人负担沉重，难以承担起家庭的责任。
        </ppt>
        <ppt title="延迟成年">
            相比以往，现在的年轻人更加晚熟，追求自己的事业和兴趣，而不是早早地步入婚姻殿堂。这也是导致年轻人不愿意结婚的原因之一。
        </ppt>
        <ppt title="婚姻观念的改变与家庭教育">
            从根本上来说，婚姻观念的改变与家庭教育有着密不可分的关系。现在的年轻人受到的家庭教育不同于过去，更加注重独立、自由和个性，这也是导致婚姻观念改变的原因之一。
        </ppt>
                """
        ppt_summary = parser_ppt_summary(ppt_each_summary)

        # 对主题进行布局、内容分析
        # current_ppt = ppt_summary[0]
        # topic_ppt = self.generate_ppt_topic(current_ppt)
        # print("主题", topic_ppt)
        # topic_ppt = json.loads(topic_ppt.strip('\t\r\n'))
        # data = PPTData()
        # data.add_topic(topic_ppt)

        # 对章节分析
        # had_menu = self.whether_generate_menu(ppt_each_summary)
        had_menu = '否'
        if had_menu == '是':
            pass
        elif had_menu == '否':
            summary = ppt_summary[1]
            print(summary)
            # 构建ppt页面元素
            elements = self.generate_ppt_element(summary)
            # 根据页面元素来对ppt进行布局
            # layout_data=self.generate_ppt_layout(summary,elements)
            print(elements)
            pass
        # self.data = data

    def generate_subtitle(self, title):
        prompt = f""" 
        帮我根据【】里的标题生成一个子标题,
        要求字数在6-16个字以内，
        如果是你不确定的内容你可以说无。
        【{title}】"""
        return GPT().result(prompt).content

    def generate_chapter_title(self, title, subtitle):
        prompt = f"""
            帮我生成根据主题：{title}和子主题：{subtitle}来生成ppt的章节,
            可以生成3到6个章节，
            要求字数在6-16个字以内，
            如果是你不确定的内容你可以不说，
            输出内容按照如下格式输出。
            章节一,
            章节二,
            章节三,
            章节四,
            章节五
        """
        return GPT().result(prompt).content

    # 构建ppt摘要
    def generate_ppt_summary(self, title, subtitle):
        prompt = f"""
            帮我生成根据主题：{title}和子主题：{subtitle}来设计ppt，
            可以生成5到10页的ppt，
            说明每页ppt在做什么，
            如果是你不确定的内容你可以不说，
            请按照格式输出，
            不要胡乱增减其他格式，只输出文本,
            每个示例必须以标签“<ppt ”开始，以标签“</ppt>”结束
            输出内容按照如下格式输出。
            <ppt title="设置主题和样式">内容1</ppt>，
            <ppt title="章节页">内容2</ppt>，
            <ppt title="某章节介绍">内容3</ppt>
        """
        return GPT().result(prompt).content

    """
    构建ppt内容
    
    ppt:    title = ppt[0]
            content = ppt[1]
    """

    # 构建首页
    def generate_ppt_topic(self, ppt):
        prompt = """
            请根据标题：%s和这页ppt的描述：%s，生成一页ppt内容，
            ppt的宽度为1000像素、高度为562.5像素，
            这页ppt作为首页展示，
            需要主题（一个）、子主题（一个）、图片（可选）、背景（可选），
            主题的字体大小(font-size)、颜色(color)、旋转(rotate)请选择你认为最符合主题的。
            子主题的字体大小(font-size)、颜色(color)、旋转(rotate)请选择你认为最符合主题的。
            主题和子主题内的content是html格式，请输出你认为最符合主题的样式。
            图片可以描述0到3张，请选择你认为最符合主题的描述。
            背景可以描述0到1张，请选择你认为最符合主题的描述。
            确保主题、子主题、图片高宽不要超过ppt高宽的范围。
            请把主题、子主题、图片放到你认为最合适的位置。
            背景用type="background",图片用type="image"。
            所有元素都以左上为起始点。
            请逐步分析包括位置、字体大小、颜色、旋转。
            必须按照json格式输出。
            如果是你不确定的内容你可以不说。
            请参考下面例子，按照格式输出。
            {
                "title":{ "left":"100","top":"50", "width":"585", "height"="188", "color"="#000", "content"="<p><strong><span style='font-size:  112px'>主题</span></strong></p>", "rotate"="0" },
                "subtitle":{ "left":"100", "top":"50", "width":"585", "height"="56", "color"="#ccc", "content"="<p><strong><span style='font-size:  30px'>子主题</span></strong></p>", "rotate"="0" },
                "image":[ { type="image" "left":"100", "top":"50", "width":"30", "height"="30", "content"="图片描述(不用html格式，根据主题来描述图片)", "rotate"="0"},
                          { type="background" "left":"100", "top":"50", "width":"30", "height"="30", "content"="背景图片描述(不用html格式，根据主题来描述图片)", "rotate"="0"} ],
            }
        """ % (ppt[0], ppt[1])
        return GPT().result(prompt).content

    # 是否构建文章目录
    def whether_generate_menu(self, summary):
        prompt = """
            根据下面【】里的内容来确定是否需要一页ppt来展示菜单。
            请逐步分析。
            请按照我的要求输出。
            只输出：是 或者 否
            【%s】
        """ % summary
        return GPT().result(prompt).content

    '''
    生成的结果
    {
    "text": [
        {
            "content": "婚姻观念的变化和趋势"
        },
        {
            "content": "近年来，随着社会的发展和人们思想观念的改变，越来越多的年轻人开始抵触传统的婚姻观念，他们更加追求个性化和自由化的生活方式。"
        },
        {
            "content": "影响婚姻观念变化的因素"
        },
        {
            "content": "1.社会经济变革"
        },
        {
            "content": "2.文化传统和媒体影响"
        },
        {
            "content": "3.家庭教育和人际关系"
        },
        {
            "content": "4.婚姻法律和政策"
        },
        {
            "content": "年轻人对婚姻的新认知和态度"
        },
        {
            "content": "1.婚姻不再是必须品"
        },
        {
            "content": "2.婚姻不是人生的唯一选择"
        },
        {
            "content": "3.婚姻需要建立在平等和尊重的基础上"
        },
        {
            "content": "4.婚姻需要与个人发展相匹配"
        }
    ],
    "image": [
        {
            "content": "一张年轻人在户外拍摄的自由自在的照片"
        }
    ],
    "shape": [
        {
            "content": "矩形框"
        }
    ],
    "chart": [],
    "table": []
}
    '''

    def generate_ppt_element(self, summary):
        prompt = """
            根据标题：%s和这页ppt的描述：%s里的内容来确定这个页面需要哪些元素。
            内容包括文本(text)、图片(image)、形状(shape)、图表(chart)、表格(table)。
            并分析每个元素所需要的数量。
            请逐步分析。
            如果不需要上面某个元素可以不用分析。
            如果需要形状请输出形状的名称。
            确保符合主题的内容。
            只输出json格式，不要其他内容。
            必须按照下面内容格式输出，不要输出json格式以外的文本内容。
            {
                "text":[ { "content":"内容" } ],
                "image":[ { "content"="图片描述" } ],
                "shape":[ { "content"="形状描述" } ],
                "chart":[ { "content"="图表描述" } ],
                "table":[ { "content"="表格描述" } ],
            }
        """ % (summary[0], summary[1])
        return GPT().result(prompt).content

    # 构建ppt布局
    def generate_ppt_layout(self, summary, elements):
        prompt = """
            PPT的宽度为1000像素、高度为562.5像素;
            标题：%s；
            本页PPT的描述：%s；
            PPT元素(JSON格式)：%s;
            JSON格式解释：文本(text)、图片(image)、形状(shape)、图表(chart)、表格(table);
            text下的每个content对应元素内容;
            根据以上信息，帮我对PPT元素里的内容进行布局。
            必须按照json格式输出。
            如果是你不确定的内容你可以不说。
            请参考下面例子，按照格式输出。
            {
                "text":[{ "left":"100","top":"50", "width":"585", "height"="188", "color"="#000", "content"="<p><strong><span style='font-size:  112px'>text下的content</span></strong></p>", "rotate"="0" }],
                "image":[ { "left":"100", "top":"50", "width":"30", "height"="30", "content"="image下的content", "rotate"="0"}],
            }
        """
        return GPT().result(prompt).content


"""
主题生成json
{
    "title": {
        "left": "100",
        "top": "50",
        "width": "800",
        "height": "150",
        "color": "#000",
        "content": "<p><strong><span style='font-size: 100px'>阿里云计算</span></strong></p><p><strong><span style='font-size: 80px'>产品介绍</span></strong></p>",
        "rotate": "0"
    },
    "subtitle": {
        "left": "100",
        "top": "250",
        "width": "800",
        "height": "50",
        "color": "#666",
        "content": "<p><span style='font-size: 40px'>阿里云计算产品介绍目录</span></p>",
        "rotate": "0"
    },
    "image": [
        {
            "type": "image",
            "left": "100",
            "top": "350",
            "width": "300",
            "height": "200",
            "content": "阿里云服务器ECS的图片描述",
            "rotate": "0"
        },
        {
            "type": "image",
            "left": "450",
            "top": "350",
            "width": "300",
            "height": "200",
            "content": "阿里云数据库RDS的图片描述",
            "rotate": "0"
        },
        {
            "type": "image",
            "left": "800",
            "top": "350",
            "width": "300",
            "height": "200",
            "content": "阿里云对象存储OSS的图片描述",
            "rotate": "0"
        },
        {
            "type": "background",
            "left": "0",
            "top": "0",
            "width": "1000",
            "height": "562.5",
            "content": "背景图片描述",
            "rotate": "0"
        }
    ]
}
"""
