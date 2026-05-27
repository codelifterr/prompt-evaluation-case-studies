# Prompt Evaluation Case Studies

A portfolio repository for AI output evaluation, prompt quality, localization review, and practical quality assurance.

## Target roles this supports

- AI response evaluator
- Turkish language evaluator
- Localization QA reviewer
- Prompt evaluation specialist
- Junior AI operations / AI data quality roles

## Evaluation rubric

When reviewing an AI answer, I check:

1. Instruction following
2. Factual accuracy
3. Completeness
4. Clarity and structure
5. Tone and audience fit
6. Safety and policy issues
7. Localization quality, if relevant

## Example: Turkish localization review

Checklist:

- Is the Turkish natural, not machine-translated?
- Are formal/informal tone choices consistent?
- Are idioms translated meaningfully, not literally?
- Are dates, currencies, names, and local context handled correctly?
- Is the response useful for a Turkish-speaking user?

## Example: Prompt improvement process

Before:

```text
Write about AI agents.
```

Problem:

- Too broad
- No audience
- No output format
- No quality criteria

Improved:

```text
Explain AI agents to a non-technical recruiter in 5 bullet points. Focus on practical business use cases, avoid hype, and include one limitation.
```

Why better:

- Clear audience
- Clear structure
- Clear tone
- Includes constraint against overclaiming

## Example: AI answer review template

```md
## Score
7/10

## Strengths
- Clear structure
- Mostly answers the question

## Issues
- Missing concrete example
- Slightly too generic

## Suggested correction
Add one realistic use case and mention a limitation.
```

## Portfolio note

This repository is designed to demonstrate evaluation thinking and communication clarity for recruiter review.
