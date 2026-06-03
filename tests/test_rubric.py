import unittest

from prompt_eval.rubric import RubricItem, evaluate


class RubricEvaluationTest(unittest.TestCase):
    def test_evaluate_weighted_score(self):
        result = evaluate([
            RubricItem("clarity", 1.0, 8, "clear"),
            RubricItem("completeness", 1.0, 6, "missing example"),
        ])
        self.assertEqual(result.percentage, 70.0)
        self.assertEqual(result.issues, ("missing example",))


if __name__ == "__main__":
    unittest.main()
