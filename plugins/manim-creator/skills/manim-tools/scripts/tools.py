#!/usr/bin/env python3
"""
Manim Tools Library
可复用的 Manim 工具函数集合

使用方法:
    from tools.tools import *
    或
    from tools.tools import create_circle, plot_sine
"""

from manim import *
import numpy as np

# =============================================================================
# 几何图形工具 (Geometric Shapes)
# =============================================================================

def create_circle(radius: float = 1, color: str = BLUE, stroke_width: int = 4, **kwargs) -> Circle:
    """创建圆形

    Args:
        radius: 半径
        color: 颜色
        stroke_width: 边框宽度
        **kwargs: 其他 Circle 参数

    Returns:
        Circle 对象
    """
    return Circle(radius=radius, color=color, stroke_width=stroke_width, **kwargs)


def create_square(side_length: float = 2, color: str = RED, stroke_width: int = 4, **kwargs) -> Square:
    """创建正方形

    Args:
        side_length: 边长
        color: 颜色
        stroke_width: 边框宽度

    Returns:
        Square 对象
    """
    return Square(side_length=side_length, color=color, stroke_width=stroke_width, **kwargs)


def create_triangle(side_length: float = 2, color: str = GREEN, stroke_width: int = 4, **kwargs) -> Triangle:
    """创建等边三角形

    Args:
        side_length: 边长
        color: 颜色
        stroke_width: 边框宽度

    Returns:
        Triangle 对象
    """
    return Triangle(color=color, stroke_width=stroke_width, **kwargs)


def create_polygon(n_sides: int, radius: float = 1, color: str = YELLOW, stroke_width: int = 4, **kwargs) -> RegularPolygon:
    """创建正多边形

    Args:
        n_sides: 边数
        radius: 外接圆半径
        color: 颜色
        stroke_width: 边框宽度

    Returns:
        RegularPolygon 对象
    """
    return RegularPolygon(n=n_sides, radius=radius, color=color, stroke_width=stroke_width, **kwargs)


def create_arrow(start: np.ndarray = LEFT, end: np.ndarray = RIGHT, color: str = YELLOW, **kwargs) -> Arrow:
    """创建箭头

    Args:
        start: 起点坐标
        end: 终点坐标
        color: 颜色

    Returns:
        Arrow 对象
    """
    return Arrow(start=start, end=end, color=color, **kwargs)


# =============================================================================
# 函数绘图工具 (Function Plotting)
# =============================================================================

def plot_function(func: callable, x_range: tuple = (-3, 3), color: str = BLUE, axes: Axes = None, **kwargs) -> VMobject:
    """绘制任意函数图像

    Args:
        func: 函数，接受 x 返回 y
        x_range: x 范围 (start, end)
        color: 颜色
        axes: 坐标系对象，可选

    Returns:
        函数图像的 VMobject
    """
    if axes:
        return axes.plot(func, x_range=x_range, color=color, **kwargs)
    return FunctionGraph(func, x_range=x_range, color=color, **kwargs)


def plot_sine(x_range: tuple = (-PI, PI), amplitude: float = 1, color: str = BLUE, axes: Axes = None, **kwargs) -> VMobject:
    """绘制正弦函数图像

    Args:
        x_range: x 范围
        amplitude: 振幅
        color: 颜色
        axes: 坐标系对象

    Returns:
        正弦函数图像
    """
    func = lambda x: amplitude * np.sin(x)
    return plot_function(func, x_range=x_range, color=color, axes=axes, **kwargs)


def plot_cosine(x_range: tuple = (-PI, PI), amplitude: float = 1, color: str = RED, axes: Axes = None, **kwargs) -> VMobject:
    """绘制余弦函数图像

    Args:
        x_range: x 范围
        amplitude: 振幅
        color: 颜色
        axes: 坐标系对象

    Returns:
        余弦函数图像
    """
    func = lambda x: amplitude * np.cos(x)
    return plot_function(func, x_range=x_range, color=color, axes=axes, **kwargs)


def plot_derivative(func: callable, x_range: tuple = (-3, 3), delta: float = 0.001, color: str = YELLOW, axes: Axes = None, **kwargs) -> VMobject:
    """绘制函数的导数图像

    Args:
        func: 原函数
        x_range: x 范围
        delta: 数值求导步长
        color: 颜色
        axes: 坐标系

    Returns:
        导数图像
    """
    deriv = lambda x: (func(x + delta) - func(x - delta)) / (2 * delta)
    return plot_function(deriv, x_range=x_range, color=color, axes=axes, **kwargs)


