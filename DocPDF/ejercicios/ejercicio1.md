# Espacios tensoriales

1. Considere dos espacios vectoriales de polinomios de grado $\leq 2, \mathcal{P}_2(x)  \text{ y } \mathcal{G}_2(y)$. Se puede construir un espacio tensorial a partir de estos espacios vectoriales mediante el producto exterior $\mathcal{T}_2(xy) = \mathcal{P}_2(x) \otimes  \mathcal{G}_2(y)$ de tal manera que cualquier polinomio de dos variables puede ser escrito como $\mathcal{T}_2(xy) = c^{ij}|e_i^{\mathcal{P}},e_j^{\mathcal{G}} \rangle$. Donde $\{|e_i^{\mathcal{P}}| \rangle$ y $\{ | e_j^{\mathcal{G}} \rangle \}$ corresponden a bases ortogonales para los espacios vectoriales $\mathcal{P}_2(x)$ y $\mathcal{G}_2(y)$, respectivamente.

a) Cosidere el polimonio $p^{\mathcal{P}}(x)=x^2+x+3$ y expréselo en términos de la base de polinomios de Legendre $\{ | e_i^{\mathcal{P}} \rangle \} \leftrightarrow \{ | P_i(x) \rangle \} $ (2 ptos)

Polinomios de Legendre: $\{ 1, x, \frac{1}{2}(3x^2 - 1) \}$



$$
\begin{align*}
c_0(1) + c_1(x) + c_2(\frac{1}{2}(3x^2 -1)) &= x^2 + x + 3 \\
 c_0 + c_1x+ \frac{3}{2}c_2x^2 - \frac{1}{2}c_2 &= x^2 + x +3 \\
c_0 - \frac{1}{2}c_2 &= 3 \\ 
c_1x &= x \\ 
\frac{3}{2}c_2x^2 &= x^2 
\end{align*}
$$

Luego, $c_0=\frac{10}{3}, c_1=1, c_2=\frac{2}{3}$

b) Seleccione ahora dos polinomios $p^{\mathcal{P}}(x) = x^2+x+3$ y $p^{\mathcal{G}}(y)=y+1$. Construya el tensor, $p^{\mathcal{P}\otimes\mathcal{G}}(x,y) = p^{\mathcal{P}}(x) \otimes p^{\mathcal{G}}(y)$, mediante el producto exterior de esos polinomios. (2ptos)

<!-- $$
 p^{\mathcal{P}}(x) \otimes p^{\mathcal{G}}(y) = 
 \begin{bmatrix}
  \frac{10}{3} \\ 
  1 \\ 
  \frac{2}{3}
  \end{bmatrix}
   \begin{bmatrix}
   1 & 1 & 0 
 \end{bmatrix} \cdot
 \begin{bmatrix}
 1 \\ 
 x \\ 
 \frac{1}{2}(3x^2 - 1)
 \end{bmatrix} 
 \begin{bmatrix}
 1 & y & \frac{1}{2}(3y^2 - 1)
 \end{bmatrix} \\[4pt] =
 \begin{bmatrix}
 \frac{10}{3} & \frac{10}{3}  & 0 \\
 1 & 1 & 0\\ 
 \frac{2}{3} &  \frac{2}{3} & 0
 \end{bmatrix} \cdot 
 \begin{bmatrix}
 1 & y & \frac{1}{2}(3y^2 - 1) \\
 x & xy & \frac{x}{2}(3y^2 - 1) \\
 \frac{1}{2}(3x^2 - 1) &  \frac{y}{2}(3x^2 - 1) & 
 \frac{1}{4}(3x^2 - 1)(3y^2 - 1)
 \end{bmatrix} \\ [4pt]
 = \begin{bmatrix}
 \frac{10}{3}  & \frac{10y}{3} & 0 \\
 x & xy & 0 \\
 x^2 -\frac{1}{3} & yx^2 - \frac{y}{3} & 0
 \end{bmatrix}
$$ -->


$$
 p^{\mathcal{P}}(x) \otimes p^{\mathcal{G}}(y) = \begin{bmatrix}
 3 \\ x \\ x^2
 \end{bmatrix} \otimes \begin{bmatrix} 1 & y & 0 \end{bmatrix} =
 \begin{bmatrix} 
 3 & 3y & 0 \\
 x & xy & 0 \\ 
 x^2 & x^2y & 0
 \end{bmatrix}
$$


