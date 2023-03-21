# Notes on the Cross Product

The cross product is often given in one of two ways: Either geometrically, or as a formula given in coordinates.

## The geometric description

The cross product of two vectors in 3D Euclidean space results in a new vector that is orthogonal to both the input vectors,
points in the direction given by the right hand rule (by convention), and has a length equal to the area of the paralellogram spanned by the two vectors.

## The coordinate formula description

The cross product $c = a \times b$ of $a = \(a_x, a_y, a_z\)$ and $b = \(b_x, b_y, b_z\)$ is given by the formula
$c = \( a_y b_z - a_z b_y, -a_x b_z + a_z b_x,  a_x b_y - a_y b_x \)$


## An algebraic description

The cross product is less often introduced with an algebraic description. The algebraic properties are usually presented after giving the geometric motivation,
but it can be fully determined based on it's algebraic properties.

The cross product of two vectors $a$ and $b$ is bilinear in it's arguments and anti-commutative, that is, $a \times b = - b \times a$.
Bilinearity means that it is linear separately in each of its arguments:

Additivity: $(a + b) \times c = a \times c + b \times c$ , $a \times (b + c) = a \times b + a \times c$ 

and homogeniety: $(xa) \times b = x(a \times b) = a \times (xb)$,

Consider again the cross product $c = a \times b$. Let's expand $a$ and $b$ out in terms of their coordinates in an orthonormal basis $e_1, e_2, e_3$.

$a = {\sum_{i=1}^3 a_i e_i}$

and

$b = \sum_{j=1}^3 b_j e_j$

Then by using the linearity of the cross product we get:
$a \times b = \sum_{i=1}^3 \sum_{j=1}^3 (a_i e_i) \times (b_j e_j)  = \sum_{i=1}^3 \sum_{j=1}^3 (a_i b_j) \(e_i \times e_j)$

Then we use: $e_1 \times e_2 = e_3$, $e_2 \times e_3 = e_1$ and $e_3 \times e_1 = e_2$ and $e_i \times e_j = - e_j \times e_i$

and get

$a \times b =  (a_y b_z - a_z b_y) (e_2 \times e_3) + (a_x b_z - a_z b_x)(e_1 \times e_3) + (a_x b_y - a_y b_x)(e_1 \times e_2)$

$a \times b =  (a_y b_z - a_z b_y) e_1 - (a_x b_z - a_z b_x) e_2 + (a_x b_y - a_y b_x) e_3$

Which matches the coordinate definition of the cross product. Notice that since we had $e_1 \times e_3$ we had to use anti-commutativity to flip the order,
from which we pick up a negative sign, to obtain $e_2$.



