"""Homework 3 Template
This is the template for HW3 in CSE 4256 at The Ohio State University.
"""
#Sudi Yussuf

# TODO
# Besides the syntax used to create them, what are three fundamental differences
# between a Python \lstinline{set} and a Python \lstinline{list}?
# 1. Sets are unordered whereas lists are ordered.
# 2. Objects in a set must be unique.
# 3. Objects in a set must be hashable.


def all_unique(ls: list) -> bool:
    """Reports whether the list contains all unique elements.
  Positional Arguments:
  ls -- A list of hashable items, such as ints.
  """
    #this line creates a boolean list that returns all true 
    #values unless a list value is repeated
    return False not in [ls.count(i) == 1 for i in ls]
    
# l = [1,2,3,4,5]
# print(all_unique(l))


def maybe_apply_all(s: set, f=lambda x: x + 5):
    """Applies function f to each element of s, updating s in place."""
    for x in s:
        x = f(x)


# TODO
# Is this function correct according to the docstring? If not, what's wrong?
# Answer: This function doesn't work because the x is immutable and cannot be changed during an iteration.


def apply_all(s: set, f=lambda x: x + x):
    """Applies function f to each element of s, updating s in place."""

    #create a temporary set
    s1 = set()

    #add the changed values to the temporary set
    for x in s:
        i = f(x)
        s1.add(i)

    #clear the old set and update it with
    #data from the temp set
    s.clear()
    s.update(s1)

    print(s)

    pass

# s = {1,2,3,4,5}
# apply_all(s)

# TODO
# Does your solution to apply_all(s, f) work for all f?
# Answer: My solution does work for all f.

def subset_sum(s: set, t: int) -> bool:
  """Solves the Subset Sum problem.
  
  Returns True iff there is a subset of s whose sum is equal to t.
  Positional arguments:
  s -- A set of integers.
  t -- The target sum.  
  """
  #base cases
  if t == 0:
    return True
  elif len(s) == 0:
    return False
  else:
    x = s.pop()
    if x == t:
      return True
    #runs until subset is found
    else:
      return subset_sum(s, (t - x)) or subset_sum(s, t)
  
s = {1, 2, 3, 4, 5}
boo = subset_sum(s,6)
print(boo)


def is_subset_sum(sub: set, s: set, t: int) -> bool:
  """Checks a proposed solution to the Subset Sum Problem.
  Returns True iff sub is a subset of s and the sum of the elements of s is
  equal to t.
  Positional arguments:
  sub -- A set of integers; the proposed subset.
  s -- A set of integers.
  t -- The target sum.
  """
  #TODO
 
 #returns true or false if sub is a subset and equals t
  return sub.issubset(s) and sum(sub) == t
  
     
    
# s = {1, 2, 3, 4, 5}
# sub = {2,3}
# boo = is_subset_sum(sub,s,5)
# print(boo)


# **********************
#  Challenge Activities
# **********************
def subset_sum_approx(s: set, t: int) -> bool:
    """Approximates the Subset Sum problem.
  
  Returns True iff there is a subset of s whose sum is approximately t.
  Positional arguments:
  s -- A set of integers.
  t -- The target sum.  
  """
    # TODO
    pass


def subset_sum_dyn(s: set, t: int) -> bool:
    """Solves the Subset Sum problem using dynamic programming.
  
  Returns True iff there is a subset of s whose sum is approximately t.
  Implemented using Dynamic Programming.
  Positional arguments:
  s -- A set of integers.
  t -- The target sum.  
  """
    # TODO
    pass


def subset_sum_h_s(s: set, t: int) -> bool:
    """Solves the Subset Sum problem using the Horowitz-Sahni algorithm.
  
  Returns True iff there is a subset of s whose sum is approximately t.
  Implemented using the Horowitz-Sahni algoritm. 
  Positional arguments:
  s -- A set of integers.
  t -- The target sum.  
  """
    #TODO
    pass
