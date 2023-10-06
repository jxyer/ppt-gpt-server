"""
    ppt元素格式
"""
from typing import Optional

"""
/**
 * 图片滤镜
 * 
 * https://developer.mozilla.org/zh-CN/docs/Web/CSS/filter
 * 
 * 'blur'?: 模糊，默认0（px）
 * 
 * 'brightness'?: 亮度，默认100（%）
 * 
 * 'contrast'?: 对比度，默认100（%）
 * 
 * 'grayscale'?: 灰度，默认0（%）
 * 
 * 'saturate'?: 饱和度，默认100（%）
 * 
 * 'hue-rotate'?: 色相旋转，默认0（deg）
 * 
 * 'opacity'?: 不透明度，默认100（%）
 */
"""


class ImageElementFilters:
    def __init__(self, blur: Optional[str] = None, brightness: Optional[str] = None, contrast: Optional[str] = None,
                 grayscale: Optional[str] = None, saturate: Optional[str] = None, hue_rotate: Optional[str] = None,
                 opacity: Optional[str] = None):
        self.blur = blur
        self.brightness = brightness
        self.contrast = contrast
        self.grayscale = grayscale
        self.saturate = saturate
        self.hue_rotate = hue_rotate
        self.opacity = opacity


"""
/**
 * 元素边框
 * 
 * style?: 边框样式（实线或虚线）
 * 
 * width?: 边框宽度
 * 
 * color?: 边框颜色
 */
"""


class PPTElementOutline:
    def __init__(self, style: str = None, width: int = None, color: str = None):
        self.style = style
        self.width = width
        self.color = color

        # 添加默认值以确保类实例可以成功创建
        if self.style is None:
            self.style = 'solid'
        if self.width is None:
            self.width = 1
        if self.color is None:
            self.color = 'black'


"""
/**
 * 图片裁剪
 * 
 * range: 裁剪范围，例如：[[10, 10], [90, 90]] 表示裁取原图从左上角 10%, 10% 到 90%, 90% 的范围
 * 
 * shape: 裁剪形状，见 configs/imageClip.ts CLIPPATHS 
 */
"""


class ImageElementClip:
    def __init__(self,
                 range: [[Optional[int], Optional[int]], [Optional[int], Optional[int]]] = None,
                 shape: Optional[str] = None):
        self.range = range
        self.shape = shape


"""
/**
 * 元素阴影
 * 
 * h: 水平偏移量
 * 
 * v: 垂直偏移量
 * 
 * blur: 模糊程度
 * 
 * color: 阴影颜色
 */
"""


class PPTElementShadow:
    def __init__(self, h: int, v: int, blur: int, color: str):
        self.h = h
        self.v = v
        self.blur = blur
        self.color = color


"""
/**
 * 图片蒙版
 * 
 * color: 蒙版颜色
 * 
 * opacity: 蒙版透明度
 */
"""


class ImageColorElementMask:
    def __init__(self, color: str, opacity: int):
        self.color = color
        self.opacity = opacity


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
    def __init__(self, id, left, top, width, height, rotate, fixedRatio=False, src='',
                 outline: PPTElementOutline = None,
                 filters: ImageElementFilters = None,
                 clip: ImageElementClip = None,
                 flipH: bool = False,
                 flipV: bool = False,
                 shadow: PPTElementShadow = None,
                 colorMask: ImageColorElementMask = None):
        super().__init__(id, left, top, width, height, rotate)
        self.type = 'image'
        self.fixedRatio = fixedRatio
        self.src = src
        self.outline = outline
        self.filters = filters
        self.clip = clip
        self.flipH = flipH
        self.flipV = flipV
        self.shadow = shadow
        self.colorMask = colorMask


"""
/**
 * 形状渐变
 * 
 * type: 渐变类型（径向、线性）
 * 
 * color: 渐变颜色
 * 
 * rotate: 渐变角度（线性渐变）
 */
"""


class ShapeGradient:
    def __init__(self, type: str, color: tuple, rotate: int):
        self.type = type
        self.color = color
        self.rotate = rotate

        # 添加默认值以确保类实例可以成功创建
        if self.type is None:
            self.type = 'linear'
        if self.color is None:
            self.color = ('white', 'black')
        if self.rotate is None:
            self.rotate = 0


