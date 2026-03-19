import numpy as np
from manim import *

class FourierAnimation(Scene):
    def construct(self):
        # ===== 1. ЗАГОЛОВОК =====
        title = Text("Ряд Фурье", font_size=48, color=WHITE)
        title.to_edge(UP)

        background = Rectangle(
            width=title.width + 1.0,
            height=title.height + 1.0,
            color=YELLOW,
            fill_opacity=0.5
        ).move_to(title)

        title_frame = SurroundingRectangle(
            title,
            buff=0.4,
            color=RED,
            stroke_width=3
        )

        self.add(background, title, title_frame)

        # ===== 2. ФОРМУЛА =====
        formula = MathTex(
            r"f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty} \left[ a_n \cos(nx) + b_n \sin(nx) \right]",
            tex_to_color_map={
                r"f(x)": YELLOW,
                r"\frac{a_0}{2}": BLUE,
                r"\sum_{n=1}^{\infty}": TEAL,
                r"a_n": GREEN,
                r"\cos(nx)": RED,
                r"b_n": ORANGE,
                r"\sin(nx)": PURPLE,
            },
            font_size=36
        )
        formula.next_to(title, DOWN, buff=1.5)

        formula_frame = RoundedRectangle(
            width=formula.width + 1.0,
            height=formula.height + 0.8,
            corner_radius=0.3,
            color=TEAL,
            stroke_width=4,
            fill_color=TEAL,
            fill_opacity=0.1
        ).move_to(formula)

        outer_frame = RoundedRectangle(
            width=formula.width + 1.2,
            height=formula.height + 1.0,
            corner_radius=0.4,
            color=GOLD,
            stroke_width=1,
            fill_opacity=0
        ).move_to(formula)

        self.play(Write(formula))
        self.play(Create(formula_frame), Create(outer_frame))
        self.wait(2)

        # ===== 3. ОЧИСТКА И ОСИ =====
        self.play(
            FadeOut(formula), FadeOut(formula_frame), FadeOut(outer_frame),
            FadeOut(title), FadeOut(background), FadeOut(title_frame),
            run_time=1
        )

        axes = Axes(
            x_range=[-2 * np.pi, 2 * np.pi, np.pi/2],
            y_range=[-2, 2, 1],
            x_length=10,
            y_length=6,
        )
        self.play(Create(axes), run_time=2)
        self.wait(1)

        # Целевая функция (Квадратная волна)
        square_wave = axes.plot(
            lambda x: np.sign(np.sin(x)),
            x_range=[-2 * np.pi, 2 * np.pi],
            color=YELLOW,
            stroke_width=4,
        )
        square_label = Text("Целевая функция", color=YELLOW, font_size=28)
        square_label.move_to([2, 2.2, 0]) # Фиксированная позиция для красоты

        self.play(Create(square_wave), Write(square_label), run_time=2)
        self.wait(2)