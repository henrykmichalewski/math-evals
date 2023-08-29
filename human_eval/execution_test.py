"""
This module contains a set of tests for GSM8k problem type.

We leverage the unittest framework to structure our tests. The TestGsm8k 
class houses all of our test cases, testing functions like 
'extract_gsm8k_answer' and 'check_gsm8k_correctness'.

Each test ensures an aspect of functionality is working correctly by 
comparing generated results with expected output.
"""

import unittest
from human_eval.execution import extract_gsm8k_answer, check_gsm8k_correctness
from data import gsm8k_python_prompt

class TestGsm8k(unittest.TestCase):
    """Testing the GSM8K problem type."""

    def setUp(self):
        self.problem = {
            'question': 'Kylar went to the store to buy glasses for his new apartment...',
            'answer': 'The discount price of one glass is 60/100...#### 64'
        }
        self.expected_output = 64.0
        prompt = gsm8k_python_prompt.PYTHON_PROMPT + gsm8k_python_prompt.PYTHON_TEMPLATE.format(
            question=self.problem['question'])
        # Sample HumanEval-like problem dictionary.
        self.he_problem = {'prompt': prompt,
                           'answer': self.problem['answer'],
                           'entry_point': 'exercise9',
                           'task_id': 1}
        self.task_id = 1
        self.sample_completion = """
def exercise9():
    return 4.123 # sample right answer for illustration, your actual code may differ
"""
    def test_extract_gsm8k_answer(self):
        """Testing the extraction of the GSM answer extraction function based on pre-set values."""
        self.assertEqual(extract_gsm8k_answer(self.problem), self.expected_output)

    def test_check_correctness(self):
        """Testing the correctness of the GSM checker function based on pre-set values."""
        result = check_gsm8k_correctness(self.he_problem, self.sample_completion, self.task_id)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()