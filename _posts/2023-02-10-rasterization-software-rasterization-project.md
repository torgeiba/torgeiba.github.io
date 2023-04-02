# Rasterization: Software Rasterization Pipeline

![A painting of a rasterization pipeline by DALL-E](/assets/images/DALL-E_2023-02-10_22.00.36_-_An_artful_interpretation_of_a_technical_diagram_graph_of_a_computer_graphics_rasterization_pipeline_algorithm,_on_a_dark_background_with_neon_colored_.png)
> A painting of a rasterization pipeline by DALL-E 2

This post will simply be an outline of my plans for my CPU software rasterization project.

## Scope

This post will primarily concern just the rasterizer stage of a triangle-rasterizer software rendering pipeline.
That is to say, it will mostly not discuss vertex shading or pixel shading, nor any other stage before or after rasterization.
However, in the rasterization I also plan on including several sub-stages such as frustum culling, binning, occlusion culling, hierarchical Z-buffering, and so on.
Some closely related systems will also be described such as the instancing and batched drawing approach.

## Features

For perfomance reasons I will attempt to make as good use of SIMD, multithreading and cache efficiency as possible.
This will impact several aspects of the design of the rasterizer.
As an experiment I plan on writing a small library to use 16 element wide SIMD operations for integer single precision floating point data,
similar to AVX-512 but implemented using AVX and AVX2, as well as some FMA instructions.
The expected advantage of this is that each operand will correspond to an entire cache line, making full use of the cache capacity,
and simplifying the task of making sure data is contiguous, not straddling cache line boundaries, and preventing false sharing between threads.
It should also make it relatively straight forward to estimate the number of cache lines used in various parts of the code. 
The cache line count could be used as a heuristic, or parameter, for tuning data batch and block sizes during development.

## Sub-stages

- Frustum culling
- Backface culling
- Triangle setup ( some data may be re-used from the culling steps )
- Triangle binning (low-res conservative rasterization)
- Occlusion culling
- Rasterization and depth testing

## Input and output

The input to the procedure will be a pointer to a buffer of triangle vertex positions, a pointer to a buffer of triangle vertex indices,
a triangle count, and triange index offset. The triangle input offset will be used to handle instancing and batched rendering.
The output will be a Z-buffer to that can be used by the next shading steps, material calculation and so on, and a visibility buffer, which is simply a buffer, or image,
of triangle indices. The indices will also have the instance index baked into them (using the triangle index offset), so the index will have to be decoded to find the actual triangle index for the mesh.


## Frustum culling details

There are some notes on frustum culling on the [ryg blog here](https://fgiesen.wordpress.com/2010/10/17/view-frustum-culling/)

## Backface culling details

When we have access to the normal, or equivalent information, we can simply backface cull triangles by computing a single dot product by the view direction and the
triangle normal.

## Triangle setup details

For computing triangle overlap one will need to compute the triangle edge functions. It is possible to save some work by making sure to only compute the parts
that are invariant over the triangle just once. 

## Triangle binning details

Triangle binning basically amounts to performing overestimated conservative rasterization, rasterizing triangles over tiles instead of pixels.
A pixel is usually rasterized by sampling a single point, but a tile is a screen space axis aligned rectangular region.
The basic sampling step for this is essentially a rectangle-triangle overlap test. This is essentially overestimated conservative rasterization.
In the 2D case it is possible to determine overlap by testing whether the tile is fully outside one of the triangle edges or the tile is fully outside the
triangle bounding box. In the 3D case we do not always have appropriate bounding boxes for the triangles.
Instead it is possible to instead use the test of whether the tile is fully outside one of the triangle edges or the triangle is fully outside one of the tile edges.
This can be made efficient for a grid of tiles (where many edges are shared), and generalized to 3D and clipless rasterization where the edges become planes for both triangles and tiles.

The test is a series of dot products. The tile edges are axis aligned, so it is possible to omit one coordinate. For 2D this becomes a one-coordinate test.
For 3D it becomes a two-coordinate test. The vertical tile edges have normals with zero $y$ (vertical) coordinate. 
Since we do not care about the length of the normal, just the sign of the dot products, we can just rotate the vector from the camera to where
the edge crosses the screen coordinate axes by a quarter turn. 
Conceptually it is just an optimization of taking the cross product of two adjacent corner positions of the tile.

### Acceptance and rejection tests



## Occlusion culling details

For occlusion culling it makes sense to use a hierarchical depth buffer using conservative depth for all but the highest resolution level.
If we at any level can find a set of tiles that completely conver the object to be drawn, e.g a triangle or bounding box, and all the depth values in those tiles
have a depth value that is nearer than the nearest point of that object, then we can safely cull it.
To find the nearest depth value of a triangle one can use rasterization, or one can compute the nearest depth of the camera space bounding box without needing to compute the other values.

## Rasterization and depth testing details



## Visibility buffer details

every triangle index is an unsigned 32-bit integer value that represents the triangle index of the currently rendered mesh plus a triangle index offset given as a paramter to the rasterization function.

## Implementation details



## Test cases

### Triangle rendering test cases
- Crossing frustum clipping planes
- Trapped in a box ( all pixels covered )
- Ground planes (large triangles with perfectly vertical normals)
- Depth order ( overlapping triangles behind eachother rendered in various orders )
- Behind camera
- Behind "near plane"
- Backfacing triangles
- Intersecting triangles
- Crossing camera view direction plane
- Two triangles ( fullscreen )
- One triangle  ( fullscreen )
- Triangle orientations: Side/edge on triangle


## Footnotes and references:

[Visibility Buffer Rendering with Material Graphs, by John Hable](http://filmicworlds.com/blog/visibility-buffer-rendering-with-material-graphs/)

[Rasterization on Larrabee, by Michael Abrash](https://www.cs.cmu.edu/afs/cs/academic/class/15869-f11/www/readings/abrash09_lrbrast.pdf)
