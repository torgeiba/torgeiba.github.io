# Vectors and Tensors

Vectors and especially tensors can be a littlebit mysterious the first time you encounter them,
and it doesn't help that they are often introduced by giving some intuitive idea or analogy that isn't entirely precice, or even really correct.
So if you are trying to get a firm conceptual understanding of what they *are*, then it is better to ground all the intuition and examples
in a very formal and precise definition and build everything else on top of that.

In this post the goal is to give the *true* mathematical definitions of these concepts, show *how* to work with them, give some examples
and then give some references that I found useful when I was exploring these topics.

Since tensors builds on top of the concepts of vectors, we will start with vectors.

## Vectors

Some common ways of explaining what vectors are often include "A vector is like a little arrow (directed line segment)", "A vector is the difference of two points"
or "A vector is just a list (of numbers)".

These ways of thinking about vectors can be helpful when either reasoning about vectors in geometry or calculating with vectors in a computer program,
but they are not good at capturing the essense of makes a vector a vector, or serving as a formal definition. 
We would like to have a formal abstract and universal definition
that captures the core properties of vectors and underlies all possible concrete examples of vectors.

Before we proceed it is worth pointing out that the question of what a vector is, is already a bit misleading, since consider a single vector in isolation
does not make sense. They are always part of some *structure* or algebraic system, called a vector space.

So to give the "one true" definition of a vector, it is:

> A vector is an element of a vector space

Ok, so while correct, this definition is not particularly enlightening without first knowing what a vector space is.
When we now define a vector space we can then start understand vectors to be the objects that together comprise a vector space.

So without further ado, here is the definition of a vector space:

> A vector space over a field $F$ is a set $V$, along with two binary operations, called vector addition and scalar multiplication that act on the elements of $V$,
> called vectors, and must satisfy the following eight axioms:
> 1. Associativity of vector addition
> 2. Commutativity of vector addition
> 3. Existence of an identity element of vector addition
> 4. Existence of an inverse element of vector addition
> 5. Compatability of vector addition with field multiplication
> 6. Existence of an identity element of scalar multiplication
> 7. Distrubutivity of scalar multiplication with respect to vector addition
> 8. Distrubutivity of scalar multiplication with respect to field addition


