# Desarrollo Punto 5


Considere el espacio vectorial de las matrices complejas $2\times2$ hermíticas. Tal y como demostramos con rigor en la sección 4.3.2.2 y lo detallamos en la sección 4.4.9, una matriz hermetíca (o autoadjunta) séra igual a su adjunta. Esto es, una matriz será igual a su transpuesta conjugada $(A^{\dagger})^i_j \rightarrow (A^*)^i_j \equiv A^i_j.$

$$ A \iff 
\begin{pmatrix}
z_1 & z_2 \\
z_3 & z_4 
\end{pmatrix} \equiv A^{\dagger} = 
\begin{pmatrix}
z_1^* & z_3^* \\
z_2^* & z_4^* 
\end{pmatrix} \quad \text{es decir} 
     \begin{cases}
        z_1^* = z_1 \text{ real}\\
        z_4^* = z_4 \text{ real}\\
        z_2^* = z_3 \text{ complejo}\\
     \end{cases}
$$

Entonces

(a). Muestre que las matrices de Pauli $ \{ \sigma_0 , \sigma_1 , \sigma_2 , \sigma_3 \} $ presentadas en los ejercicios de la sección 2.2.4 forman una base para ese espacio vectorial.

**Condiciones**

1) Todos las matrices de Pauli pertenencen al espacio vectorial? Si

$$ \sigma_1 = 
\begin{pmatrix}
0 &  1 \\
1 &  0 
\end{pmatrix}, 
\sigma_2 = 
\begin{pmatrix}
0 &  -i \\
i &  0 
\end{pmatrix}, 
\sigma_3 = 
\begin{pmatrix}
1 &  0 \\
0 &  -1 
\end{pmatrix},
\sigma_0 \equiv \textbf{I} = 
\begin{pmatrix}
1 &  0 \\
0 &   1
\end{pmatrix}
$$

2) Son linealmente independientes?


$$ a\cdot\sigma_1 +b\cdot\sigma_2 +c\cdot\sigma_3 +d\cdot\sigma_0 = 0\\ 
= a \begin{pmatrix}
0 &  1 \\
1 &  0 
\end{pmatrix} + 
b \begin{pmatrix}
0 &  -i \\
i &  0 
\end{pmatrix} + 
c \begin{pmatrix}
1 &  0 \\
0 &  -1 
\end{pmatrix} +
d \begin{pmatrix}
1 &  0 \\
0 &   1
\end{pmatrix} = 0 \\ 
= \begin{pmatrix}
c+d &  a-bi \\
a+bi &   -c+d
\end{pmatrix} $$

con esto tenemos que

$$
c + d = 0 \\
-c+d = 0 \\
a + bi = 0 \\
a - bi = 0
$$

Luego, $a=b=c=d=0$


3) Todo elemento del espacio vectorial se puede escribir como una combinación lineal de las matrices de Pauli?


Dada una matriz hermetica $A$


$$
A =  \begin{pmatrix}
z_1 & z_2 \\
z_3 & z_4 
\end{pmatrix} = 
a\cdot\sigma_1 +b\cdot\sigma_2 +c\cdot\sigma_3 +d\cdot\sigma_0 \\
= a \begin{pmatrix}
0 &  1 \\
1 &  0 
\end{pmatrix} + 
b \begin{pmatrix}
0 &  -i \\
i &  0 
\end{pmatrix} + 
c \begin{pmatrix}
1 &  0 \\
0 &  -1 
\end{pmatrix} +
d \begin{pmatrix}
1 &  0 \\
0 &   1
\end{pmatrix} 
$$

Tenemos que,

$$
z_1 = a\cdot0+b\cdot0+c\cdot1+d\cdot1 = c + d \quad \text{real} \\ 
z_4 = a\cdot0+b\cdot0-c\cdot1+d\cdot1 = - c + d \quad \text{real} \\ 
z_2 = a - bi \quad \text{complejo} \\
z_3 = a + bi \quad \text{complejo} \\
z_2^* = (a-bi)^* = a+bi = z_3 \qquad  \blacksquare
$$

(b). Compruebe que una base es ortogonal bajo la definición de producto interno $\langle a | b \rangle \Leftrightarrow \text{Tr}(A^{\dagger}B)$ que introducimos en los ejercicios de la misma sección


Productos internos $\langle \sigma^i | \sigma_j \rangle, i \neq j $

