# Computing Analytic Disk-Rectangle Intersection Area

## Subproblem 1 Translate and scale to unit circle

<iframe width="640" height="360" frameborder="0" src="https://www.shadertoy.com/embed/7lVBWc?gui=true&t=10&paused=true&muted=false" allowfullscreen></iframe>

## Subproblem 2: Clip rect against X and Y coordinate axes

<iframe width="640" height="360" frameborder="0" src="https://www.shadertoy.com/embed/NtyBRc?gui=true&t=10&paused=true&muted=false" allowfullscreen></iframe>

## Subproblem 3: Flip all rectangles to top right quadrant

<iframe width="640" height="360" frameborder="0" src="https://www.shadertoy.com/embed/stKfDc?gui=true&t=10&paused=true&muted=false" allowfullscreen></iframe>

## Subproblem 4: Detect rectangles intersecting unit circle (not disk)

Note that the implemented version only works if the rectangle is fully in the top right quadrant!
The rectangle must be clipped against the axes.

<iframe width="640" height="360" frameborder="0" src="https://www.shadertoy.com/embed/NtGBWt?gui=true&t=10&paused=true&muted=false" allowfullscreen></iframe>

## Subproblem 5: Find intersection points of circle and rectangle

<iframe width="640" height="360" frameborder="0" src="https://www.shadertoy.com/embed/ftGfWt?gui=true&t=10&paused=true&muted=false" allowfullscreen></iframe>

## Subproblem 6: Clip rectangle to intersection points

<iframe width="640" height="360" frameborder="0" src="https://www.shadertoy.com/embed/flyBDt?gui=true&t=10&paused=true&muted=false" allowfullscreen></iframe>

## Subproblem 7: Compute area of cap and triangle

<iframe width="640" height="360" frameborder="0" src="https://www.shadertoy.com/embed/flGfDt?gui=true&t=10&paused=true&muted=false" allowfullscreen></iframe>


## Subproblem 8: Compute remaining area inside triangle

<iframe width="640" height="360" frameborder="0" src="https://www.shadertoy.com/embed/ftyfDt?gui=true&t=10&paused=true&muted=false" allowfullscreen></iframe>

## Subproblem 9: Combine the area of the remaining rectangle part with the triangle and cap

<iframe width="640" height="360" frameborder="0" src="https://www.shadertoy.com/embed/NlyfDt?gui=true&t=10&paused=true&muted=false" allowfullscreen></iframe>

## Subproblem 10: Combine the area of all four quadrant pieces of the rectangle

<iframe width="640" height="360" frameborder="0" src="https://www.shadertoy.com/embed/ftGBWd?gui=true&t=10&paused=true&muted=false" allowfullscreen></iframe>

## Subproblem 10: Combine the area of all four quadrant pieces of the rectangle

<iframe width="640" height="360" frameborder="0" src="https://www.shadertoy.com/embed/ftGfWd?gui=true&t=10&paused=true&muted=false" allowfullscreen></iframe>

## Subproblem 10b: Another way to visualize the result in 10

<iframe width="640" height="360" frameborder="0" src="https://www.shadertoy.com/embed/ftGBDd?gui=true&t=10&paused=true&muted=false" allowfullscreen></iframe>

## The final result

<iframe width="640" height="360" frameborder="0" src="https://www.shadertoy.com/embed/DssGzr?gui=true&t=10&paused=true&muted=false" allowfullscreen></iframe>

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
