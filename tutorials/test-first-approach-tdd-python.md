---
title: The Test-First Approach - Implementing TDD in Python
subtitle: All code is guilty untill proven innocent!
format:
    pdf:
      toc: true
      colorlinks: true
    docx:
      toc: true
      highlight-style: github
    html:
      toc: true
      toc-expand: 2
      embed-resources: true
---

## Introduction

This tutorial demonstrates test-driven development (TDD) by building a simple calculator application in Python using the `unittest` module. We will create the core arithmetic functions of add, subtract, multiply and divide following incremental red-green-refactor cycles. The completed program with all test cases is provided in the https://github.com/teaching-repositories/test-first-approach-tdd-python.git repository.

## What Programming Paradigm to use?

With this example, we are taking a purer test-driven approach by starting with just an add function, rather than assuming a larger class structure upfront. This defers design commitments and lets the tests drive emergence of the appropriate programming style.

However, TDD does not forbid some initial assumptions to scaffold the process, as long as the implementation remains flexible. For instance, in some cases starting with empty class stubs can provide anchors for the tests to build upon. The key is balancing upfront structure with test-driven development. Core TDD principles still apply even with some initial scaffolding.

By starting with a simple functional interface in this introductory example, we aim to demonstrate the purer outside-in approach. But we recognise that pragmatic hybrid styles are also valid and may be better suited depending on the context. The goal is to avoid overly rigid upfront design while utilising tests to enable iterative refinement. 

The feedback loop of making tests pass guides the paradigm and design into something that fits the problem, rather than trying to fit the problem to an initial choice. This balance enables writing clean, maintainable code.

## The process

### Organising Tests

For this tutorial, we will one test file for each operation, each containing a class that tests a specific capability of our calculator module. 

For example:

- `test_add.py` - Contains `TestAdd` class
- `test_subtract.py` - Contains `TestSubtract` class

This keeps our tests focused and modular. Each test file tests one aspect of the system.

We can then aggregate the test classes into a test suite in `all_tests.py`:

```python
import unittest
from test_add import TestAdd 
from test_subtraction import TestSubtraction

# Additional imports as test classes are added

if __name__ == '__main__':
   unittest.main()
```

Running `all_tests.py` will execute all our test classes, verifying the full system.

This structure demonstrates good testing practices:

- Individual test classes keep tests isolated and focused 
- The test suite provides overall coverage
- New test classes can be easily added

This approach will be used for the tutorial to showcase robust test organisation.

The full implementation can be viewed in the GitHub https://github.com/teaching-repositories/test-first-approach-tdd-python.git repository. 


### First iteration

First, let's write a failing test. Create a file called `test_add.py` and copy the following. We are creating a `TestAdd` class that inherits from `unittest.TestCase`. 

We will structure our test cases using the AAA pattern - Arrange, Act, Assert. The Arrange section sets up objects and inputs needed for the test. The Act section executes the code being tested. The Assert section verifies the expected results.

In Python, we define a class using the `class` keyword followed by the class name. 

Here our class is called `TestAdd`. By convention, test classes are often named starting with Test.

`(unittest.TestCase)` means the `TestAdd` class inherits from the `TestCase` class defined in the `unittest` module. This gives our test class access to useful testing functions like `assertEqual()`.

We don't need to understand inheritance and objects yet. For now, know that defining a class like this allows grouping related test functions together, while `TestCase` provides test-specific utilities.

We'll focus on just using the test class as a container for test functions. The object-oriented concepts will be covered more formally later.

When writing a test method, we have one constraint - the method **must** be prefixed with `test_`. 

```python
import unittest

class TestAdd(unittest.TestCase):

  def test_add_integers(self):
    # Arrange
    num1 = 5
    num2 = 3
    
    # Act
    result = add(num1, num2)
    
    # Assert
    self.assertEqual(result, 8)

if __name__ == "__main__":
    unittest.main()
```

This test obviously fails as there is no add function yet. Let's create `add()` and write the minimal code necessary to pass the test.

```python
def add(num1, num2):
  return 8 
``` 

Where should this code go? There are a few common options for where to put the `add()` function code in relation to the test file:

- Put it in the same test file. This keeps things together for the initial TDD cycle, but could get messy as codebases grow.
- Create a separate calculator.py module for the add function and import it into the test file. This separates concerns better but requires switching between files.
- Use a src folder structure with /tests and /src dirs. Import add function from /src. Scales well.

