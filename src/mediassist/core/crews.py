from crewai import Crew, Process
from .agents import (
    MedicalDataAgent,
    MedicalDataAcquisitionAgent,
    MedicalDataPreprocessingAgent,
    DiagnosisAgent,
    RecommendationAgent,
)
from .tasks import get_tasks


class MedicalCrew:
    def __init__(self, language):
        self.language = language
        self.agents = self._create_agents()
        self.tasks = get_tasks(self.agents, language)

    def _create_agents(self):
        return {
            "medical_data_agent": MedicalDataAgent(self.language).get_agent(),
            "medical_data_acquisition_agent": MedicalDataAcquisitionAgent(
                self.language
            ).get_agent(),
            "medical_data_preprocessing_agent": MedicalDataPreprocessingAgent(
                self.language
            ).get_agent(),
            "diagnosis_agent": DiagnosisAgent(self.language).get_agent(),
            "recommendation_agent": RecommendationAgent(self.language).get_agent(),
        }

    def run_crew(self, data):
        crew = Crew(
            agents=list(self.agents.values()),
            tasks=self.tasks,
            process=Process.sequential,
            full_output=True,
        )
        return crew.kickoff(inputs={"data": data})
