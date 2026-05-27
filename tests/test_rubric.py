from prompt_eval.rubric import RubricItem, evaluate


def test_evaluate_weighted_score():
    result = evaluate([
        RubricItem("clarity", 1.0, 8, "clear"),
        RubricItem("completeness", 1.0, 6, "missing example"),
    ])
    assert result.percentage == 70.0
    assert result.issues == ("missing example",)
