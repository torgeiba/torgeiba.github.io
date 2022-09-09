# On the binomial theorem

The binomial theorem is a useful tool when working with polynomials.
It can be written as follows:

$$ (x + y)^d = \sum_{i=0}^d  \binom{d}{i} x^{d-i}y^i $$

The name derives from the sum of two variables (monomial, binomial, ..., polynomial).
The factor $\binom{d}{i}$ is called the binomial coefficient.

The binomial coefficients can be defined in a number of ways.
They can be defined to be the coefficients where the binomial theorem holds,
but they can also be defined in terms of a ratio of factorials

$$\binom{d}{i} = \frac{d!}{(d-i)!\,i!}$$

Or via a recurrence relations

$$\binom{d}{i} = \binom{d-1}{i} + \binom{d-1}{i-1}$$

With the initial values, or boundry values

$$\binom{d}{0} = \binom{d}{d} = 1$$

The core aspect of the theorem is that it relates what is essentially a product of sums
to a sum of products.

$$ (x + y)^d = \prod_{i=1}^d (x + y)  = \sum_{i=0}^d  \binom{d}{i} x^{d-i}y^i $$



## Properties
symmetry in x and y

## Proof of the theorem

## Applications and connections to other polynomial relations

The binomial theorem are related to the Bernstein polynomials, Bézier curves,
can be used to prove the power rule in calculus (differentiation of monomials),
