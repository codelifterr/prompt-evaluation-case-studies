from __future__ import annotations

import json
import sys
from pathlib import Path

from .localization import turkish_localization_checks
from .rubric import RubricItem, evaluate


def main(argv: list[str] | None = None) -> int:
    argv = argv or sys.argv[1:]
    if not argv:
        print("Usage: python3 -m prompt_eval.cli examples/turkish_localization_case.json")
        return 2
    data = json.loads(Path(argv[0]).read_text(encoding="utf-8"))
    items = [RubricItem(**item) for item in data["rubric"]]
    result = evaluate(items)
    print(f"Score: {result.percentage}%")
    if result.issues:
        print("Issues:")
        for issue in result.issues:
            print(f"- {issue}")
    if "localized_text" in data:
        checks = turkish_localization_checks(data["localized_text"])
        if checks:
            print("Localization checks:")
            for check in checks:
                print(f"- {check}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
