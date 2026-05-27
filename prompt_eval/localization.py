from __future__ import annotations


def turkish_localization_checks(text: str) -> list[str]:
    """Return simple heuristic notes for Turkish localization review."""
    issues: list[str] = []
    if "you" in text.lower():
        issues.append("English word detected in Turkish text: you")
    if "merhaba" in text.lower() and "siz" not in text.lower() and "sen" not in text.lower():
        issues.append("Greeting is present but formality level is unclear")
    if len(text.strip()) < 40:
        issues.append("Text may be too short for a useful localized answer")
    return issues
