"""
Enhanced rules module for eco-code-analyzer.
This package contains the rule system for analyzing code for ecological impact.
"""

from . import algorithm

# Import all rule categories to register them
from . import energy
from . import io
from . import memory
from .base import RuleExample, Rule, RuleMetadata, RuleRegistry
from .context import AnalysisContext
from .patterns import PatternDetector

# Export the rule registry for use by the analyzer
__all__ = [
    "RuleExample",
    "Rule",
    "RuleMetadata",
    "RuleRegistry",
    "AnalysisContext",
    "PatternDetector",
]
