# Prompt Evaluation Case Studies

Python examples for evaluating AI outputs with weighted rubrics, issue detection, and Turkish localization quality checks.

This repository is intentionally small and inspectable. It shows how an evaluator can turn subjective review criteria into repeatable checks that produce a score, notes, and follow-up issues.

## What this project demonstrates

- Weighted rubric scoring for AI responses
- Detection of low-scoring quality dimensions
- Turkish localization checks for tone, untranslated strings, and awkward phrasing
- JSON-based case studies that can be reviewed or extended
- A simple CLI for repeatable local evaluation
- Tests that document expected scoring behavior

## Example use cases

- AI response quality review
- Prompt evaluation case studies
- Localization QA for Turkish output
- Lightweight evaluator training examples
- Human-in-the-loop review workflows

## Project structure

```text
prompt_eval/
  cli.py            # CLI entry point
  localization.py   # Turkish localization checks
  rubric.py         # Weighted scoring model
examples/
  turkish_localization_case.json
  hallucination_risk_case.json
  instruction_following_case.json
tests/
  test_rubric.py
```

## Run locally

```bash
python3 -m prompt_eval.cli examples/turkish_localization_case.json
python3 -m prompt_eval.cli examples/hallucination_risk_case.json
python3 -m prompt_eval.cli examples/instruction_following_case.json
```

## Run tests

```bash
python3 -m unittest discover -s tests -p 'test*.py'
```

## Example output

```text
Score: 78.57%
Issues:
- Missing clear source for one factual claim
- Turkish wording is understandable but not fully natural
Localization checks:
- Text may contain literal or awkward Turkish phrasing
```

## Evaluation dimensions

The examples use dimensions such as:

- Instruction following
- Factual accuracy
- Completeness
- Clarity
- Localization quality
- Safety and risk awareness

## Why this matters

AI evaluation work improves when rubrics are explicit, examples are reproducible, and reviewers can explain why a response passed or failed. This project provides a small technical base for that workflow.

## License

MIT