Some guidelines:

- If just experimenting, keeping test and code in one file is fine.
- For real projects, separate into files/modules based on logical concerns.
- Import between test and source files enables loose coupling.
- Structure for readability and modularity first, worry about separation later.

So for this initial TDD iteration, keeping the `add()` function in the same test file is reasonable. But separating into modules is a good idea as complexity increases to manage concerns.

```python
import unittest

def add(num1, num2):
  return 8 

class TestAdd(unittest.TestCase):

  def test_add_integers(self):
    # Arrange
    num1 = 5
    num2 = 3
    
    # Act
    result = add(num1, num2)
    
    # Assert
    self.assertEqual(result, 8)

if __name__ == "__main__":
    unittest.main()
```


#### First Iteration wrap up

In this first test-driven development cycle, we followed these steps:

- Wrote an initial failing test for the `add()` function based on requirements. This test failed since `add()` was not yet implemented.
- Added the minimal code in `add()` to make the test pass, just returning a hard-coded result.
- The test now passes as expected.

This demonstrates the red-green-refactor TDD flow:

- Red - The failing test indicates incomplete code.
- Green - We wrote the simplest code to make the test succeed.
- Refactor - No changes yet, but we'll improve the code incrementally.

By starting with a failing test, we are driving the implementation based on specific required behaviour. The test failures guide the development process.

We focused on the minimal code to pass the test, avoiding over-engineering. As more tests are added, we'll refactor and expand the implementation.

This cycle allowed us to take the first TDD step of going from failing test to passing code in small, validated increments. We'll continue to build on this foundation iteratively.

The key takeaways are:

- Start by writing a failing test based on requirements
- Focus on the minimal code to make it pass
- Build incrementally in small steps


### Second iteration

This now passes the test. Let's write another test. But where do these tests come from?

In TDD, test cases are written incrementally as part of the red-green-refactor cycle, rather than being pre-defined upfront. The developer thinks through required behaviours and likely edge cases as they write each test. However, some level of upfront analysis of requirements and design considerations helps guide the scope and priorities of testing. High-risk areas and essential functionality get targeted first. The developer may sketch out possible test scenarios to drive the TDD iterations, but the specifics emerge and evolve as code is written. Tests are derived interactively from both thinking through expected behaviours and discovering new considerations while incrementally expanding the code. Maintaining a test backlog and test matrices can help organise testing, but test cases aren't comprehensive before writing code. The interplay between hands-on coding and critical thinking guides thorough test coverage.

Here is our next failing test. I have only included the relevant test code to make it easier to see the new test.

```python 
def test_add_integers(self):
  # Arrange
  num1 = 5 
  num2 = 3

  # Act
  result = add(num1, num2)

  # Assert
  self.assertEqual(result, 8)
  
  # Arrange
  num1 = 2
  num2 = 4
  
  # Act
  result = add(num1, num2)

  # Assert
  self.assertEqual(result, 6)
```

Should test methods have more than one assert?

Proper unit tests should fail for a single clear reason, so aim for one assertion per test method focusing on one logical concept under test. However, multiple assertions can be appropriate when kept cohesive - for example, asserting against different properties of the same object to test related behaviours. The goal is balancing improved test coverage with understandability, by keeping assertions grouped by conceptual units yet isolating distinct behaviours across separate methods. Tests should validate one concern at a time, but validating concerns may require multiple targeted assertions.

So let's write minimal code to pass the test.

```python
import unittest

def add(num1, num2):
  return num1 + num2

class TestAdd(unittest.TestCase):

    def test_add_integers(self):
      # Arrange
      num1 = 5 
      num2 = 3

      # Act
      result = add(num1, num2)

      # Assert
      self.assertEqual(result, 8)

      # Arrange
      num1 = 2
      num2 = 4

      # Act
      result = add(num1, num2)

      # Assert
      self.assertEqual(result, 6)
    
if __name__ == "__main__":
    unittest.main()
```

Let's do some simple refactoring. We will move the `add()` function into its own file. Create a file called `calculator.py` and copy `add()` into the file. 

```python
def add(num1, num2):
  return num1 + num2
```

