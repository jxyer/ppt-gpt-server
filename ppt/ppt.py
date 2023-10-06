from gpt import GPT
import json

from ppt.ppt_global import PPTSlide, PPTColor, PPTFont, PPTStyle
from util.str_util import parser_ppt_summary, extract_json


def generate_chapter_title(title, subtitle):
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
    return extract_json(GPT().chat_result(prompt).content)


def generate_subtitle(title):
    prompt = f""" 
    帮我根据【】里的标题生成一个子标题,
    要求字数在6-16个字以内，
    如果是你不确定的内容你可以说无。
    【{title}】"""
    return extract_json(GPT().chat_result(prompt).content)


class PPT:
    def __init__(self):
        pass
        # self.vo = PPTVo(ppt_slides, style.background)

    async def generate_ppt(self, topic, websocket, slide_finish):
        # 构建ppt副标题
        subtitle = generate_subtitle(topic)
        print("ppt 副标题", subtitle)
        # 构建ppt摘要
        ppt_each_summary = self.generate_ppt_summary(topic, subtitle)
        print("ppt 摘要", ppt_each_summary)
        # 构建ppt风格
        ppt_style = self.generate_ppt_style(ppt_each_summary)
        print("ppt 样式", ppt_style)
        style = PPTStyle(ppt_style)

        # 获取每个摘要的内容
        ppt_summary = parser_ppt_summary(ppt_each_summary)

        # 对主题进行布局、内容分析
        # current_ppt = ppt_summary[0]
        # topic_ppt = self.generate_ppt_topic(current_ppt)
        # print("主题", topic_ppt)
        # topic_ppt = json.loads(topic_ppt.strip('\t\r\n'))

        ppt_slides = []
        # data.add_topic(topic_ppt)

        # 对章节分析
        # had_menu = self.whether_generate_menu(ppt_each_summary)
        had_menu = '否'
        if had_menu == '是':
            pass
        elif had_menu == '否':
            for i in range(len(ppt_summary)):
                if i >= 2:
                    slide = PPTSlide()
                    summary = ppt_summary[i]
                    # 构建ppt页面元素
                    elements = self.generate_ppt_element(summary)
                    print("ppt 元素", elements)
                    # 构建ppt排版
                    typesetting = self.generate_ppt_typesetting(elements, ppt_style)
                    print("ppt 排版", typesetting)
                    # # 构建ppt布局
                    layout_elements = self.generate_ppt_layout(elements, typesetting)
                    print("ppt 布局", layout_elements)
                    slide.add_layout(json.loads(layout_elements.strip('\t\r\n')))
                    # # 添加幻灯片
                    slide.background = style.background
                    ppt_slides.append(slide)
                    print("完成")
                    await slide_finish(websocket, slide)

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
            <ppt title="主题和样式">内容1</ppt>，
            <ppt title="章节页">内容2</ppt>，
            <ppt title="某章节介绍">内容3</ppt>
        """
        return extract_json(GPT().chat_result(prompt).content)

    """
    构建ppt内容
    
    ppt:    title = ppt[0]
            content = ppt[1]
    """

    # 构建首页
    def generate_ppt_topic(self, ppt):
        prompt = """
            请根据标题：%s和这页ppt的描述：%s，生成一页幻灯片内容，
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
                "title":{ "left":"100","top":"50", "width":"585", "height":"188", "color":"#000", "content":"<p><strong><span style='font-size:  112px'>主题</span></strong></p>", "rotate":"0" },
                "subtitle":{ "left":"100", "top":"50", "width":"585", "height":"56", "color":"#ccc", "content":"<p><strong><span style='font-size:  30px'>子主题</span></strong></p>", "rotate":"0" },
                "image":[ { "type":"image", "left":"100", "top":"50", "width":"30", "height":"30", "content":"图片描述(不用html格式，根据主题来描述图片)", "rotate":"0"},
                          { "type":"background", "left":"100", "top":"50", "width":"30", "height":"30", "content":"背景图片描述(不用html格式，根据主题来描述图片)", "rotate":"0"} ],
            }
        """ % (ppt[0], ppt[1])
        return extract_json(GPT().chat_result(prompt).content)

    # 是否构建文章目录
    def whether_generate_menu(self, summary):
        prompt = """
            根据下面【】里的内容来确定是否需要一页幻灯片来展示菜单。
            请逐步分析。
            请按照我的要求输出。
            只输出：是 或者 否
            【%s】
        """ % summary
        return extract_json(GPT().chat_result(prompt).content)

    # 构建ppt布局
    def generate_ppt_layout(self, elements, typesetting):
        prompt = """
            PPT元素：%s;
            PPT排版信息：%s;
            根据以上信息，填充一下json内容，json内容涵盖了上面的元素信息;
            如果某些元素不需要，可以输出空数组如："chart":[]、"table":[],
            如果你不知道的，你可以不输出。
            请务必按照以下json格式填充，务必参考//后面的注释。
            请务必按照以下json格式填充，务必参考//后面的注释。
            请务必输出完整的json格式：{"text":[],"image":[],"shape":[],"chart":[],"table":[]}。
            参考下面json格式输出：
            {
                "text":[
                    {
                        left: 355, // 元素水平方向位置（距离画布左侧）
                        top: 253.25, // 元素垂直方向位置（距离画布顶部）
                        width: 585, // 元素宽度
                        height: 56, // 元素高度
                        rotate: 0, // 旋转角度
                        content: '<p><span style=\'font-size:  24px\'></span></p>', //文本内容（HTML字符串）
                        defaultFontName: 'Microsoft Yahei', // 默认字体（会被文本内容中的HTML内联样式覆盖）
                        color: '#333' // 默认颜色（会被文本内容中的HTML内联样式覆盖）
                    },
                ],
                "image":[
                    {
                        "left": "0",
                        "top": "0", 
                        "width": "10",
                        "height": "10",
                        "rotate": "0",
                        "content": "猫", 
                        "fixedRatio": true, 
                    }              
                ],
                "shape":[
                    {
                        "left": 0,
                        "top": 200,
                        "width": 546,
                        "height": 362.5,
                        "rotate": 0,
                        "viewBox": [200, 200], // SVG的viewBox属性，例如 [1000, 1000] 表示 '0 0 1000 1000'
                        "path": 'M 0 0 L 0 200 L 200 200 Z', // 形状路径，SVG path 的 d 属性
                        "fill": '#5b9bd5', // 填充，不存在渐变时生效
                        "fixedRatio": false,
                        "opacity": 0.7,
                    }
                ],
                "chart":[
                    {
                        "left": 0,
                        "top": 200,
                        "width": 546,
                        "height": 362.5,
                        "rotate": 0,
                        "chartType": "bar", // 图表基础类型(bar/line/pie)
                        "themeColor": ['#ccc','#000'],
                        "data":{
                            "labels" : ['必要开支','可选开支'], //如果有chart,务必填写数据
                            "legends" : ['开支分类'], //如果有chart,务必填写数据
                            "series" : [[11，11],[22,22]] //如果有chart,务必填写数据
                        }
                    },
                ],
                "table":[
                    {
                        "left": 0,
                        "top": 200,
                        "width": 546,
                        "height": 362.5,
                        "rotate": 0,
                        "outline": {
                            "style": "dashed" //边框样式（'dashed' | 'solid'）
                            "width": "1", // 边框宽度
                            "color": "#ccc" // 边框颜色
                        },
                        "colWidths": [30,50,20],
                        "cellMinHeight":20,
                        "data":[{ "id"="1", "colspan": 1, "rowspan": 1, "text":"addd"}]
                    }
                ]
            }
            只输出json格式，不要输出其他的内容。
            只输出json格式，不要输出其他的内容。
        """ % (elements, typesetting)
        return extract_json(GPT().chat_result(prompt).content)

    def generate_ppt_style(self, summaries):
        prompt = """
            根据整个ppt摘要信息：%s里的内容来设计这个ppt的主题风格。
            参考下面的标准：
            1、字号采用html的px单位；
            2、PPT的宽度为1000px、高度为562.5px；
            3、确保符合主题的内容；
            只输出json格式，不要输出其他的内容。
            必须按照下面内容例子格式输出，不要输出json格式以外的文本内容。
            '''
            {
                "fonts": { "font":"Arial","title":"0", "subtitle":"0", "body":"0" },
                "color": { "primary":"#000", "secondary":"#fff", "tertiary":"#ccc", "neutral":"#000" }
                "background": "#000"
            }
            '''
            我解释一下json格式属性：
            fonts：字体相关的集合。
            font：字体，选择一个符合主题的。
            title：对应主标题，以px为单位。
            subtitle：对应副标题，以px为单位。
            body：对应正文，以px为单位。
            color：主题颜色集合,集合元素输出格式为#000十六进制。
            primary: The primary key color is used to derive roles for key components across the UI.
            secondary: The secondary key color is used for less prominent components in the UI such as filter chips, while expanding the opportunity for color expression.
            tertiary: The tertiary key color is used to derive the roles of contrasting accents that can be used to balance primary and secondary colors or bring heightened attention to an element. The tertiary color role is left for teams to use at their discretion and is intended to support broader color expression in products.
            neutral: The neutral key color is used to derive surface color roles for backgrounds, as well as colors used for high emphasis text and icons.
            background: 幻灯片背景颜色，应该采用neutral。
        """ % summaries
        return extract_json(GPT().chat_result(prompt).content)

    # 构建排版
    def generate_ppt_typesetting(self, elements, ppt_style):
        prompt = """
            本页幻灯片所有的元素：[%s];
            PPT样式：[%s];
            根据以上提供信息来设计本页幻灯片的排版和样式。
            排版选择：
            1、水平排版：将内容从左到右横向排列，适合呈现流程、时间线或对比等信息。
            2、垂直排版：将内容从上到下纵向排列，适合呈现列表、步骤或分类等信息。
            3、网格排版：将幻灯片划分为网格，将不同的内容元素放置在不同的格子中，适合呈现多个空间相关的信息。
            4、绝对定位排版：通过精确定位和调整元素的位置和大小，实现自由度更高的排版效果，适用于需要精确控制每个元素位置的设计需求。
            5、层叠排版：通过将多个图层叠加在一起来呈现多层次的视觉效果，使幻灯片更具深度感和立体感。
            6、对称排版：将幻灯片的元素在垂直、水平或对角线方向上进行镜像或对称排列，呈现出均衡和统一感。
            不要输出排版示意图，用文字说明即可。
            不要输出排版示意图，用文字说明即可。
            不要输出排版示意图，用文字说明即可。
        """ % (elements, ppt_style)
        return extract_json(GPT().chat_result(prompt).content)

    # 构建ppt元素
    def generate_ppt_element(self, summary):
        prompt = """
            本页幻灯片的描述: %s;
            请根据本页幻灯片的描述，来填写扩充本页幻灯片的内容，只需要填写本页的内容。
        """ % (summary[1])
        gpt = GPT()
        a = gpt.chat_result(prompt).content
        print(a)
        prompt = """
            根据以上内容，请帮我添加一些元素来美化一下本页幻灯片。
            元素信息包括如下：
            1、背景
            2、图片
            3、形状：请描述形状的颜色，用途
            4、图表
            5、表格
            如果你认为没有必要以上某个元素，可以不添加。
        """
        b = gpt.chat_result(prompt).content
        print(b)

        prompt = """
            根据以上内容帮我生成一个json文件，用来表达当前页面的需要哪些元素，元素用来干什么的。
            元素包括：text、image、shape、chart、table。
        """
        return extract_json(gpt.chat_result(prompt).content)


# todo 备用
"""
            text元素：
            {
                "left": "0", // 元素水平方向位置（距离画布左侧）
                "top": "0", // 元素垂直方向位置（距离画布顶部）
                "width": "10", // 元素宽度
                "height": "10", // 元素高度
                "rotate": "0", // 旋转角度
                "content": "", // 文本内容（HTML字符串）
                "defaultFontName": "", // 默认字体（会被文本内容中的HTML内联样式覆盖）
                "defaultColor": "#000000", // 默认颜色（会被文本内容中的HTML内联样式覆盖）
                "outline": { // 边框
                "style": "solid", // 边框样式（实线或虚线）
                "width": 1, // 边框宽度
                "color": "#000000" // 边框颜色
                },
                "fill": "", // 填充色
                "lineHeight": 1.5, // 行高（倍），默认1.5
                "wordSpace": 0, // 字间距，默认0
                "opacity": 1, // 不透明度，默认1
                "shadow": { // 阴影
                "h": 0, // 水平偏移量
                "v": 0, // 垂直偏移量
                "blur": 0, // 模糊程度
                "color": "#000000" // 阴影颜色
                },
                "textIndent": 0, // 段落首行缩进
                "paragraphSpace": 5, // 段间距，默认 5px
                "vertical": false // 竖向文本
            }
            image元素：
            {
                "fixedRatio": true, // 固定图片宽高比例
                "src": "图片地址",
                "outline": { // 边框，可以为空 
                "style": "solid", // 边框样式（'dashed' | 'solid'）
                "width": 1, // 边框宽度
                "color": "#000000" // 边框颜色
                },
                "filters": { //图片滤镜，可以为空 
                "blur": "0px",
                "brightness": "100%%",
                "contrast": "100%%",
                "grayscale": "0%%",
                "saturate": "100%%",
                "hue-rotate": "0deg",
                "opacity": "100%%"
                },
                "clip": { //裁剪信息，可以为空 
                "range": [[10, 10],[90, 90]],// 裁剪范围,[[10, 10], [90, 90]] 表示裁取原图从左上角 10%%, 10%% 到 90%%, 90%% 的范围
                "shape": "rect"
                },
                "flipH": true, // 水平翻转，可以为空 
                "flipV": true, // 垂直翻转，可以为空 
                "shadow": { // 阴影，可以为空 
                "h": 0, // 水平偏移量
                "v": 0, // 垂直偏移量
                "blur": 0, // 模糊程度
                "color": "#000000" // 阴影颜色
                },
                "colorMask": { // 图片颜色遮罩，可以为空 
                "color": "蒙版颜色",
                "opacity": "蒙版透明度"
                }
            }
            shape元素：
            {
                "type": "shape", // 形状类型
                "viewBox": [1000, 1000], // 视图框大小
                "path": "形状路径", // 形状路径描述
                "fixedRatio": true, // 是否固定比例
                "fill": "填充颜色", // 填充颜色
                "gradient": {
                "type": "linear", // 渐变类型linear | radial
                "color": ["渐变颜色1", "渐变颜色2"] // 渐变颜色列表
                },
                "outline": {
                "style": "dashed" //边框样式（'dashed' | 'solid'）
                "width": "边框宽度", // 边框宽度
                "color": "边框颜色" // 边框颜色
                },
                "opacity": "不透明度", // 不透明度
                "flipH": true, // 是否水平翻转
                "flipV": true, // 是否垂直翻转
                "shadow": { // 阴影，可以为空 
                "h": 0, // 水平偏移量
                "v": 0, // 垂直偏移量
                "blur": 0, // 模糊程度
                "color": "#000000" // 阴影颜色
                },
                "special": true, // 是否特殊处理
                "text": {
                "content": "文本内容（HTML字符串）",
                "defaultFontName": "默认字体",
                "defaultColor": "默认颜色",
                "align": "文本对齐方向（垂直方向）"
                },
                "pathFormula": "ROUND_RECT", // 形状路径计算公式，可以不填
                "keypoint": "关键点位置百分比" // 关键点位置百分比，
            }

"""
