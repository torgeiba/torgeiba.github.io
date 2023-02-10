# Rasterization: Software Rasterization Pipeline

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
a triangle count, the instance index and instance transform.
The output will be a Z-buffer to that can be used by the next shading steps, material calculation and so on, and a visibility buffer, which is simply a buffer, or image,
of triangle indices. The indices will also have the instance index baked into them, so the index will have to be decoded to find the actual triangle index for the mesh.


## Frustum culling details

## Backface culling details

## Triangle setup details

## Triangle binning details

## Occlusion culling details

## Rasterization and depth testing details

## Visibility buffer details

## Implementation details

## Test cases


