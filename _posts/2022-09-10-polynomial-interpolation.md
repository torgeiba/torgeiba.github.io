# Polynomial interpolation

## Connect the dots

How do you get a straight line through two points? You could just represent the line, or line segment, between points $A$ and $B$ by the pair
$(A, B)$, which can be ordered or unordered based on whether you care about the direction or not. This abstracts away the geometry
and only retains the connectedness. So this is the way it would be represented in topology or in graphs, as it is agnostic to the path taken between the points.
It is a non-parametric approach which can be thought of as having omitted information about the travel time.

But what if we want to find the points on the path between the two points? We could design a function, $g$, that can answer whether a given point is on the path or not.
The function $g(X) = 0$ if we are on the path, and nonzero otherwise. For example, let's say we represent the points by vectors in a normed vector space.
Then we can use the function

$$g(X) = ||X - A|| + ||X - B|| - ||B - A||$$

This function makes use of the triangle identity, and is equal to zero when the three points $X$, $A$ and $B$ are collinear.
Therefore the function indicates whether a point is on the straight line that goes through $A$ and $B$.
If we also want to indicate whether $X$ is on the line segment between the points, and not outside, we must also require that

$$||X - A|| \le  ||B - A||$$

and

$$||X - B|| \le  ||B - A||$$

If we have a dot product then we could also have used it to find the projection $p(X)$ and rejection $r(X)$ of the point $X$ to and from the line, where

$$p(X)  =  \frac{(X - A) \cdot (B - A)}{(B - A) \cdot (B - A)} (B - A) + A$$

and 

$$r(X) = X - p(X)$$

These are vector valued functions, and a function $g$ that satisfies out requirements can then be defined as

$$g(X) = ||r(X)||$$

## Parametric lines and curves

The previous examples were abstract topological, and implicit non-parametric, respectively.
We can also represent the line using an explicit parametric approach. In this case, we can define a function that takes a parameter $t, which is often conceptualized as the travel time, and gives an explicit point on the line. We can identify this point $X$ as a function of $t$ with

$$X(t) = (B - A) t + A$$

This function returns $A$ when $t = 0$, $B$ when $t = 1$ and some point in the line segment when $t$ is in the interval $[0, 1]$



