# Smale's 7th Problem

## Overview
smale7 is an open-source Python package providing PyTorch models, algorithms, and numerical optimizations for distributions of points on the hypersphere. The most prominent application is the 7th problem from [Smale's list of eighteen unsolved problems in mathematics](https://en.wikipedia.org/wiki/Smale%27s_problems). This repo is a collective effort to solve numerical and algorithmic problems including Smale's 7th problem, the (generalized) Thomson problem, the Tammes problem, and (quantum) spherical $t$-design.

---

Let $f$ be a decreasing real-valued function and $x = (x_1,\ldots, x_N)$ be points on the 2D sphere. The energy is defined as $E(x) = \sum_{i < j} f(\Vert x_i - x_j\Vert )$. A series of unsolved problems in mathematics concerns configurations of points $x$ minimizing the energy $E(x)$. Important instantiations are:
- Generalized Thomson Problem: $E(x) = \sum_{i < j} \Vert x_i - x_j\Vert^{-s}$ with $s\in\mathbf{R}$. Goal: Find minimum energy $E_{min}$.<br>
This problem arises in physics and chemistry as the minimum electrostatic potential energy configuration of N electrons constrained to the surface of a unit sphere that repel each other with a force given by Coulomb's law ($s=1$). A configuration of points $x$ with minimal energy $E(x) = E_{min}$ is called elliptic Fekete points.

-  Smale's 7th Problem: $E(x) = -\sum_{i < j} \log \Vert x_i - x_j\Vert$. Goal: Find algorithm for $x$ such that $E(x) - E_{min} < c \log N$ for some universal constant $c\in\mathbb{R}$.<br>
Algorithm means in the BSS model of computation running time bounded by a polynomial in N.

---

<div style="text-align: center;">
  <img src="assets/optimization456.gif" alt="Optimization Process" style="width: 100%; height: auto;">
</div>


---


## Scope
- PyTorch implementation of gradient-based, simulated annealing, and normalizing flow solutions
- Training and inference code (requires CUDA 11.8)
- Visualization of vector fields and elliptic Fekete points
- Approximate (polynomial time) algorithm for optimal initial point selection

---

## Setup
```bash
conda env create -f environment.yml
conda activate thomson
```
