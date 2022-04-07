# Los Operadores de Pauli

Expresión matricial para los operadores lineales de Pauli: $\mathbb{R}^2 \rightarrow \mathbb{R}^2$, definidos como

$$
\begin{aligned}
&\sigma_z | + \rangle =  |+\rangle, \quad &&\sigma_z|-\rangle = \ - | - \rangle \\ 
&\sigma_x | + \rangle_x =  |+\rangle_x, \quad  &&\sigma_x|-\rangle_x = \ - | - \rangle_x, \\
&\sigma_y | + \rangle_y =  |+\rangle_y, \quad &&\sigma_y|-\rangle_y = \ - | - \rangle_y 
\end{aligned}
$$  con la base canónica representada por: $|+\rangle \leftrightarrows \begin{pmatrix} 1 \\ 0 \end{pmatrix} $,  $|-\rangle \leftrightarrows \begin{pmatrix} 0 \\ 1 \end{pmatrix}$

Además, tenemos otros dos conjuntos de vectores base

$$
|+\rangle_x = \frac{1}{\sqrt{2}}[|+\rangle + |-\rangle], \quad |-\rangle_x=\frac{1}{\sqrt{2}}[|+\rangle - |-\rangle],\\
|+\rangle_y=\frac{1}{\sqrt{2}}[|+\rangle + i|-\rangle], \quad |-\rangle_y = \frac{1}{\sqrt{2}}[|+\rangle-i|-\rangle],
$$

y sus formas asociadas $\langle x | \leftrightarrows (1, 0 ) \quad \langle - | \leftrightarrows (1, 0)$


## Representaciones Matriciales

La representación matricial de $(\sigma_z^{(+)(-)})^i_j$

$$
(\sigma_z^{(+)(-)})^i_j = 
\begin{pmatrix}
\langle + | \sigma_z | + \rangle & 
\langle + | \sigma_z | - \rangle \\
\langle - | \sigma_z | + \rangle & 
\langle - | \sigma_z | - \rangle
\end{pmatrix} = 
\begin{pmatrix}
1 & 
0 \\
0 & 
-1
\end{pmatrix}
$$

La representación matriicial de $(\sigma_z^{(+x)(-x)})^i_j$


$$
(\sigma_z^{(+x)(-x)})^i_j = 
\begin{pmatrix}
_x\langle + | \sigma_z | + {\rangle}_x & 
_x\langle + | \sigma_z | - {\rangle}_x \\
_x\langle - | \sigma_z | + {\rangle}_x & 
_x\langle - | \sigma_z | - {\rangle}_x 
\end{pmatrix} 
$$


$$
\sigma_z | + {\rangle}_x =  
\sigma_z \Big(\frac{1}{\sqrt{2}}[|+\rangle + | - \rangle]\Big) = 
\frac{1}{\sqrt{2}}[\sigma_z|+\rangle +\sigma_z|-\rangle] =
\frac{1}{\sqrt{2}}[|+\rangle -|-\rangle] =  | - \rangle_x \\
\sigma_z | -\rangle_x = 
\sigma_z\Big(\frac{1}{\sqrt{2}}[|+\rangle - |-\rangle]\Big) = 
 \frac{1}{\sqrt{2}}[\sigma_z|+\rangle - \sigma_z|-\rangle] = 
 \frac{1}{\sqrt{2}}[+\rangle + |-\rangle] = |+ \rangle_x
$$

entonces,
$$
(\sigma_z^{(+x)(-x)})^i_j = 
\begin{pmatrix}
_x\langle + |  - {\rangle}_x & 
_x\langle + |  + {\rangle}_x \\
_x\langle - |  - {\rangle}_x & 
_x\langle - |  + {\rangle}_x 
\end{pmatrix} =
\begin{pmatrix}
0 & 
1 \\
1 & 
0 
\end{pmatrix} 
$$

La representación matricial de $(\sigma_x^{(+y)(-y)})^i_j$

$$
(\sigma_x^{(+y)(-y)})^i_j  = 
\begin{pmatrix}
_y\langle + | \sigma_z | + {\rangle}_y & 
_y\langle + | \sigma_z | - {\rangle}_y \\
_y\langle - | \sigma_z | + {\rangle}_y & 
_y\langle - | \sigma_z | - {\rangle}_y 
\end{pmatrix} 
$$

$$
\sigma_z|+\rangle_y=
\sigma_z\Big( \frac{1}{\sqrt{2}} [|+\rangle + i|-\rangle] \Big) =
\frac{1}{\sqrt{2}}[ \sigma_z|+\rangle + i\sigma_z|-\rangle ] = 
\frac{1}{\sqrt{2}}[|+\rangle - i |-\rangle] = |-\rangle_y \\
\sigma_z|-\rangle_y=
\sigma_z\Big( \frac{1}{\sqrt{2}} [|+\rangle - i|-\rangle] \Big) =
\frac{1}{\sqrt{2}}[ \sigma_z|+\rangle - i\sigma_z|-\rangle ] = 
\frac{1}{\sqrt{2}}[|+\rangle + i |-\rangle] = |+\rangle_y
$$

entonces,

$$
(\sigma_x^{(+y)(-y)})^i_j  = 
\begin{pmatrix}
_y\langle + | - {\rangle}_y & 
_y\langle + | + {\rangle}_y \\
_y\langle - | - {\rangle}_y & 
_y\langle - | + {\rangle}_y 
\end{pmatrix} =
\begin{pmatrix}
0 & 
1 \\
1 & 
0 
\end{pmatrix} 
$$