c)  Elija las bases de monomios $\{ 1, x, x^2\}$ y $\{1, y, y^2 \}$ e identifique las componentes $c^{ij}$ del tensor $p^{\mathcal{P}\otimes \mathcal{G}}(x,y)$ al expandir ese tensor respecto a estas bases en el espacio tensorial $\mathcal{T}_2(xy)=\mathcal{P}_2(x)\otimes \mathcal{G}_2(y).$ (2pts)

$$
p^{\mathcal{P}}(x) = x^2 + x + 3 = \begin{bmatrix} 3 & 1 & 1 \end{bmatrix}
\begin{bmatrix} 1 \\ x \\ x^2 \end{bmatrix}
$$

$$
p^{\mathcal{G}}(y) = y + 1 = \begin{bmatrix} 1 & 1 & 0 \end{bmatrix} 
\begin{bmatrix} 1 \\ y \\ y^2 \end{bmatrix}
$$


$$
p^{\mathcal{P} \otimes \mathcal{G}} = \begin{bmatrix} 
3 \\ x \\ x^2
\end{bmatrix} \otimes \begin{bmatrix} 
1 & y & 0
\end{bmatrix} = \begin{bmatrix}
3 & 3y & 0 \\
x & xy & 0 \\
x^2 & x^2y & 0
\end{bmatrix}
$$

$$
c^{ij} = \begin{bmatrix} 3 \\ 1 \\ 1 \end{bmatrix} \otimes \begin{bmatrix} 1 & 1 & 0 \end{bmatrix} =\begin{bmatrix}
3 & 3 & 0 \\
1 & 1 & 0 \\
1 & 1 & 0
\end{bmatrix}
$$


$$
| e_i^{\mathcal{P}} , e_j^{\mathcal{G}} \rangle = \begin{bmatrix}
1 \\ x \\ x^2
\end{bmatrix} \otimes \begin{bmatrix}
1 & y & y^2
\end{bmatrix} = \begin{bmatrix}
1 & y & y^2 \\
x & xy & xy^2 \\
x^2 & x^2y & x^2y^2
\end{bmatrix}
$$


d) Ahora suponga las bases de polinomios de Legendre, $\{ | e_i^{\mathcal{P}} \rangle \} \leftrightarrow \{ | P_i(x) \rangle \}$ y $\{ | e_j^{\mathcal{G}} \rangle \} \leftrightarrow \{ | P_j(y) \rangle \}$, para $\mathcal{P}_2(x)$ y $\mathcal{G}_2(y)$. Calcule las componentes $\hat{c}^{ij}$ del tensor $p^{\mathcal{P}\otimes \mathcal{G}}(x,y)$ respecto a estas bases en el espacio tensorial $\mathcal{T}_2(xy) = \mathcal{P}_2(x)\otimes \mathcal{G}_2(y).$ (4pts)

$$
p^{\mathcal{P} \otimes \mathcal{G}} = \begin{bmatrix}
3 & 3y & 0 \\
x & xy & 0 \\
x^2 & x^2y & 0
\end{bmatrix}
$$

$$
\mathcal{L}_x = \{ 1, x, \frac{1}{2}(3x^2 - 1) \}
$$

$$
p^{\mathcal{P}}(x)= \begin{bmatrix} 10/3 & 1 & 2/3 \end{bmatrix} \begin{bmatrix}
1 \\ x \\ (1/2)(3x^2 - 1)
\end{bmatrix}
$$

$$
p^{\mathcal{G}}(y) = \begin{bmatrix} 1 & 1 & 0\end{bmatrix} \begin{bmatrix}
1 \\ y \\ (1/2)(3y^2 - 1)
\end{bmatrix}
$$


$$
\hat{c}^{ij} = \begin{bmatrix} 
10/3 \\ 1 \\ 2/3
\end{bmatrix} \otimes \begin{bmatrix}
1 & 1 & 0
\end{bmatrix} = \begin{bmatrix}
10/3 & 10/3 & 0 \\
1 & 1 & 0 \\
2/3 & 2/3 & 0
\end{bmatrix}
$$

$$
| e_i^{\mathcal{P}} , e_j^{\mathcal{G}} \rangle = \begin{bmatrix}
1 \\ x \\ (1/2)(3x^2 - 1)
\end{bmatrix} \otimes \begin{bmatrix}
1 & y & (1/2)(3y^2-1)
\end{bmatrix} = \\ \begin{bmatrix} 
1 & y & (1/2)(3y^2 - 1) \\ 
x & xy & (x/2)(3y^2 - 1) \\ 
(1/2)(3x^2 - 1) & (y/2)(3y^2 - 1) & (1/4)(3x^2 - 1)(3y^2 - 1)
\end{bmatrix}
$$
