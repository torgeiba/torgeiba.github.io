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
$||X - A|| \le  ||B - A||$ and $||X - B|| \le  ||B - A||$ 