$$ 
\begin{align*}  \langle \sigma_1 | \sigma_2 \rangle  &= 
\text{Tr} \bigg[
\begin{pmatrix}
0 &  1 \\
1 &  0 
\end{pmatrix} 
\begin{pmatrix}
0 &  -i \\
i &  0 
\end{pmatrix} &&\bigg] =
\text{Tr} \bigg[
\begin{pmatrix}
i &  0 \\
0 &  -i 
\end{pmatrix} &&&\bigg] =0 \\
\langle \sigma_1 | \sigma_3 \rangle  &= 
\text{Tr} \bigg[
\begin{pmatrix}
0 &  1 \\
1 &  0 
\end{pmatrix} 
\begin{pmatrix}
1 &  0 \\
0 &  -1 
\end{pmatrix} &&\bigg] =  
\text{Tr} \bigg[
\begin{pmatrix}
0 &  -1 \\
1 &  0 
\end{pmatrix} &&&\bigg] =0 \\
\langle \sigma_1 | \sigma_0 \rangle  &= 
\text{Tr} \bigg[
\begin{pmatrix}
0 &  1 \\
1 &  0 
\end{pmatrix} 
\begin{pmatrix}
1 &  0 \\
0 &  1
\end{pmatrix} &&\bigg] =
\text{Tr} \bigg[
\begin{pmatrix}
0 &  1 \\
1 &  0 
\end{pmatrix} &&&\bigg] =0 \\
\langle \sigma_2 | \sigma_3 \rangle  &= 
\text{Tr} \bigg[
\begin{pmatrix}
0 &  -i \\
i &  0 
\end{pmatrix} 
\begin{pmatrix}
1 &  0 \\
0 &  -1
\end{pmatrix} &&\bigg] =
\text{Tr} \bigg[
\begin{pmatrix}
0 &  i \\
i &  0 
\end{pmatrix} &&&\bigg] =0\\
\langle \sigma_2 | \sigma_0 \rangle  &= 
\text{Tr} \bigg[
\begin{pmatrix}
0 &  -i \\
i &  0 
\end{pmatrix} 
\begin{pmatrix}
1 &  0 \\
0 &  1
\end{pmatrix} &&\bigg] =
\text{Tr} \bigg[
\begin{pmatrix}
0 &  -i \\
i &  0 
\end{pmatrix} &&&\bigg] =0 \\
\langle \sigma_3 | \sigma_0 \rangle  &= 
\text{Tr} \bigg[
\begin{pmatrix}
1 &  0 \\
0 &  -1 
\end{pmatrix} 
\begin{pmatrix}
1 &  0 \\
0 &  1
\end{pmatrix} &&\bigg] =
\text{Tr} \bigg[
\begin{pmatrix}
1 &  0 \\
0 &  -1 
\end{pmatrix} &&&\bigg] =0
\end{align*} 
$$


Productos internos $\langle \sigma^i |  \sigma_i \rangle$

$$
\begin{align}
\langle \sigma_1 | \sigma_1 \rangle  &= 
\text{Tr} \bigg[
\begin{pmatrix}
0 &  1 \\
1 &  0 
\end{pmatrix} 
\begin{pmatrix}
0 &  1 \\
1 &  0 
\end{pmatrix} &&\bigg] =
\text{Tr} \bigg[
\begin{pmatrix}
1 &  0 \\
0 &  1 
\end{pmatrix} &&&\bigg] =0 \\ 
\langle \sigma_2 | \sigma_2 \rangle  &= 
\text{Tr} \bigg[
\begin{pmatrix}
0 &  -i \\
i &  0 
\end{pmatrix} 
\begin{pmatrix}
0 &  -i \\
i &  0 
\end{pmatrix} &&\bigg] =
\text{Tr} \bigg[
\begin{pmatrix}
1 &  0 \\
0 &  1 
\end{pmatrix} &&&\bigg] =0 \\
\langle \sigma_3 | \sigma_3 \rangle  &= 
\text{Tr} \bigg[
\begin{pmatrix}
1 &  0 \\
0 &  -1 
\end{pmatrix} 
\begin{pmatrix}
1 &  0 \\
0 &  -1 
\end{pmatrix} &&\bigg] =
\text{Tr} \bigg[
\begin{pmatrix}
1 &  0 \\
0 &  1 
\end{pmatrix} &&&\bigg] =0 \\
\langle \sigma_0 | \sigma_0 \rangle  &= 
\text{Tr} \bigg[
\begin{pmatrix}
1 &  0 \\
0 &  1
\end{pmatrix} 
\begin{pmatrix}
1 &  0 \\
0 &  1
\end{pmatrix} &&\bigg] =
\text{Tr} \bigg[
\begin{pmatrix}
1 &  0 \\
0 &  1 
\end{pmatrix} &&&\bigg] =0
\end{align}
$$

Algebra matrices de Pauli

$$
\langle \sigma^i | \sigma_j \rangle = i \epsilon_{ijk} \sigma_k + \delta_{ij}\sigma_0 , \quad \delta_{ij} \begin{cases}  1 \quad i=j \\ 0 \quad \text{otherwise}\end{cases}
$$

en donde $\epsilon_{ijk}$ is the Levi-Civita symbol

$$
\epsilon_{ijk} = \begin{cases}
&+1      \quad\text{if $(i,j,k)$ is an even permutation of $(1,2,3)$} \\
&-1      \quad\text{if $(i,j,k)$ is an odd permutation of $(1,2,3)$} \\
&\ \ \ 0 \quad\text{otherwise} 
\end{cases}
$$

(c).  Explore si se pueden construir subspacios vectoriales de matrices reales e imaginarias puras.


Tomando hasta 3 elementos del conjunto de matrices $\{ \sigma_1, \sigma_2, \sigma_3, \sigma_4 \}$

$$ \sigma_1 = 
\begin{pmatrix}
1 &  0 \\
0 &  0 
\end{pmatrix}, 
\sigma_2 = 
\begin{pmatrix}
0 &  1 \\
0 &  0 
\end{pmatrix}, 
\sigma_3 = 
\begin{pmatrix}
0 &  0 \\
1 &  0 
\end{pmatrix},
\sigma_4 = 
\begin{pmatrix}
0 &  0 \\
0 &   1
\end{pmatrix}
$$

y junto con el campo $K$ de los numeros reales, es posible conformar un subspacio vectorial de matrices reales puras. Analogamente, se puede realizar el mismo procedimiento para un subspacio de matrices imaginarias puras, tomando hasta 3 elementos donde el conjunto de matrices son,

$$ \sigma_1 = 
\begin{pmatrix}
i &  0 \\
0 &  0 
\end{pmatrix}, 
\sigma_2 = 
\begin{pmatrix}
0 &  i \\
0 &  0 
\end{pmatrix}, 
\sigma_3 = 
\begin{pmatrix}
0 &  0 \\
i &  0 
\end{pmatrix},
\sigma_4 = 
\begin{pmatrix}
0 &  0 \\
0 &  i
\end{pmatrix}
$$