"""
This file contains the original MATH prompt from the Minerva paper 
https://arxiv.org/abs/2206.14858 and a template to compose solutions 
to math problems.

The MATH_MINERVA_PROMPT string includes an introduction comment that explains 
the tasks, followed by a natural language solution and a short answer.
"""


MINERVA_MATH_PROMPT =  '''Problem:
Find the domain of the expression \(\frac{\sqrt{x-2}}{\sqrt{5-x}}\).

Solution:
The expressions inside each square root must be non-negative. Thus, for the numerator, we have:
\[ x-2 \ge 0 \]
\[ \Rightarrow x\ge2 \]
For the denominator, we need:
\[ 5 - x \ge 0 \]
\[ \Rightarrow x \le 5 \]
But since the denominator cannot be zero:
\[ 5-x>0 \]
\[ \Rightarrow x<5 \]
Therefore, combining the two conditions, the domain of the expression is:
\[ [2,5) \]

Final Answer:
$[2,5)$


Problem:
Given that \(\det \mathbf{A} = 2\) and \(\det \mathbf{B} = 12\), find \(\det (\mathbf{A} \mathbf{B})\).

Solution:
Using the properties of determinants, we have:
\[ \det (\mathbf{A} \mathbf{B}) = (\det \mathbf{A})(\det \mathbf{B}) \]
Substituting the given values:
\[ \det (\mathbf{A} \mathbf{B}) = (2)(12) = 24 \]

Final Answer:
$24$


Problem:
Terrell usually lifts two 20-pound weights 12 times. If he switches to two 15-pound weights, how many times must he lift them to match the total weight lifted earlier?

Solution:
When Terrell lifts two 20-pound weights 12 times, the total weight lifted is:
\[ 2 \times 12 \times 20 = 480 \text{ pounds} \]
If he lifts two 15-pound weights \( n \) times, the total weight lifted is:
\[ 2 \times 15 \times n = 30n \text{ pounds} \]
Equating the two expressions:
\[ 30n = 480 \]
\[ n = \frac{480}{30} = 16 \]

Final Answer:
$16$


Problem:
Given the system of equations:

\[
\begin{align*}
6x-4y &= a, \\
6y-9x &= b
\end{align*}
\]

If there's a solution \((x, y)\) where both \(x\) and \(y\) are non-zero, determine the value of \(\frac{a}{b}\), assuming \(b\) isn't zero.

Solution:
Multiplying the first equation by \(-\frac{3}{2}\) gives:
\[ 6y-9x = -\frac{3}{2}a \]
Given that:
\[ 6y-9x = b \]
We can equate the two expressions:
\[ -\frac{3}{2}a = b \]
From which we find:
\[ \frac{a}{b} = -\frac{2}{3} \]

Final Answer:
$-\frac{2}{3}$'''


MINERVA_MATH_TEMPLATE = '''
Problem:
{question}

Solution:
'''