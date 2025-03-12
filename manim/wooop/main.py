from manim import *
import numpy as np

class AxesTemplate(Scene):
    def construct(self):
        graph = Axes(
            x_range=[-1,10,1],
            y_range=[-1,10,1],
            x_length=9,
            y_length=6,
            axis_config={"include_tip":False}
        )
        labels = graph.get_axis_labels()
        #self.add(graph, labels)

        cos_func = FunctionGraph( lambda t: np.cos(t) + 0.5 * np.cos(7 * t) + (1 / 7) * np.cos(14 * t),
            color=RED,
        )

        #self.play(Create(graph), Write(labels), run_time=2, rate_func=linear)
        self.add(graph, labels)
        self.play(Create(cos_func), run_time=5, rate_func=linear)
        


