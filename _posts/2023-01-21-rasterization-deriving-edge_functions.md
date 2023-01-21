# Rasterization: Deriving Triangle Edge functions

Edge functions in the context of triange rasterization are functions that are used to determine which side of a triangle edge a pixel lies on.
Conceptually, this can be calculated easily by using the dot product of the inwards facing normal of the edge and an offset vector from a point on the edge to the pixel position.
The challenge lies in efficiently determining the projected edge on the screen from the 3D triangle edges and obtaining the inwards facing normal from it.

The projected edge on the screen is the intersection of the near plane with the new triangle formed by the two endpoints of the original triangle edge and the camera position.
The normal of this plane is the cross product of the position vectors of the endpoint vertices $V_0 \times V_1$.
The screenspace edge normal can then be found by projecting this triangle normal to lie in the image plane.
An alternative approach is to use perspective projection on the vertices by dividing them by their Z-component, causing all the vertices to lie in the image plane.
The projected triangle edge normals can then be found by performing a simple counter clockwise 2D rotation, given by $x' = -y$ and $y' = x$.

For a pixel with position vector $P$, a triangle with vertices $V_i = (x_i, y_i, z_i)$, 
the 2D counter clockwise rotation matrix $\textbf{R}$, the edge function from the vertex $V_0$ to $V_1$ can be computed by:

$$e(P) = (P - V_0) \cdot \textbf{R} \left( \frac{V_1}{z_1} - \frac{V_0}{z_0} \right) $$

Notice that the reciprocal Z-values appear again, like in the previous post, but this time, it's only the Z-values of the vertices themselves, not the ones that go into the Z-buffer after having been interpolated. Mathematically  we could also have scaled the function by $z_0 z_1$ to get rid of the divisions, since we only care about the sign of the edge function.

The edge functions are related to barycentric coordinates, but since the barycentric coordinates are slightly more expenisve to compute, we will prefer the edge function where the barycentric coordinates are not needed.
