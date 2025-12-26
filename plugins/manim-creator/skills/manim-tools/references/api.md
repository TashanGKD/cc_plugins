# Manim Tools API 参考

完整的工具函数 API 文档。

## 几何图形 (Geometric Shapes)

### `create_circle(radius=1, color=BLUE, stroke_width=4, **kwargs)`

创建圆形。

**参数:**
- `radius` (float): 半径，默认 1
- `color` (str): 颜色，默认 BLUE
- `stroke_width` (int): 边框宽度，默认 4

**返回:** Circle 对象

**示例:**
```python
circle = create_circle(radius=2, color=RED)
```

---

### `create_square(side_length=2, color=RED, stroke_width=4, **kwargs)`

创建正方形。

**参数:**
- `side_length` (float): 边长，默认 2
- `color` (str): 颜色，默认 RED
- `stroke_width` (int): 边框宽度，默认 4

**返回:** Square 对象

---

### `create_triangle(side_length=2, color=GREEN, stroke_width=4, **kwargs)`

创建等边三角形。

**参数:**
- `side_length` (float): 边长，默认 2
- `color` (str): 颜色，默认 GREEN
- `stroke_width` (int): 边框宽度，默认 4

**返回:** Triangle 对象

---

### `create_polygon(n_sides, radius=1, color=YELLOW, stroke_width=4, **kwargs)`

创建正多边形。

**参数:**
- `n_sides` (int): 边数
- `radius` (float): 外接圆半径，默认 1
- `color` (str): 颜色，默认 YELLOW
- `stroke_width` (int): 边框宽度，默认 4

**返回:** RegularPolygon 对象

**示例:**
```python
hexagon = create_polygon(n_sides=6)
octagon = create_polygon(n_sides=8, color=ORANGE)
```

---

### `create_arrow(start=LEFT, end=RIGHT, color=YELLOW, **kwargs)`

创建箭头。

**参数:**
- `start` (np.ndarray): 起点坐标，默认 LEFT (-3, 0, 0)
- `end` (np.ndarray): 终点坐标，默认 RIGHT (3, 0, 0)
- `color` (str): 颜色，默认 YELLOW

**返回:** Arrow 对象

**示例:**
```python
arrow = create_arrow(start=LEFT*2, end=RIGHT*2, color=RED)
```

---

## 函数绘图 (Function Plotting)

### `plot_function(func, x_range=(-3, 3), color=BLUE, axes=None, **kwargs)`

绘制任意函数图像。

**参数:**
- `func` (callable): 函数，接受 x 返回 y
- `x_range` (tuple): x 范围 (start, end)，默认 (-3, 3)
- `color` (str): 颜色，默认 BLUE
- `axes` (Axes): 坐标系对象，可选

**返回:** VMobject (函数图像)

**示例:**
```python
# 绘制二次函数
quad = plot_function(lambda x: x**2, color=GREEN)

# 使用坐标系
axes = Axes(x_range=[-5, 5], y_range=[-2, 10])
graph = plot_function(lambda x: x**2, axes=axes)
```

---

### `plot_sine(x_range=(-PI, PI), amplitude=1, color=BLUE, axes=None, **kwargs)`

绘制正弦函数图像。

**参数:**
- `x_range` (tuple): x 范围，默认 (-π, π)
- `amplitude` (float): 振幅，默认 1
- `color` (str): 颜色，默认 BLUE
- `axes` (Axes): 坐标系对象，可选

**返回:** VMobject (正弦函数图像)

---

### `plot_cosine(x_range=(-PI, PI), amplitude=1, color=RED, axes=None, **kwargs)`

绘制余弦函数图像。

**参数:**
- `x_range` (tuple): x 范围，默认 (-π, π)
- `amplitude` (float): 振幅，默认 1
- `color` (str): 颜色，默认 RED
- `axes` (Axes): 坐标系对象，可选

**返回:** VMobject (余弦函数图像)

---

### `plot_derivative(func, x_range=(-3, 3), delta=0.001, color=YELLOW, axes=None, **kwargs)`

绘制函数的导数图像（数值求导）。

**参数:**
- `func` (callable): 原函数
- `x_range` (tuple): x 范围，默认 (-3, 3)
- `delta` (float): 数值求导步长，默认 0.001
- `color` (str): 颜色，默认 YELLOW
- `axes` (Axes): 坐标系对象，可选

