# Cheatsheet for Testing with 'unittest'

### Basic Test Functions:

| Method | Checks that |
| ------ | ----------- |
| assertEqual(a, b) |	a == b |
| assertNotEqual(a, b) |	a != b |
| assertTrue(x) |	bool(x) is True |
| assertFalse(x) |	bool(x) is False |
| assertIs(a, b) |	a is b |
| assertIsNot(a, b) |	a is not b |
| assertIsNone(x) |	x is None |
| assertIsNotNone(x) |	x is not None |
| assertIn(a, b) |	a in b |
| assertNotIn(a, b) |	a not in b |
| assertIsInstance(a, b) |	isinstance(a, b) |
| assertNotIsInstance(a, b) |	not isinstance(a, b) |


### Decorators:

Unconditionally skip the decorated test. reason should describe why the test is being skipped.
@unittest.skip(reason)

Skip the decorated test if condition is true.
@unittest.skipIf(condition, reason)

Skip the decorated test unless condition is true.
@unittest.skipUnless(condition, reason)

Mark the test as an expected failure. If the test fails when run, the test is not counted as a failure.
@unittest.expectedFailure
