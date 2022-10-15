# Computing Analytic Disk-Rectangle Intersection Area

<iframe width="640" height="360" frameborder="0" src="https://www.shadertoy.com/embed/7lVBWc?gui=true&t=10&paused=true&muted=false" allowfullscreen></iframe>

<iframe width="640" height="360" frameborder="0" src="https://www.shadertoy.com/embed/NtyBRc?gui=true&t=10&paused=true&muted=false" allowfullscreen></iframe>

<iframe width="640" height="360" frameborder="0" src="https://www.shadertoy.com/embed/stKfDc?gui=true&t=10&paused=true&muted=false" allowfullscreen></iframe>

<iframe width="640" height="360" frameborder="0" src="https://www.shadertoy.com/embed/NtGBWt?gui=true&t=10&paused=true&muted=false" allowfullscreen></iframe>

<iframe width="640" height="360" frameborder="0" src="https://www.shadertoy.com/embed/ftGfWt?gui=true&t=10&paused=true&muted=false" allowfullscreen></iframe>

<iframe width="640" height="360" frameborder="0" src="https://www.shadertoy.com/embed/flyBDt?gui=true&t=10&paused=true&muted=false" allowfullscreen></iframe>

<iframe width="640" height="360" frameborder="0" src="https://www.shadertoy.com/embed/flGfDt?gui=true&t=10&paused=true&muted=false" allowfullscreen></iframe>

<iframe width="640" height="360" frameborder="0" src="https://www.shadertoy.com/embed/ftyfDt?gui=true&t=10&paused=true&muted=false" allowfullscreen></iframe>

<iframe width="640" height="360" frameborder="0" src="https://www.shadertoy.com/embed/NlyfDt?gui=true&t=10&paused=true&muted=false" allowfullscreen></iframe>

<iframe width="640" height="360" frameborder="0" src="https://www.shadertoy.com/embed/ftGBWd?gui=true&t=10&paused=true&muted=false" allowfullscreen></iframe>

<iframe width="640" height="360" frameborder="0" src="https://www.shadertoy.com/embed/ftGfWd?gui=true&t=10&paused=true&muted=false" allowfullscreen></iframe>

<iframe width="640" height="360" frameborder="0" src="https://www.shadertoy.com/embed/ftGBDd?gui=true&t=10&paused=true&muted=false" allowfullscreen></iframe>

## Alternative approaches

### Integrals


The height of the unit hemicircle from minus one to one can be given as $y = \sqrt{1-x^2}$.

Consider also taking a slice through the unit disk and considering the indicator function of the disk, i.e a function that is equal to one inside the disk
and zero elsewhere.
The result is a box function, which is discontinuous, but which it is still possible to take the integral of. 
The integral wil be a piecewise linear function. 

<img width="260" alt="box_function_integral" src="https://user-images.githubusercontent.com/5385533/196010869-f4f47695-0e9e-4532-91cc-03d363ca36d6.png">
