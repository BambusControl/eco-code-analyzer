from typing import NamedTuple, Dict

from eco_code_analyzer.data.analysis_result import AnalysisResult


class ProjectAnalysisResult(NamedTuple):
    file_results: Dict[str, AnalysisResult]
    overall_score: float
