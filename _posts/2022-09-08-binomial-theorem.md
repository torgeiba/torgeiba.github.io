# On the binomial theorem

The binomial theorem is a useful tool when working with polynomials.
It can be written as follows:

$$ (x + y)^d = \sum_{i=0}^d  \binom{d}{i} x^{d-i}y^i $$

The name derives from the sum of two variables (monomial, binomial, ..., polynomial).
The factor $\binom{d}{i}$ is called the binomial coefficient, and can be read as "$d$ choose $i$",
alluding to the fact that the binomial coefficients count the number of (different) ways 
of choosing $i$ (different) number of items from a set of $d$ items. Or to put it another way,
the number of unique subsets of size $i$ of a set of size $d$. Or drawing $i$ items among $d$
disregarding the order of the draws and without returning drawn items.

The binomial coefficients can be defined in a number of ways.
They can be defined to be the coefficients where the binomial theorem holds,
but they can also be defined in terms of a ratio of factorials

$$\binom{d}{i} = \frac{d!}{(d-i)!\,i!}$$

Or via a recurrence relations

$$\binom{d}{i} = \binom{d-1}{i} + \binom{d-1}{i-1}$$

With the initial values (or boundry values)

$$\binom{d}{0} = \binom{d}{d} = 1$$

Since the factorial function counts the number of permutations of a sequence,
the definition based on factorials can be interpreted as starting out with the number of
permutations of $d$ elements and then accounting for the fact that we do not care about the
order of the chosen elements, $i!$, or the order of the rest of the items, $(d-i)!$, 
by dividing them out.

The recurrence relation definition of the binomial coefficients provides and easy way to
manually work out pascal's triangle.

Another interesting fact about the binomial coefficients for a given degree $d$ is that they sum to 
$2^d$, that is

$$\sum_{i=0}^{d} \binom{d}{i} = 2^d$$

This can be seen by considering the expansion of $(x + y)^d$ by the distributive property
and counting number the terms (before like terms are collected, if one was to simplify the expression).
Each term in the expansion corresponds to an ordered choice of one of two variables, either x or y.
This can be encoded as a string of $d$ bits, each encoding the choice for a single set of parentheses.
And since a binary number with $d$ bits can encode $2^d$ different values, this must also be the number
of terms in the expansion, and in turn the sum of the binomial coefficients.




A core aspect of the theorem is that it relates what is essentially a product of sums
to a sum of products.

$$ (x + y)^d = \prod_{i=1}^d (x + y)  = \sum_{i=0}^d  \binom{d}{i} x^{d-i}y^i $$



## Properties
symmetry in x and y

## Proof of the theorem

The proof of the theorem is a fairly straight forward induction based argument,

assume it holds for a base case, and for degree $d$, then we need to show that it also holds for $d+1$

starting from the left hand side we have

$$(x + y)^{d+1}$$

$$(x + y)^{d} (x + y)$$

Since we assumed it holds for degree $d$ we can substitute that in:

$$ \sum_{i=0}^d  \binom{d}{i} x^{d-i}y^i (x + y)$$

we distribute the $(x+y)$ factor 

$$ x \sum_{i=0}^d  \binom{d}{i} x^{d-i}y^i + y \sum_{i=0}^d  \binom{d}{i} x^{d-i}y^i$$

and distribute $x$ and $y$ again into their respective sums and update the exponents accordingly

$$ \sum_{i=0}^d  \binom{d}{i} x^{d+1-i}y^i + \sum_{i=0}^d  \binom{d}{i} x^{d-i}y^{i+1}$$

we change the summation index of the second sum to range to $1$ to ${d+1}$ and update the terms accordingly

$$ \sum_{i=0}^d  \binom{d}{i} x^{d+1-i}y^i + \sum_{i=1}^{d+1}  \binom{d}{i-1} x^{d+1-i}y^{i}$$

we temporarily extract the $i=0$ term from the first sum and the $i=d+1$ term from the second sum
in order to match their ranges again

$$\binom{d}{0} x^{d+1}y^0 + \binom{d}{d} x^{0}y^{d+1} + \sum_{i=1}^d  \binom{d}{i} x^{d+1-i}y^i + \sum_{i=1}^{d}  \binom{d}{i-1} x^{d+1-i}y^{i}$$

Then we combine the sums

$$\binom{d}{0} x^{d+1}y^0 + \binom{d}{d} x^{0}y^{d+1} +  \sum_{i=1}^d  (\binom{d}{i} + \binom{d}{i-1}) x^{d+1-i}y^i $$

we use the recurrence property of the binomial coefficients to combine them

$$\binom{d}{0} x^{d+1}y^0 + \binom{d}{d} x^{0}y^{d+1} +  \sum_{i=1}^d  \binom{d+1}{i} x^{d+1-i}y^i $$

we use the fact that $\binom{d}{0} = \binom{d+1}{0} = \binom{d}{d} = \binom{d+1}{d+1} = 1$ to insert them again

$$\binom{d+1}{0} x^{d+1}y^0 + \binom{d+1}{d+1} x^{0}y^{d+1} +  \sum_{i=1}^d  \binom{d+1}{i} x^{d+1-i}y^i $$

we insert the terms back into the summation as the terms for $i=0$ and $i=d+1$

$$\sum_{i=0}^{d+}  \binom{d+1}{i} x^{d+1-i}y^i $$

which is the desired result



$$(x+y)^{d+1} = (x+y)^{d} (x+y) = x (x+y)^{d} + y (x+y)^{d} $$

## Applications and connections to other polynomial relations

The binomial theorem are related to the Bernstein polynomials, Bézier curves and
can be used to prove the power rule in calculus (differentiation of monomials).
It is also formally related to Leibniz rules, which take the same form, in umbral calculus.


