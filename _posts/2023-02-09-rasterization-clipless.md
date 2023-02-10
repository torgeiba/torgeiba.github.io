# Rasterization: Triangle Rasterization Without Clipping

The usual way that triangle rasterization works is that there is a clipping step and a perspective divide step.
The primary reason for the clipping step is to ensure that the perspective divide gives the correct projection on the screen even when the original
one or two of the triangle vertices are behind the camera. In that case, a simple perspective divide by the depth coordinate (and projection onto the image plane) will 
yield the wrong result with regard to what the next steps in the rasterizer expects. In the projective setting, i.e using homogeneous coordinates, the zero depth coordinate
corresponds to points at infinity, while points behind the camera can be interpreted as points that have gone past the point at infinity, wrapped around, and appeared again
from the other side. Therefore there will be a disconnect between considering the vertices of the triangle in isolation as points, and viewing them as endpoints of line segments or triangles.

If triangles are also clipped against the top, bottom and sides of the view frustum, then all new triangle vertices (of visible triangles)
will correctly land on the screen within the screen bounds.

The perspective divide and projection onto the image plane is done so that we can find the pixel coordinates of the vertices on the screen and rasterize the triangle in 2D instead of 3D.

The downside of performing explicit polygon clipping of triangles is that it can be a computationally expensive operation and be somewhat tricky to implement.
In some cases a triangle will be clipped to produce two visible triangles on screen, which complicates the rasterization pipeline.

It is possible to avoid explicit polygon clipping altogether by using the fact that a triangle covers a pixel sample point if, and only if, the view-direction correspong to that
pixel sample point is a member of the [convex cone](https://en.wikipedia.org/wiki/Convex_cone) spanned by the vectors pointing from the camera position, the origin in camera space, to each of the verices of the triangle.
The convex cone of a set of vectors contains all vectors that can be expressed as a linear combination of the spanning vectors with the restriction that the coefficients must be non-negative.

The test to check the membership of the view direction in the convex cone can be performed by performing a dot product with normals of each of the faces of the
tetrahedra formed by the camera position and the triangle vertices, which intersect the origin. That is, all faces except the triangle itself.
If all the dot products are positive, then the view-direction is a member of the convex cone.
The normals of these planes can be found by taking the cross product of each of the ordered pairs of the vectors spanning the convex cone.
The cross and dot products together amounts to the [triple-product](https://en.wikipedia.org/wiki/Triple_product). It can also equivalently be computed via determinants.

The operation of computing cross and dot products, or triple products, is essentially the same as computing the matrix-vector product of the [inverse of the 3x3 matrix](https://en.wikipedia.org/wiki/Invertible_matrix#Inversion_of_3_×_3_matrices)
consisting of the spanning vectors with the view-direction, up to a scaling factor. Note the connection between the explicit form of the 3x3 matrix inverse in terms of cross products and the determinant and [Cramers rule](https://en.wikipedia.org/wiki/Cramer%27s_rule). The scaling factor being the full determinant of the matrix of spanning vectors.

