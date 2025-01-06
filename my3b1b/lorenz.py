from manimlib import *
from scipy.integrate import solve_ivp
import numpy as np

def lorenz_system(t, state, sigma=10, rho=28, beta=8/3):
    x, y, z = state
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]

def ode_solution_points(function, state0, time, dt=0.01):
    solution = solve_ivp(
        function,
        t_span=(0, time),
        y0=state0,
        t_eval=np.arange(0, time, dt)
    )
    return solution.y.T

class LorenzAttractor(Scene):
    def construct(self):
        # Set up axes
        axes = ThreeDAxes(
            x_range=(-50, 50, 5),
            y_range=(-50, 50, 5),
            z_range=(-0, 50, 5),
            width=16,
            height=16,
            depth=8,
        )
        axes.set_width(FRAME_WIDTH)
        axes.center()
        
        # Camera setup for ManimGL
        self.frame.set_euler_angles(
            theta=45 * DEGREES,
            phi=75 * DEGREES
        )
        self.frame.add_updater(
            lambda m, dt: m.increment_theta(0.2 * dt)
        )
        
        self.add(axes)

        # Add the equations
        equations = Tex(
            R"""
            \begin{aligned}
            \frac{\mathrm{d} x}{\mathrm{~d} t} & =\sigma(y-x) \\
            \frac{\mathrm{d} y}{\mathrm{~d} t} & =x(\rho-z)-y \\
            \frac{\mathrm{d} z}{\mathrm{~d} t} & =x y-\beta z
            \end{aligned}
            """,
            tex_to_color_map={
                "x": RED,
                "y": GREEN,
                "z": BLUE,
            },
            font_size=30
        )
        equations.to_corner(UL)
        equations.fix_in_frame()
        self.add(equations)
        
        # Compute a set of solutions
        epsilon = 1e-5
        evolution_time = 30
        n_points = 10
        states = [
            [10, 10, 10 + n * epsilon]
            for n in range(n_points)
        ]
        colors = color_gradient([BLUE_E, BLUE_A], n_points)
        curves = VGroup()
        
        for state, color in zip(states, colors):
            points = ode_solution_points(lorenz_system, state, evolution_time)
            curve = VMobject().set_points_smoothly([axes.c2p(*p) for p in points])
            curve.set_stroke(color, 1, opacity=0.25)
            curves.add(curve)
        
        curves.set_stroke(width=2, opacity=1)
        
        # Create and animate the paths
        self.play(
            *[ShowCreation(curve, rate_func=linear) for curve in curves],
            run_time=evolution_time
        )
        
        self.wait(2)