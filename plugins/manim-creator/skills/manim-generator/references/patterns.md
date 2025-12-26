# Manim 代码模式参考

常见场景的代码模式和完整示例。

## 函数可视化

### 正弦函数
```python
from manim import *
import numpy as np

class SineWave(Scene):
    def construct(self):
        axes = Axes(x_range=[-PI, PI, PI/4], y_range=[-2, 2, 0.5])
        sine = axes.plot(lambda x: np.sin(x), color=BLUE)
        label = axes.get_graph_label(sine, "sin(x)")
        self.play(Create(axes), Create(sine), Write(label))
        self.wait()
```

### 导数可视化
```python
class DerivativeScene(Scene):
    def construct(self):
        func = lambda x: x**2
        deriv = lambda x: 2*x
        axes = Axes(x_range=[-2, 2], y_range=[-1, 4])
        f_graph = axes.plot(func, color=BLUE)
        d_graph = axes.plot(deriv, color=RED)
        self.play(Create(f_graph))
        self.play(Create(d_graph))
```

### 积分面积
```python
class IntegralScene(Scene):
    def construct(self):
        axes = Axes(x_range=[0, 3], y_range=[0, 2])
        graph = axes.plot(lambda x: x**2/4, x_range=[0, 2], color=BLUE)
        area = axes.get_area(graph, x_range=[0, 2], color=BLUE, opacity=0.3)
        self.play(Create(axes), Create(graph), FadeIn(area))
```

## 几何图形

### 基本图形组合
```python
class BasicShapes(Scene):
    def construct(self):
        circle = Circle(radius=1, color=BLUE)
        square = Square(side_length=2, color=RED)
        triangle = Triangle(color=GREEN)
        shapes = VGroup(circle, square, triangle).arrange(RIGHT, buff=1)
        self.play(Create(shapes))
```

### 多边形
```python
class PolygonScene(Scene):
    def construct(self):
        hexagon = RegularPolygon(n=6, color=YELLOW)
        pentagon = RegularPolygon(n=5, color=ORANGE)
        VGroup(hexagon, pentagon).arrange(RIGHT, buff=1)
        self.play(Create(hexagon), Create(pentagon))
```

## 动画变换

### 形状变形
```python
class MorphScene(Scene):
    def construct(self):
        circle = Circle(color=BLUE)
        square = Square(color=RED)
        self.play(Create(circle))
        self.play(Transform(circle, square))
```

### 旋转缩放
```python
class RotateScaleScene(Scene):
    def construct(self):
        square = Square(color=BLUE)
        self.play(Create(square))
        self.play(Rotate(square, angle=PI/4), scale_square_about_point(square, 2, ORIGIN))
```

### 序列动画
```python
class AnimationSequence(Scene):
    def construct(self):
        circle = Circle(color=BLUE)
        square = Square(color=RED)
        triangle = Triangle(color=GREEN)
        self.play(Create(circle))
        self.play(FadeOut(circle), FadeIn(square))
        self.play(FadeOut(square), FadeIn(triangle))
```

## 数学公式

### 公式动画展示
```python
class FormulaAnimation(Scene):
    def construct(self):
        formula = MathTex(r"E = mc^2", font_size=72)
        self.play(Write(formula))
        self.wait()
```

### 公式推导
```python
class DerivationScene(Scene):
    def construct(self):
        eq1 = MathTex(r"(a+b)^2")
        eq2 = MathTex(r"= a^2 + 2ab + b^2")
        self.play(Write(eq1))
        self.play(Transform(eq1, eq2))
```

### 多行公式
```python
class MultiLine(Scene):
    def construct(self):
        lines = VGroup(
            MathTex(r"f(x) = x^2"),
            MathTex(r"f'(x) = 2x"),
            MathTex(r"f''(x) = 2")
        ).arrange(DOWN, aligned_edge=LEFT)
        self.play(Write(lines))
```

## 坐标系

### 带坐标系的函数图
```python
class WithAxes(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-3, 3, 1],
            x_length=10,
            y_length=6
        )
        graph = axes.plot(lambda x: np.sin(x), color=BLUE)
        self.play(Create(axes), Create(graph))
```

## 文本和标签

### 带标签的图形
```python
class LabeledShapes(Scene):
    def construct(self):
        circle = Circle(radius=1, color=BLUE)
        label = Text("Circle").next_to(circle, DOWN)
        self.play(Create(circle), Write(label))
```

### 列表展示
```python
class BulletPoints(Scene):
    def construct(self):
        items = VGroup(
            Text("• Point 1"),
            Text("• Point 2"),
            Text("• Point 3")
        ).arrange(DOWN, aligned_edge=LEFT)
        self.play(Write(items))
```

## 颜色和样式

### 渐变色
```python
class GradientColor(Scene):
    def construct(self):
        circle = Circle(radius=2, stroke_width=10)
        circle.set_stroke(color=[BLUE, RED], gradient=True)
        self.play(Create(circle))
```

### 透明度
```python
class OpacityScene(Scene):
    def construct(self):
        square = Square(side_length=3, color=BLUE, fill_opacity=0.5)
        self.play(FadeIn(square))
```
