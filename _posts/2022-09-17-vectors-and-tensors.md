# Vectors and Tensors

![A painting of a vector space by DALL-E](/assets/images/DALL-E_2022-09-18_01.00.39-a_colorful_abstract_digital_art_painting_of_a_vector_space_with_lines_grids.png)
> A painting of an abstract vector space by DALL-E

## Motivation

Vectors and especially tensors can be a little bit mysterious the first time you encounter them,
and it doesn't help that they are often introduced by giving some intuitive idea or analogy that isn't entirely precice, or even really correct.
So if you are trying to get a firm conceptual understanding of what they *are*, then it is better to ground all the intuition and examples
in a very formal and precise definition and build everything else on top of that.

In this post the goal is to give the *true* mathematical definitions of these concepts, show *how* to work with them, give some examples
and then give some references that I found useful when I was exploring these topics.

Vectors and tensors are *the* central objects in vector and tensor algebra / linear and multilinear algebra.
Since linear algebra is one of the most well studied fields within all of mathematics, there is a large body of useful theorems
that immediately becomes available once something is set identified as having a vector-type structure,
especially if there are also some natural ways to define inner products and such.
By using abstract definitions we broaden the applicability of those results as much as possible.

Since tensors builds on top of the concepts of vectors, we will start with vectors.

## Vectors

![Another painting of a vector space by DALL-E](/assets/images/DALL-E2022-09-1801.02.57-acolorfulabstractdigitalartpaintingofavectorspacewithlinesgrids.png)

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

> A vector space over a field $F$ is a set $V$, along with two binary operations, which are functions from $V \times V$ to $V$,
> called vector addition and scalar multiplication that act on the elements of $V$,
> called vectors, and must satisfy the following eight axioms:
> 1. Associativity of vector addition
> 2. Commutativity of vector addition
> 3. Existence of an identity element of vector addition
> 4. Existence of inverse elements of vector addition
> 5. Compatability of vector addition with field multiplication
> 6. Existence of an identity element of scalar multiplication
> 7. Distrubutivity of scalar multiplication with respect to vector addition
> 8. Distrubutivity of scalar multiplication with respect to field addition

I'll give a brief informal explanation of the definition and axioms, and then some formal statements.

I won't give a detailed definition of a field here, but you can either refer to the definition on wikipedia,
or just think of it as any number system that satisfies the algebraic rules of elementary algebra with the operations of addition, subtraction, multiplication and division. Examples include the rational, real and complex numbers.

- Associativity is the property that the operation is invariant to the partitioning of the expression into binary operations.
- Commutativity is the property that the operation is symmetric in its arguments
- Distributivity of one operaton over the over is the property that applying the operation to each of the arguments of the second operation is the same as
applying that same operation to the result instead.
- An identity element for an operation is an element that leaves the other operand unchanged
- Inverse elements for an operation is an element that gives the identity element when applied to the element to which it is the inverse.

It is useful to make some observations about what is *not* included in the definition of a vector space.
Namely, it does not contain any references to lists, dimension or indices,
to basis vectors or coordinates. It also does not mention scalar (dot), inner- or cross products, norms, nor any vector product or division.
Neither geometry or physics is mentioned or referred to, vectors are not described as arrows or directed line segments.
There is also no mention on linear dependence, linear combinations or spans, but those are rather constructions that are built on top of the definition of a vector space.
There is not mention of row or column vectors, and no transpose, just vectors.

### Formal expressions

For the following formal expressions, we will use the symbol $+$ for *vector addition*, $*$ for scalar multiplication,
$u, v, w$ for vectors from $V$ and $a, b, c$ for scalars from $F$

The axioms can then be given as

> 1. $(u + v) + w = u + (v + w)$
> 2. $u + v = v + u$
> 3. There is a vector $0 \in V$ such that $v + 0 = v$
> 4. There is a vector $-v \in V$ for every $v \in V$ such that $v + (-v) = 0$
> 5. $(ab) * v = a * (b * v)$
> 6. $I * v = v$, where $I$ is the multiplicative identity of $F$ (usually denoted by just $1$) 
> 7. $a * (u + v) = a * u + a * v$
> 8. $(a + b) * v = a * v + b * v$