In this refactoring stage, we want to restructure the code to keep the test and implementation separate. Having the `add()` function defined in the test module works for our initial TDD cycle, but doesn't scale well.

By moving `add()` into its own calculator module, we establish cleaner separation of concerns. The test module just handles testing, while the calculator module encapsulates the implementation details.

This sets us up nicely for expanding the calculator capabilities going forward. As we add more functions like subtract(), multiply(), etc, they can all be kept together in the calculator module and imported into the test module.

Refactoring is an important part of TDD. As the code evolves, we refactor to improve the design while ensuring all tests continue to pass. This enables incremental development while maintaining a clean architecture. The tests provide safety nets during refactoring changes.

Now remove the `add()` function from `test_add.py`. To access the `add()` function within the `TestAdd` class we will need to import the function.

```python  
import unittest
from calculator import add

class TestAdd(unittest.TestCase):

    def test_add_integers(self):
      # Arrange
      num1 = 5 
      num2 = 3

      # Act
      result = add(num1, num2)

      # Assert
      self.assertEqual(result, 8)

      # Arrange
      num1 = 2
      num2 = 4

      # Act
      result = add(num1, num2)

      # Assert
      self.assertEqual(result, 6)

if __name__ == "__main__":
    unittest.main()
```

Now rerun the tests to make sure everything is still working. 

#### Second Iteration Wrap up
In this second TDD cycle, we took the next incremental step of adding another failing test for a new set of inputs. After getting this test to pass with the minimal code update, we did some refactoring to organise the code.

Key points:

- Added a second test case with different inputs to expand coverage.
- Implemented the actual addition logic in `add()` to make both tests pass.
- Refactored by moving `add()` to its own module to separate concerns.
- Imported `add()` into the test module to maintain loose coupling.
- Validated that all tests still pass after refactoring code organisation.

Each iteration continues to build on the existing code in small steps driven by failing tests. We followed the Red-Green-Refactor workflow to incrementally expand the calculator capability while keeping the code clean through refactoring.

This TDD cycle focused on adding a second targeted test case and introducing some structure. In the next iteration, we'll continue extending the test suite and implementation in this manner.

### Third iteration

Let's add another failing test. Perhaps we are concerned that 0 might cause problems. Let's check, by adding `0` and `1`. 

```python
import unittest
from calculator import add

class TestAdd(unittest.TestCase):

    def test_add_integers(self):
      # Arrange
      num1 = 5 
      num2 = 3

      # Act
      result = add(num1, num2)

      # Assert
      self.assertEqual(result, 8)

      # Arrange
      num1 = 2
      num2 = 4

      # Act
      result = add(num1, num2)

      # Assert
      self.assertEqual(result, 6)

      # Arrange
      num1 = 0
      num2 = 1

      # Act
      result = add(num1, num2)

      # Assert
      self.assertEqual(result, 1)
  

if __name__ == "__main__":
    unittest.main()
```

The test passes even though we expected it to fail initially. When this happens, we have a few options:

- Leave the test as-is
- Expand the test with more cases
- Use it as a stepping stone to refactor
- Mark as skipped
- Remove if low value

Since 0 is an important edge case, we'll leave this test in place for now even though it passed upfront. We may expand it later for more coverage.

So when do I stop writing tests?

There is no definitive answer on when to stop writing tests. Key guiding principles are:

- Write tests driven by requirements and risk analysis.
- Aim for coverage of typical usage, edge cases and failure modes.
- Prioritise areas with complexity, ambiguity, or critical behaviour.
- Stop when all components have adequate test coverage based on risk.
- Refactor tests along with code to keep them relevant.
- Make sure the test suite runs efficiently and adds value.

So leverage an initial passing test as a springboard for improving coverage and quality. Focus on writing tests that address meaningful potential issues versus unnecessarily repetitive cases. And re-evaluate regularly to ensure the test suite improves the codebase over time.

## Conclusion

Through this tutorial we walked through the red-green-refactor TDD workflow to build the core add function, starting with no implementation and letting failing tests drive the design. The process helped us discuss considerations like separating code and tests, single vs multiple asserts, refactoring, and stopping criteria.

The completed calculator example with full test cases is available in the https://github.com/teaching-repositories/test-first-approach-tdd-python.git repository for reference. TDD takes practice, but following the cycle of test-first development, incremental implementation, and constant refactoring will lead to robust, maintainable code.