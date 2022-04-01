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
p^{\mathcal{P}}(x)= \begin{bmatrix} 1/2 & 1 & 2/3 \end{bmatrix} \begin{bmatrix}
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
1/2 \\ 1 \\ 2/3
\end{bmatrix} \otimes \begin{bmatrix}
1 & 1 & 0
\end{bmatrix} = \begin{bmatrix}
1/2 & 1/2 & 0 \\
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
