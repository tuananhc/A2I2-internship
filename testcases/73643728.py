Here are some unit test cases for the given task:

```python
import unittest
from mymodule import myFunc

class MyFuncTestCase(unittest.TestCase):
    def test_version_with_date(self):
        result = myFunc("0.1.1a0+date")
        self.assertEqual(result, "Version 0.1.1a0+date")

    def test_version_with_jira_task_number(self):
        result = myFunc("0.1.1a0+jiraTaskNumber")
        self.assertEqual(result, "Version 0.1.1a0+jiraTaskNumber")

    def test_version_with_git_branch_name(self):
        result = myFunc("0.1.1a0+gitBranchName")
        self.assertEqual(result, "Version 0.1.1a0+gitBranchName")

    def test_invalid_version_format(self):
        result = myFunc("invalid_version_format")
        self.assertEqual(result, "Invalid version format")

if __name__ == '__main__':
    unittest.main()
```

In the above code, we import the `unittest` library and the `myFunc` function from the `mymodule` module. Then, we create a test case class that inherits from `unittest.TestCase` and define test methods for various scenarios.

1. The `test_version_with_date` method tests the scenario where the version includes the current date.
2. The `test_version_with_jira_task_number` method tests the scenario where the version includes a Jira task number.
3. The `test_version_with_git_branch_name` method tests the scenario where the version includes the name of the Git branch.
4. The `test_invalid_version_format` method tests the scenario where the version has an invalid format.

Each test method calls the `myFunc` function with a specific version and asserts the expected result using the `self.assertEqual` method.

Finally, we run the tests by executing `unittest.main()`.