**返回:** VMobject (导数图像)

**示例:**
```python
# x^2 的导数是 2x
f = lambda x: x**2
df = plot_derivative(f, color=RED)
```

---

### `plot_integral(func, x_range=(0, 2), color=BLUE, opacity=0.3, axes=None, **kwargs)`

绘制函数的积分面积。

**参数:**
- `func` (callable): 被积函数
- `x_range` (tuple): 积分范围，默认 (0, 2)
- `color` (str): 颜色，默认 BLUE
- `opacity` (float): 填充透明度，默认 0.3
- `axes` (Axes): 坐标系对象，可选

**返回:** VGroup (包含函数图像和面积)

---

## 动画效果 (Animations)

### `fade_in_transform(mobject, run_time=1, lag_ratio=0, **kwargs)`

淡入动画。

**参数:**
- `mobject` (Mobject): 要动画的对象
- `run_time` (float): 动画时长（秒），默认 1
- `lag_ratio` (float): 延迟比例，默认 0

**返回:** FadeIn 动画对象

---

### `grow_from_center(mobject, run_time=1, **kwargs)`

从中心生长动画。

**参数:**
- `mobject` (Mobject): 要动画的对象
- `run_time` (float): 动画时长（秒），默认 1

**返回:** GrowFromCenter 动画对象

---

### `morph_transform(mobject1, mobject2, run_time=2, **kwargs)`

变形动画，将一个对象变成另一个。

**参数:**
- `mobject1` (Mobject): 源对象（会被替换）
- `mobject2` (Mobject): 目标对象
- `run_time` (float): 动画时长（秒），默认 2

**返回:** Transform 动画对象

**示例:**
```python
circle = Circle()
square = Square()
self.play(Create(circle))
self.play(morph_transform(circle, square))  # circle 变成 square
```

---

### `rotate_and_scale(mobject, angle=PI, scale_factor=1.5, run_time=1, **kwargs)`

旋转和缩放组合动画。

**参数:**
- `mobject` (Mobject): 要动画的对象
- `angle` (float): 旋转角度（弧度），默认 π
- `scale_factor` (float): 缩放因子，默认 1.5
- `run_time` (float): 动画时长（秒），默认 1

**返回:** AnimationGroup

---

## 文本公式 (Text & Formulas)

### `create_formula(formula, font_size=48, color=WHITE, **kwargs)`

创建数学公式（LaTeX）。

**参数:**
- `formula` (str): LaTeX 公式字符串
- `font_size` (float): 字体大小，默认 48
- `color` (str): 颜色，默认 WHITE

**返回:** MathTex 对象

**示例:**
```python
einstein = create_formula(r"E = mc^2")
integral = create_formula(r"\int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}")
```

---

### `create_title(text, font_size=72, color=WHITE, **kwargs)`

创建标题文本。

**参数:**
- `text` (str): 标题文本
- `font_size` (float): 字体大小，默认 72
- `color` (str): 颜色，默认 WHITE

**返回:** Text 对象

---

### `create_bullet_points(items, font_size=36, color=WHITE, buff=0.5, **kwargs)`

创建项目符号列表。

**参数:**
- `items` (list): 文本列表
- `font_size` (float): 字体大小，默认 36
- `color` (str): 颜色，默认 WHITE
- `buff` (float): 项之间的间距，默认 0.5

**返回:** VGroup (包含所有列表项)

**示例:**
```python
points = create_bullet_points(["第一点", "第二点", "第三点"])
self.play(Write(points))
```

---

## 常用常量

```python
from manim import *
import numpy as np

# 角度
PI = np.pi           # π
TAU = 2 * np.pi      # 2π

# 方向
LEFT = LEFT          # 左 (-1, 0, 0)
RIGHT = RIGHT        # 右 (1, 0, 0)
UP = UP              # 上 (0, 1, 0)
DOWN = DOWN          # 下 (0, -1, 0)
ORIGIN = ORIGIN      # 原点 (0, 0, 0)

# 颜色
BLUE, RED, GREEN, YELLOW, WHITE, BLACK
ORANGE, PURPLE, PINK, GRAY
```
