from functools import cache
from math import comb
from pathlib import Path

import numpy as np
import plotly.graph_objects as go
from tqdm import tqdm


@cache
def prob_a(a: int, b: int) -> float:
  if a < 2:
    return 0
  return comb(a, 2) / comb(a + b, 2)


@cache
def prob_b(a: int, b: int) -> float:
  if b < 2:
    return 0
  return comb(b, 2) / comb(a + b, 2)


@cache
def prob_c(a: int, b: int) -> float:
  if a < 1 or b < 1:
    return 0
  return comb(a, 1) * comb(b, 1) / comb(a + b, 2)


@cache
def prob(a: int, b: int) -> float:
  if a <= 0:
    return 1.0
  if b <= 0:
    return 0.0

  alpha = prob_a(a, b)
  beta = prob_b(a, b)
  gamma = prob_c(a, b)
  y = prob(a - 2, b)
  z = prob(a, b - 1)
  return (gamma * z + alpha * y) / (1 - beta)


def build_grid(max_a: int, max_b: int) -> np.ndarray:
  grid = np.zeros((max_a + 1, max_b + 1), dtype=float)
  for a in tqdm(range(max_a + 1)):
    for b in range(max_b + 1):
      grid[a, b] = prob(a, b)
  return grid


def main(max_a: int = 100, max_b: int = 100) -> None:
  grid = build_grid(max_a=max_a, max_b=max_b)
  z = grid[1:, 1:]
  a_values = np.arange(1, max_a + 1)
  b_values = np.arange(1, max_b + 1)

  heatmap_fig = go.Figure(
    data=go.Heatmap(
      x=b_values,
      y=a_values,
      z=z,
      colorscale="Viridis",
      colorbar={"title": "P(a, b)"},
    )
  )
  heatmap_fig.update_layout(
    title="Recursive option probabilities (2D heatmap, 1 ≤ a,b ≤ 100)",
    xaxis_title="b",
    yaxis_title="a",
  )

  surface_fig = go.Figure(
    data=go.Surface(
      x=b_values,
      y=a_values,
      z=z,
      colorscale="Viridis",
      colorbar={"title": "P(a, b)"},
    )
  )
  surface_fig.update_layout(
    title="Recursive option probabilities (3D surface, 1 ≤ a,b ≤ 100)",
    scene={
      "xaxis_title": "b",
      "yaxis_title": "a",
      "zaxis_title": "P(a, b)",
    },
  )

  base = Path(__file__).parent
  heatmap_path = base / "recursive_plot_a100_b100_heatmap.html"
  surface_path = base / "recursive_plot_a100_b100_surface3d.html"
  heatmap_fig.write_html(heatmap_path, include_plotlyjs="cdn")
  surface_fig.write_html(surface_path, include_plotlyjs="cdn")
  print(heatmap_path)
  print(surface_path)


if __name__ == "__main__":
  main()
