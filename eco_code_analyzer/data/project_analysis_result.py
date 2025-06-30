from typing import TypedDict, Dict

from eco_code_analyzer.data.analysis_result import AnalysisResult


class ProjectAnalysisResult(TypedDict):
    file_results: Dict[str, AnalysisResult]
    overall_score: float