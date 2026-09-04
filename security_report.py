"""
SecurityReport data model.

Represents a completed, safe-to-store summary of a password check.
The raw password is never included anywhere in this model.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional

from .password_analysis import PasswordAnalysis


@dataclass
class SecurityReport:
    """A safe, storable summary of one password analysis session.

    Attributes:
        account_label: A user-chosen label for the account (e.g. "Gmail"),
            never the password itself.
        analysis: The PasswordAnalysis result for the checked password.
        breached: Whether the password appeared in a known data breach,
            or None if the breach check was not performed / unavailable.
        breach_count: How many times the password appeared in breaches,
            if known.
        ai_summary: Short AI-generated explanation/recommendation text.
        recommendations: List of short, actionable suggestions.
        timestamp: ISO-8601 timestamp for when the report was generated.
    """

    account_label: str
    analysis: PasswordAnalysis
    breached: Optional[bool] = None
    breach_count: Optional[int] = None
    ai_summary: str = ""
    recommendations: List[str] = field(default_factory=list)
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat(timespec="seconds"))

    def to_dict(self) -> dict:
        """Convert this report into a JSON-serializable dictionary."""
        return {
            "account_label": self.account_label,
            "analysis": self.analysis.to_dict(),
            "breached": self.breached,
            "breach_count": self.breach_count,
            "ai_summary": self.ai_summary,
            "recommendations": list(self.recommendations),
            "timestamp": self.timestamp,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "SecurityReport":
        """Rebuild a SecurityReport from a dictionary (e.g. loaded from JSON)."""
        return cls(
            account_label=data.get("account_label", "Unlabeled account"),
            analysis=PasswordAnalysis.from_dict(data.get("analysis", {})),
            breached=data.get("breached"),
            breach_count=data.get("breach_count"),
            ai_summary=data.get("ai_summary", ""),
            recommendations=data.get("recommendations", []),
            timestamp=data.get("timestamp", datetime.now().isoformat(timespec="seconds")),
        )