def plot_integral(func: callable, x_range: tuple = (0, 2), color: str = BLUE, opacity: float = 0.3, axes: Axes = None, **kwargs) -> VGroup:
    """绘制函数的积分面积

    Args:
        func: 被积函数
        x_range: 积分范围
        color: 颜色
        opacity: 透明度
        axes: 坐标系

    Returns:
        包含函数图像和面积的 VGroup
    """
    if axes:
        graph = axes.plot(func, x_range=x_range, color=color)
        area = axes.get_area(graph, x_range=x_range, color=color, opacity=opacity)
        return VGroup(graph, area)
    else:
        axes_obj = Axes(x_range=[x_range[0]-1, x_range[1]+1], y_range=[0, 5])
        graph = axes_obj.plot(func, x_range=x_range, color=color)
        area = axes_obj.get_area(graph, x_range=x_range, color=color, opacity=opacity)
        return VGroup(axes_obj, graph, area)


# =============================================================================
# 动画效果工具 (Animations)
# =============================================================================

def fade_in_transform(mobject: Mobject, run_time: float = 1, lag_ratio: float = 0, **kwargs) -> Animation:
    """淡入动画

    Args:
        mobject: 要动画的对象
        run_time: 动画时长
        lag_ratio: 延迟比例

    Returns:
        FadeIn 动画对象
    """
    return FadeIn(mobject, run_time=run_time, lag_ratio=lag_ratio, **kwargs)


def grow_from_center(mobject: Mobject, run_time: float = 1, **kwargs) -> Animation:
    """从中心生长动画

    Args:
        mobject: 要动画的对象
        run_time: 动画时长

    Returns:
        GrowFromCenter 动画对象
    """
    return GrowFromCenter(mobject, run_time=run_time, **kwargs)


def morph_transform(mobject1: Mobject, mobject2: Mobject, run_time: float = 2, **kwargs) -> Animation:
    """变形动画，将一个对象变成另一个

    Args:
        mobject1: 源对象（会被替换）
        mobject2: 目标对象
        run_time: 动画时长

    Returns:
        Transform 动画对象
    """
    return Transform(mobject1, mobject2, run_time=run_time, **kwargs)


def rotate_and_scale(mobject: Mobject, angle: float = PI, scale_factor: float = 1.5, run_time: float = 1, **kwargs) -> Animation:
    """旋转和缩放组合动画

    Args:
        mobject: 要动画的对象
        angle: 旋转角度（弧度）
        scale_factor: 缩放因子
        run_time: 动画时长

    Returns:
        动画组
    """
    return AnimationGroup(
        Rotate(mobject, angle=angle, run_time=run_time),
        Scale(mobject, scale_factor=scale_factor, run_time=run_time),
        **kwargs
    )


# =============================================================================
# 文本公式工具 (Text & Formulas)
# =============================================================================

def create_formula(formula: str, font_size: float = 48, color: str = WHITE, **kwargs) -> MathTex:
    """创建数学公式

    Args:
        formula: LaTeX 公式字符串
        font_size: 字体大小
        color: 颜色

    Returns:
        MathTex 对象

    Example:
        formula = create_formula(r"E = mc^2")
        formula = create_formula(r"\int_0^\infty e^{-x^2} dx")
    """
    return MathTex(formula, font_size=font_size, color=color, **kwargs)


def create_title(text: str, font_size: float = 72, color: str = WHITE, **kwargs) -> Text:
    """创建标题文本

    Args:
        text: 标题文本
        font_size: 字体大小
        color: 颜色

    Returns:
        Text 对象
    """
    return Text(text, font_size=font_size, color=color, **kwargs)


def create_bullet_points(items: list, font_size: float = 36, color: str = WHITE, buff: float = 0.5, **kwargs) -> VGroup:
    """创建项目符号列表

    Args:
        items: 文本列表
        font_size: 字体大小
        color: 颜色
        buff: 项之间的间距

    Returns:
        包含所有列表项的 VGroup

    Example:
        bullets = create_bullet_points(["第一点", "第二点", "第三点"])
        self.play(Write(bullets))
    """
    bullets = VGroup()
    for item in items:
        bullet = Text(f"• {item}", font_size=font_size, color=color, **kwargs)
        bullets.add(bullet)
    bullets.arrange(DOWN, aligned_edge=LEFT, buff=buff)
    return bullets
