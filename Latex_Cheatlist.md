---
tags:
  - workflow
  - tools
  - math
---

# LaTeX Cheat Sheet

## Basic Operations & Formatting
| Syntax | Output | Note |
| :--- | :--- | :--- |
| `\frac{a}{b}` | $\frac{a}{b}$ | Fractions |
| `x^{2}` / `x_{i}` | $x^{2}$ / $x_{i}$ | Superscript / Subscript |
| `\sqrt{x}` / `\sqrt[n]{x}` | $\sqrt{x}$ / $\sqrt[n]{x}$ | Square / $n$-th root |
| `\mathbf{v}` / `\vec{v}` | $\mathbf{v}$ / $\vec{v}$ | Bold vector / Arrow vector |
| `\text{text}` | $\text{text}$ | Plain text inside math blocks |
| `\,` / `\quad` | $a\,b \quad c$ | Small space / Large space |

## Calculus & Analysis
| Syntax | Output |
| :--- | :--- |
| `\lim_{x \to 0}` | $\lim_{x \to 0}$ |
| `\sum_{i=1}^{n}` | $\sum_{i=1}^{n}$ |
| `\int_{a}^{b} f(x) \, dx` | $\int_{a}^{b} f(x) \, dx$ |
| `\partial f / \partial x` | $\partial f / \partial x$ |
| `\infty` | $\infty$ |

## Logic, Sets & Relations
| Syntax | Output | Syntax | Output |
| :--- | :--- | :--- | :--- |
| `\implies` | $\implies$ | `\iff` | $\iff$ |
| `\rightarrow` | $\rightarrow$ | `\leftarrow` | $\leftarrow$ |
| `\in` | $\in$ | `\notin` | $\notin$ |
| `\neq` | $\neq$ | `\approx` | $\approx$ |
| `\le` | $\le$ | `\ge` | $\ge$ |
| `\forall` | $\forall$ | `\exists` | $\exists$ |

## Essential Environments

### Multi-line Equations (Aligned)
```latex
$$\begin{aligned}   f(x) &= (x + 1)^2 \\        &= x^2 + 2x + 1 \end{aligned}$$
```
$$
\begin{aligned}
  f(x) &= (x + 1)^2 \\
       &= x^2 + 2x + 1
\end{aligned}
$$

### Piecewise Functions (Cases)
```latex
$$f(x) =  \begin{cases}    x & \text{if } x \ge 0 \\    -x & \text{if } x < 0  \end{cases}$$
```
$$
f(x) = 
\begin{cases} 
  x & \text{if } x \ge 0 \\ 
  -x & \text{if } x < 0 
\end{cases}
$$

### Matrices
```latex
$$A = \begin{pmatrix}    a & b \\    c & d  \end{pmatrix}, \quad B = \begin{bmatrix}    1 & 0 \\    0 & 1  \end{bmatrix}$$
```
$$
A = \begin{pmatrix} 
  a & b \\ 
  c & d 
\end{pmatrix}, \quad
B = \begin{bmatrix} 
  1 & 0 \\ 
  0 & 1 
\end{bmatrix}
$$