"""
/**
 * 元素阴影
 * 
 * h: 水平偏移量
 * 
 * v: 垂直偏移量
 * 
 * blur: 模糊程度
 * 
 * color: 阴影颜色
 */
"""


class PPTElementShadow:
    def __init__(self, h: int = 0, v: int = 0, blur: int = 0, color: str = 'transparent') -> None:
        self.h = h
        self.v = v
        self.blur = blur
        self.color = color


"""
/**
 * 形状内文本
 * 
 * content: 文本内容（HTML字符串）
 * 
 * defaultFontName: 默认字体（会被文本内容中的HTML内联样式覆盖）
 * 
 * defaultColor: 默认颜色（会被文本内容中的HTML内联样式覆盖）
 * 
 * align: 文本对齐方向（垂直方向）
 */
"""


class ShapeText:
    def __init__(self, content: str = '', defaultFontName: str = 'Arial', defaultColor: str = 'black',
                 align: str = 'top') -> None:
        self.content = content
        self.defaultFontName = defaultFontName
        self.defaultColor = defaultColor
        self.align = align


class PPTShapeElement(PPTBaseElement):
    def __init__(self, id, left, top, width, height, rotate, viewBox: [int, int], path: str, fixedRatio: bool = False,
                 fill: str = None, gradient: ShapeGradient = None,
                 outline: PPTElementOutline = None, opacity: float = None, flipH: bool = None, flipV: bool = None,
                 shadow: PPTElementShadow = None, special: bool = None, text: ShapeText = None,
                 pathFormula: str = None, keypoint: int = None):
        super().__init__(id, left, top, width, height, rotate)
        self.type = 'shape'
        self.viewBox = viewBox
        self.path = path
        self.fixedRatio = fixedRatio
        self.fill = fill
        self.gradient = gradient
        self.outline = outline
        self.opacity = opacity
        self.flipH = flipH
        self.flipV = flipV
        self.shadow = shadow
        self.special = special
        self.text = text
        self.pathFormula = pathFormula
        self.keypoint = keypoint


class ChartData:
    def __init__(self, labels: list[str], legends: list[str], series: list[list[float]]):
        self.labels = labels
        self.legends = legends
        self.series = series


"""
/**
 * 图表元素
 * 
 * type: 元素类型（chart）
 * 
 * fill?: 填充色
 * 
 * chartType: 图表基础类型（bar/line/pie），所有图表类型都是由这三种基本类型衍生而来
 * 
 * data: 图表数据
 * 
 * options?: 图表配置项
 * 
 * outline?: 边框
 * 
 * themeColor: 主题色
 * 
 * gridColor?: 网格&坐标颜色
 * 
 * legend?: 图例/位置
 */
"""


class PPTChartElement(PPTBaseElement):
    def __init__(self, id, left, top, width, height, rotate, chartType: str, data: ChartData, themeColor: list[str],
                 fill: str = None, options: dict = None, outline: dict = None, gridColor: str = None, legend: str = ''):
        super().__init__(id, left, top, width, height, rotate)
        self.type = 'chart'
        self.fill = fill
        self.chartType = chartType
        self.data = data
        self.options = options
        self.outline = outline
        self.themeColor = themeColor
        self.gridColor = gridColor
        self.legend = legend


class TableCell:
    def __init__(self, id, colspan, rowspan, text, style=None):
        self.id = id
        self.colspan = colspan
        self.rowspan = rowspan
        self.text = text
        self.style = style


"""
/**
 * 表格元素
 * 
 * type: 元素类型（table）
 * 
 * outline: 边框
 * 
 * theme?: 主题
 * 
 * colWidths: 列宽数组，如[30, 50, 20]表示三列宽度分别为30%, 50%, 20%
 * 
 * cellMinHeight: 单元格最小高度
 * 
 * data: 表格数据
 */
"""


class PPTTableElement(PPTBaseElement):
    def __init__(self, id, left, top, width, height, rotate, outline: PPTElementOutline, colWidths: [int],
                 cellMinHeight: int,
                 data: list[list[TableCell]], theme=None):
        super().__init__(id, left, top, width, height, rotate)
        self.type = 'table'
        self.outline = outline
        self.theme = theme
        self.colWidths = colWidths
        self.cellMinHeight = cellMinHeight
        self.data = data
