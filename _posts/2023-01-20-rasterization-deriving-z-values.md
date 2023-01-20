# Rasterization: Deriving Z values

For determining the values in the Z buffer one needs an algorithm to compute the z value for each pixel in a triangle.
In the following we assume that we operate in camera space. That is, the camera is placed at the origin and looking along the Z-axis in this coordinate system.
Further, we are gived the coordinates of the pixels we are rendering in this camera space. Each pixel corresponds to a ray from the camera
and so has a range of coordinate values associated with it instead of just a fixed value. We also assume that the near plane, or image plane, of the camera is located
at a unit length offset along the Z-axis from the camera position. We also know the normal of the triangle, and at least one point on the plane the triangle resides in.
This is arbitrary but could for example be a vertex or the centroid. We'll just assume it's the first vertex.

To find the Z-coordinate of the point where the pixel ray intersects the triangle plane we first define a useful function.
The function will take a position or a vector in camera space and return a scalar.
The function is uniquely defined as the function that is zero in the camera position,
increases linearly along the normal direction,
and is constant in all directions orthogonal to the normal direction.
Then that function will always give the same value for each point on the triangle plane.
Since each intersection point is by definition on the triangle plane, and we know at least one point on the plane,
we can figure out how much we need to scale the position vector of the pixel on the near plane by in order to intersect the triangle plane.
The function in question is given by the dot product by the triangle normal vector.

We have:
The position on the near plane corresponding to a pixel: $d$
The triangle normal: $N$
The triangle normal: $N$
A point on the triangle plane $P$
An unknown scaling value $t$

We want to find the $z$ coordinate of $td$.
We know that $P \cdot N = td \cdot N$
Solving for the scaling $t$ gives 
$$ t  = \fract{P \cdot N}{d \cdot N} $$
The case where the denominator $d \cdot N$ is equal to zero corresponds to when the ray lies in the plane, and can therefore be excluded in an earlier stage of the system.
The Z-value can then be found by computing $d_z t$, but since we assumed that $d_z$ was plus or minus one unit, we just get either $-t$ or $t$ depending on our choice.
