"""
Base classes for the rule system.
"""

import ast
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Type, Literal

from eco_code_analyzer.data import Example, Suggestion, AppConfig
from eco_code_analyzer.rules.context import AnalysisContext
from eco_code_analyzer.rules.rule_example import RuleExample


@dataclass
class RuleMetadata:
    """Metadata for a rule including description, impact, and references."""

    name: str
    description: str
    category: str
    impact: Literal["high", "medium", "low"]
    references: set[str] = field(
        default_factory=set
    )  # Research papers or articles supporting this rule
    examples: RuleExample | None = None  # Good/bad examples


class Rule:
    """Base class for all eco-code rules."""

    metadata: RuleMetadata

    def __init__(self, config: AppConfig = None) -> None:
        self.config = config or {}

    def check(self, node: ast.AST, context: AnalysisContext) -> float:
        """
        Check if the rule applies to this node.
        Returns a score multiplier (< 1.0 for penalties, > 1.0 for rewards).
        """
        raise NotImplementedError("Rule subclasses must implement check method")

    def get_suggestion(self) -> Suggestion:
        """Get improvement suggestion for this rule."""

        return Suggestion(
            name=self.metadata.name,
            description=self.metadata.description,
            category=self.metadata.category,
            impact=self.metadata.impact,
            example=Example(
                efficient=self.metadata.examples["efficient"],
                inefficient=self.metadata.examples["inefficient"],
            )
            if self.metadata.examples
            else None,
            environmental_impact="Reduces energy consumption and carbon footprint.",
            references=self.metadata.references
            if self.metadata.references
            else "",
        )


class RuleRegistry:
    """Registry to manage all eco-code rules."""

    _rules: Dict[str, Dict[str, Type[Rule]]] = {}

    @classmethod
    def register(cls, rule_class: Type[Rule]) -> Type[Rule]:
        """Register a rule class."""
        category = rule_class.metadata.category
        if category not in cls._rules:
            cls._rules[category] = {}
        cls._rules[category][rule_class.metadata.name] = rule_class
        return rule_class

    @classmethod
    def get_rules(cls, category: Optional[str] = None) -> Dict[str, Type[Rule]]:
        """Get all rules or rules for a specific category."""
        if category:
            return cls._rules.get(category, {})
        return {
            name: rule
            for category in cls._rules.values()
            for name, rule in category.items()
        }

    @classmethod
    def create_rule_instances(cls, config: AppConfig) -> Dict[str, Dict[str, Rule]]:
        """Create instances of all registered rules with the given config."""
        instances = {}
        for category, rules in cls._rules.items():
            instances[category] = {
                name: rule_class(config) for name, rule_class in rules.items()
            }
        return instances

    @classmethod
    def get_categories(cls) -> List[str]:
        """Get all rule categories."""
        return list(cls._rules.keys())
