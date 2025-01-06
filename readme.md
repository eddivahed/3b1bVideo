# Lorenz Attractor Visualization with Manim

This project demonstrates how to create a visualization of the Lorenz Attractor using ManimGL, the mathematical animation engine used by 3Blue1Brown.

## Project Overview

The Lorenz Attractor is a chaotic system that demonstrates the butterfly effect - how small changes in initial conditions can lead to drastically different outcomes. This visualization shows multiple trajectories of the system with slightly different starting points.

## Prerequisites

- Python 3.10 or higher
- ManimGL
- scipy
- LaTeX distribution

## Installation Steps

1. **Create a Python Virtual Environment**
```bash
python3.10 -m venv manim-env
source manim-env/bin/activate
```

2. **Install ManimGL**
```bash
git clone https://github.com/3b1b/manim.git
cd manim
pip install -e .
```

3. **Install Required Dependencies**
```bash
pip install scipy
```

4. **Install LaTeX** (if not already installed)
   - Download MacTeX from https://www.tug.org/mactex/mactex-download.html
   - Install the downloaded package
   - Add LaTeX to your PATH:
```bash
echo 'export PATH="/Library/TeX/texbin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

## Troubleshooting Steps We Encountered

1. **Python Version Issues**
   - Initial error with IPython compatibility
   - Solution: Upgraded to Python 3.10

2. **LaTeX Installation Issues**
   - Homebrew installation conflicts
   - Solution: Direct installation from MacTeX website

3. **Import Issues**
   - `manim_imports_ext` not found
   - Solution: Updated imports to use `manimlib`

4. **Camera Orientation Issues**
   - Incorrect camera setup methods
   - Solution: Updated to use correct ManimGL camera controls

## The Code

```python
from manimlib import *
from scipy.integrate import solve_ivp
import numpy as np

[Main code content...]
```

## Running the Animation

To run the visualization:
```bash
manimgl lorenz.py LorenzAttractor
```

## Understanding the Visualization

The animation shows:
1. A 3D coordinate system
2. The Lorenz system equations displayed in the upper left
3. Multiple trajectories with slightly different initial conditions
4. A rotating view to show the 3D structure

## Key Components

1. **Lorenz System Equations**
   - dx/dt = σ(y - x)
   - dy/dt = x(ρ - z) - y
   - dz/dt = xy - βz

2. **Parameters**
   - σ (sigma) = 10
   - ρ (rho) = 28
   - β (beta) = 8/3

3. **Visualization Features**
   - Rotating 3D view
   - Color-coded trajectories
   - LaTeX rendered equations

## Common Issues and Solutions

1. **LaTeX Not Found Error**
   - Symptom: "FileNotFoundError: [Errno 2] No such file or directory: 'latex'"
   - Solution: Add LaTeX to PATH and ensure proper installation

2. **Camera Orientation**
   - Symptom: Camera orientation methods not working
   - Solution: Use `self.frame.set_euler_angles()` instead of `set_camera_orientation()`

## Resources

- [ManimGL Documentation](https://3b1b.github.io/manim/)
- [Lorenz System on Wikipedia](https://en.wikipedia.org/wiki/Lorenz_system)
- [3Blue1Brown YouTube Channel](https://www.youtube.com/@3blue1brown)

## Next Steps

- Add interactive parameters
- Implement color gradients based on velocity
- Add more educational annotations
- Explore different initial conditions

## License

This project is licensed under the MIT License - see the LICENSE file for details.