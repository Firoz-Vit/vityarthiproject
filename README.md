<img width="900" height="300" alt="image" src="https://github.com/user-attachments/assets/462f013c-f61e-4d16-b165-57b469db71ec" />

# Vityarthi Project 2025 - 26 batch by Firoz Ahmad Khan
⨳⨳⨳⨳⨳

PROJECT IDEA : “Given two families of lines, compute and visualize the integer intersection points.”

⨳⨳⨳⨳⨳

AIM OF THE PROJECT :

→ Define clear objectives and expected outcomes.
→ Use appropriate tools, libraries, or programming techniques based on the subject.
→ Problem definition
→ Top-Down design / modularization
→ Implementation
→ Testing and refinement

⨳⨳⨳⨳⨳

WHY THIS IDEA? :

This project is inspired by the way graphing tools like Desmos handle line visualization and intersection analysis. Imagine a scenario where a creator or programmer graphs a set of lines and then wonders:
“How can I determine how many of these intersection points have integer coordinates?”
This question, along with similar analytical challenges, often arises in the workflow of programmers, engineers, and inventors. The project replicates this foundational idea—combining visualization with computational logic—to demonstrate how such problems can be solved programmatically.

⨳⨳⨳⨳⨳

PROBLEM STATEMENT : 

We have two given lines as y = x + p_i and y = -x + q_i where p_i means p_1,p_2,....,p_n i.e n such kind of lines user can input.
Similarly, q_i means q_1,q_2,...,q_m i.e m such kind of lines use can input. Given that all p_i and q_i are integers.
let constraints be: { (1 ≤ n , m ≤ 10^5) ,  (0 ≤ p_i , q_i ≤ 10^9) , time limit per test: 2 seconds , memory limit per test: 512 megabytes }

⨳⨳⨳⨳⨳

IMPLEMENTATION :

Let, po = count of odd p_i values , pe = count of even p_i values , qo = count of odd q_i values , qe = count of even q_i values,
Each line from the first family is represented as: y = x + p_i​ and second be : y = -x + q_i where p_i , q_i will be integers.
Solving these two equations we get x = (q_i - p_i) / 2. Due to the condition the difference q_i - p_i should also be an integer.
Now, If x , p_i , q_i are integer so, y should also be an integer. Therefore, the intersection (x,y) has integer coordinates if and only if
(q_i - p_i) is even i.e divisible by 2. So, we want such pairs of p_i , q_i. Instead of double for looping to get the pair, whcih will
exceed the time complexity O(n^2) which is computationally expensive for large inputs; we can find po , pe , qo , qe O(n) since,
odd − odd = even , even − even = even , odd − even = odd (invalid) , even − odd = odd (invalid). This means an integer intersection occurs 
only when the pair have both odd or both even. 
Therefore, if (n = 3) , (p_i = 1 , 3 , 2) , (m = 2) , (q_i = 0 , 3) & so there will be three lines with p_i and two lines with q_i.
Whose graph in Desmos will look like this https://www.desmos.com/calculator/vom0cniihv and it is clear that the there are 6 intersection
points out of which only 3 have intger coordinates which is the solution of the required problem.
and po = 2 , pe = 1 , qo = 1 , qe = 1. Now since we know to find the number of combination of two sets say A = {a , b} and B = {c , d}
i.e if we want pairs like (a,c) , (a,d) , (b,c) , (b,d), we simply do |A| x |B| i.e 2 x 2 = 4. Simiarly if we want number of pairs which odd odd 
points are forming or even even are forming we can simply do ((po * qo) + (pe * qe)) i.e (2 * 1) + (1 * 1) = 3 .

⨳⨳⨳⨳⨳

PROGRAMMING : 

Code implementaion of the project is in cold.cpp in c++ and choco.py in python with plot.

⨳⨳⨳⨳⨳
