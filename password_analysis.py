"""
PasswordAnalysis data model.

Represents the result of analyzing a single password's strength.
Never stores the raw password itself.
"""

from dataclasses import dataclass, field
from typing import List


@dataclass
class PasswordAnalysis:
    """Represents the strength findings for a single password check.

    Attributes:
        length: Number of characters in the password that was analyzed.
        has_upper: Whether the password contains an uppercase letter.
        has_lower: Whether the password contains a lowercase letter.
        has_digit: Whether the password contains a digit.
        has_symbol: Whether the password contains a symbol/punctuation character.
        score: Numeric strength score (0-100).
        category: Human-readable strength category ("Weak", "Medium", "Strong").
        reasons: List of short explanations supporting the score/category.
    """

    length: int
    has_upper: bool
    has_lower: bool
    has_digit: bool
    has_symbol: bool
    score: int
    category: str
    reasons: List[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        """Convert this analysis into a JSON-serializable dictionary."""
        return {
            "length": self.length,
            "has_upper": self.has_upper,
            "has_lower": self.has_lower,
            "has_digit": self.has_digit,
            "has_symbol": self.has_symbol,
            "score": self.score,
            "category": self.category,
            "reasons": list(self.reasons),
        }

    @classmethod
    def from_dict(cls, data: dict) -> "PasswordAnalysis":
        """Rebuild a PasswordAnalysis from a dictionary (e.g. loaded from JSON)."""
        return cls(
            length=data.get("length", 0),
            has_upper=data.get("has_upper", False),
            has_lower=data.get("has_lower", False),
            has_digit=data.get("has_digit", False),
            has_symbol=data.get("has_symbol", False),
            score=data.get("score", 0),
            category=data.get("category", "Unknown"),
            reasons=data.get("reasons", []),
        )
