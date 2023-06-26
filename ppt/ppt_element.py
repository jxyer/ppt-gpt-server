"""
    ppt元素格式
"""

"""
 元素通用属性
 
 id: 元素ID
 
 left: 元素水平方向位置（距离画布左侧）
 
 top: 元素垂直方向位置（距离画布顶部）
 
 lock?: 锁定元素
 
 groupId?: 组合ID（拥有相同组合ID的元素即为同一组合元素成员）
 
 width: 元素宽度
 
 height: 元素高度
 
 rotate: 旋转角度
 
 link?: 超链接
 
 name?: 元素名
 """


class PPTBaseElement:
    def __init__(self, id, left, top, width, height, rotate, lock=False, groupId=None, link=None, name=None):
        self.id = id
        self.left = float(left)
        self.top = float(top)
        self.width = float(width)
        self.height = float(height)
        self.rotate = float(rotate)
        self.lock = lock
        self.groupId = groupId
        self.link = link
        self.name = name


"""
 * 文本元素
 * 
 * type: 元素类型（text）
 * 
 * content: 文本内容（HTML字符串）
 * 
 * defaultFontName: 默认字体（会被文本内容中的HTML内联样式覆盖）
 * 
 * defaultColor: 默认颜色（会被文本内容中的HTML内联样式覆盖）
 * 
 * outline?: 边框
 * 
 * fill?: 填充色
 * 
 * lineHeight?: 行高（倍），默认1.5
 * 
 * wordSpace?: 字间距，默认0
 * 
 * opacity?: 不透明度，默认1
 * 
 * shadow?: 阴影
 * 
 * textIndent?: 段落首行缩进
 * 
 * paragraphSpace?: 段间距，默认 5px
 * 
 * vertical?: 竖向文本
"""


class PPTTextElement(PPTBaseElement):
    def __init__(self, content, defaultFontName, defaultColor, id, left, top, width, height, rotate, type='text',
                 outline=None, fill=None, lineHeight=None, wordSpace=None, opacity=None, shadow=None, textIndent=None,
                 paragraphSpace=None, vertical=None):
        super().__init__(id, left, top, width, height, rotate)
        self.type = type
        self.content = content
        self.defaultFontName = defaultFontName
        self.defaultColor = defaultColor
        self.outline = outline
        self.fill = fill
        self.lineHeight = lineHeight
        self.wordSpace = wordSpace
        self.opacity = opacity
        self.shadow = shadow
        self.textIndent = textIndent
        self.paragraphSpace = paragraphSpace
        self.vertical = vertical


"""
/**
 * 图片元素
 * 
 * type: 元素类型（image）
 * 
 * fixedRatio: 固定图片宽高比例
 * 
 * src: 图片地址
 * 
 * outline?: 边框
 * 
 * filters?: 图片滤镜
 * 
 * clip?: 裁剪信息
 * 
 * flipH?: 水平翻转
 * 
 * flipV?: 垂直翻转
 * 
 * shadow?: 阴影
 */
"""


class PPTImageElement(PPTBaseElement):
    def __init__(self, id, left, top, width, height, rotate, imageType, fixedRatio=False, src='', outline=None,
                 filters=None,
                 clip=None, flipH=False, flipV=False, shadow=None, colorMask=None):
        super().__init__(id, left, top, width, height, rotate)
        self.type = 'image'
        self.imageType = imageType
        self.fixedRatio = fixedRatio
        self.src = src
        self.outline = outline
        self.filters = filters
        self.clip = clip
        self.flipH = flipH
        self.flipV = flipV
        self.shadow = shadow
        self.colorMask = colorMask