### An aside: Closure and linear subspaces

It is important to keep in mind that the two operations that are part of the definition of vector spaces both take vectors from the space as input and
output a vector *in the same space*. It is possible that a subset of a vector space is also a vector space with the same operations if applying those operations
to the vectors in the subspace always maps back to vector in the subspace. 
We say that the linear subspace is *closed* under the operations of vector addition and scalar multiplication.
These subspaces can exist even if they do not contain all the vectors of the superset. 
We call such a set a linear subspace, and they are vector spaces in their own right.
All vector spaces are linear subspaces of themselves since they are subsets of themselves and closed under the operations
The closure property is used in the definition of linear subspaces.

### Examples of vector spaces

- "Ordinary" numbers
- Directed line segments as vectors
- Polynomials 
- Functions ( infinite dimensional)
- Arrays of numbers with vector operations
- Matrices
- Quaternions

### Linear maps and Linearity

The operations that are used in the definition of vectorspaces are exactly the ones used in the definition of linearity

- Additivity: $f(x + y) = f(x) + f(y)$
- Homogeniety of degree 1: $f(\alpha x) = \alpha f(x)$ for all $\alpha$

### Dimensionality, bases, linear dependence and spans



### Dual vector spaces

The dual vector space of a vector space is the vector space consisting of *all* linear functions from $V$ to $F$.
The dual basis is a basis for the dual space with has the property that the dual basis vectors evaluated with the primal basis vectors
as arguments gives the Kronecker delta.
That is for basis vectors $e_i$ and dual basis vectors $e^*_j$ we have

$$e^*_j ( e_i ) = \delta_ij$$

## Tensors

![A painting of a tensor space by DALL-E](/assets/images/DALL-E2022-09-1801.08.40-avividabstractdigitalartpaintingofamathematicaltensorproductspacewithdepthandfogaroundareasegmentsdualityvolumesrotationsandpro.png)

### Bilinearity and multilinearity

Bilinearity is the property that a function is linear in each of its two arguments *separately*.

That is, a functions $f$ is bilinear if

$$f(a * u + v, w) = a * f(u, w) + f(v, w)$$

and

$$f(u, a * v + w) = a * f(u, v) + f(u, w)$$

Some examples of bilinear operators include regular multiplication of numbers, the dot product and the cross product.

### The tensor product of vector spaces

As with vectors, a good way to define tensors is as elements of tensor products of vector spaces.
But again, that begs the question what the definition of tensor products of vector spaces is.
Some care must be taken, however, because while tensor products of vectors are fairly straight forward to define, 
*not all* tensors are (just) tensor products of vectors. It is the case though that all tensors are elements of tensorproducts of vector spaces.
With that in mind, let's look at the properties that the tensor product of vectors must satisfy.
In essense the properties are simply the properties of bilinearity.
The tensor product of $u \in U$ and $v \in V$ is denoted $ u \otimes v $ and satifies the properties
$$ u \otimes v $$

$$(a * u + v) \otimes w = a *  u \otimes w + v \otimes w$$

and

$$u \otimes (a * v + w) = a * u \otimes v + u \otimes w$$

So then it may be tempting to say that the definition of tensors in the tensor product space $U \otimes V$ is just the union of all the tensor products of vectors from $U$ with vectors from $V$. However, it is easy to show that this would leave out tensors on the form $u \otimes v + r \otimes s$, if we let $u$, $v$, $r$, and $s$
be linearly independent vectors from a four-dimensional space $V$ and we consider the tensor product space $V \otimes V$.



### The Evaluation Map

### Tensor Contraction

### Covariance and Contravariance

Dual vectors are also frequently called *covectors* or *linear forms*, the components of a vector in a basis are called *covariant* or
*contravariant* depending on whether they scale proportionally or inversely proportionally with the change to the basis vectors.
Covariant components are usually written using *lower indices*, whilst contravariant components are usually written using *upper indices*.

It is important to note that vectors themselves do not change with a change of basis, and are therefore *invariant* to change of basis.
It is only the *components* of a vector *in a basis* that can be covariant or contravariant.



### The Metric Tensor

