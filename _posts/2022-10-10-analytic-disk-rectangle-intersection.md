# Computing Analytic Disk-Rectangle Intersection Area

The problem considered here is that of finding the area of a two dimensional region that is the intersection of a disk, i.e. a filled circle, and a filled rectangle.
The motivation for this problem was the use case of computing the exact (up to numerical or implementation errors) coverage of a disk in a pixel, in order
to find the correct color value for the pixel when rendering the disk. This could also be used for circle rendering by computing the converage of an annulus,
simply by computing the area of two concentric disks and subtracting the smaller one from the larger one. Of course, in order to render more than one of these shapes
correctly one would have to compute the mutual occlusion of these shapes as well, which complicates the problem further, so I'll only consider rendering a single shape here, and focus on the problem of computing the analytical area of rectangle-disk intersection. The rectangle is assumed to be axis aligned, for simplicity,
but it is possible to add a step between step 1 and 2 to rotate the coordinate system such that the rectangle becomes axis aligned without affecting the result.

The algorithm is as follows:
Input: An axis aligned rectangle (box) of arbitrary size and position, a disk of arbitrary radius and position.
Output: The area of the intersecting area

1. Translate and scale the coordinates such that the disk becomes a unit disk centered at the origin
2. Clip the rectangle against the X and Y axes to obtain four smaller rectangles, one for each XY quadrant
3. For each of the four quadrant rectangles:
  1. Flip the rectangle such that it lands in the top right quadrant, i.e the positive X and positive Y quadrant.
  2. Determine whether the rectangle intersects the unit circle
    - If the rectangle does not intersect the unit circle, then it is either fully inside or fully outside the unit disk
      - If the rectangle is fully outside, then we can skip to the next rectangle
      - Otherwise we compute the area of the rectangle and add it to the total area
    - Otherwise the rectangle intersects and we proceed with the next steps
  3. Find the intersection points of the rectangle and the unit circle.
    - The rectangle and circle must intersect in exactly two points
  4. Find the rectangle that tightly bounds the two intersection points
  5. Compute the area of the [circular segment](https://en.wikipedia.org/wiki/Circular_segment) given by the two points
  6. Find the area of the triangle given by the three vertices at the bottom left of the rectangle bounding the intersection points, and the intersection points themselves
  7. Compute the interection area of the quadrant rectangle as the area of the full rectangle, subtract the area of the rectangle bounding the two intersection points, add back the area of the cap and the triangle and subtract the area of the quadrant rectangle that is outside the circle.
  8. Add the intersection area to the total area and continue with the next quadrant rectangle

## Subproblem 1: Translate and scale to unit circle

<iframe width="640" height="360" frameborder="0" src="https://www.shadertoy.com/embed/7lVBWc?gui=true&t=10&paused=true&muted=false" allowfullscreen></iframe>

## Subproblem 2: Clip rectangle against X and Y coordinate axes

<iframe width="640" height="360" frameborder="0" src="https://www.shadertoy.com/embed/stKfDc?gui=true&t=10&paused=true&muted=false" allowfullscreen></iframe>

## Subproblem 3: Flip all rectangles to top right quadrant

<iframe width="640" height="360" frameborder="0" src="https://www.shadertoy.com/embed/NtGBWt?gui=true&t=10&paused=true&muted=false" allowfullscreen></iframe>

## Subproblem 4: Detect rectangles intersecting unit circle

Note that the implemented version only works if the rectangle is fully in the top right quadrant!
The rectangle must be clipped against the axes.

<iframe width="640" height="360" frameborder="0" src="https://www.shadertoy.com/embed/ftGfWt?gui=true&t=10&paused=true&muted=false" allowfullscreen></iframe>

## Subproblem 5: Find intersection points of circle and rectangle

<iframe width="640" height="360" frameborder="0" src="https://www.shadertoy.com/embed/flyBDt?gui=true&t=10&paused=true&muted=false" allowfullscreen></iframe>

## Subproblem 6: Clip rectangle to intersection tightly bound points

<iframe width="640" height="360" frameborder="0" src="https://www.shadertoy.com/embed/flGfDt?gui=true&t=10&paused=true&muted=false" allowfullscreen></iframe>

## Subproblem 7: Compute area of cap and triangle

<iframe width="640" height="360" frameborder="0" src="https://www.shadertoy.com/embed/ftyfDt?gui=true&t=10&paused=true&muted=false" allowfullscreen></iframe>

## Subproblem 8: Compute remaining area inside triangle

<iframe width="640" height="360" frameborder="0" src="https://www.shadertoy.com/embed/NlyfDt?gui=true&t=10&paused=true&muted=false" allowfullscreen></iframe>

## Subproblem 9: Combine the area of the remaining rectangle part with the triangle and cap

<iframe width="640" height="360" frameborder="0" src="https://www.shadertoy.com/embed/ftGBWd?gui=true&t=10&paused=true&muted=false" allowfullscreen></iframe>

## Subproblem 10: Combine the area of all four quadrant pieces of the rectangle

<iframe width="640" height="360" frameborder="0" src="https://www.shadertoy.com/embed/ftGfWd?gui=true&t=10&paused=true&muted=false" allowfullscreen></iframe>

## Subproblem 10b: Another way to visualize the result in 10

<iframe width="640" height="360" frameborder="0" src="https://www.shadertoy.com/embed/ftGBDd?gui=true&t=10&paused=true&muted=false" allowfullscreen></iframe>

## The final result

<iframe width="640" height="360" frameborder="0" src="https://www.shadertoy.com/embed/DssGzr?gui=true&t=10&paused=true&muted=false" allowfullscreen></iframe>

<iframe width="640" height="360" frameborder="0" src="https://www.shadertoy.com/embed/dds3zn?gui=true&t=10&paused=true&muted=false" allowfullscreen></iframe>

## Alternative approaches

### Integrals


The height of the unit hemicircle from minus one to one can be given as $y = \sqrt{1-x^2}$.

Consider also taking a slice through the unit disk and considering the indicator function of the disk, i.e a function that is equal to one inside the disk
and zero elsewhere.
The result is a box function, which is discontinuous, but which it is still possible to take the integral of. 
The integral wil be a piecewise linear function. 

<img width="260" alt="box_function_integral" src="https://user-images.githubusercontent.com/5385533/196010869-f4f47695-0e9e-4532-91cc-03d363ca36d6.png">

Using this along with taking appropriate limits of integration and using the symmetry of the sphere, it should be possible to derive an expression for the area of the intersection fo the disc and rectangle.

<img width="230" alt="image" src="https://user-images.githubusercontent.com/5385533/196011633-b4e59402-8ce4-4f9f-a0a6-b1f1480e2d60.png">
