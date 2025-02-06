from crewai import Agent
from src.mediassist.utils.tools import get_tools
from textwrap import dedent


class MedicalDataAgent:
    def __init__(self, language):
        self.language = language
        self.tools = get_tools(language)

    def get_agent(self):
        if self.language == "en":
            return Agent(
                role="Medical Data Analyst",
                goal=dedent(
                    """\
                    Analyze data related to risk factors and symptoms of diabetes.
                    Risk factors for type 1 diabetes include genetic predisposition (HLA DR/DQ alleles) and potential environmental triggers such as viral infections.
                    Risk factors for type 2 diabetes include: Obesity, Physical Inactivity, Age, Family History, Ethnicity, and History of Gestational Diabetes.
                    Common symptoms of diabetes include: Frequent urination, Increased thirst, Excessive hunger, Unexplained weight loss, Fatigue, Blurred vision, and Slow-healing wounds."""
                ),
                backstory=dedent(
                    """\
                    You are an AI Agent specializing in analyzing data about the risk factors and symptoms of diabetes."""
                ),
                verbose=True,
                allow_delegation=False,
            )
        elif self.language == "ar":
            return Agent(
                role="تحليل بيانات طبية",
                goal=dedent(
                    """\
                    تحليل البيانات المتعلقة بعوامل الخطر وأعراض مرض السكري.
                    تشمل عوامل الخطر لمرض السكري من النوع 1 الاستعداد الوراثي (الأليلات HLA DR/DQ) والمحرضات البيئية المحتملة مثل العدوى الفيروسية.
                    تشمل عوامل الخطر لمرض السكري من النوع 2: السمنة، قلة النشاط البدني، العمر، التاريخ العائلي، العرق، وتاريخ الإصابة بسكري الحمل.
                    تشمل الأعراض الشائعة لمرض السكري: كثرة التبول، زيادة العطش، الجوع المفرط، فقدان الوزن غير المبرر، التعب، عدم وضوح الرؤية، وبطء التئام الجروح.
                    جميع الردود يجب أن تكون باللغة العربية"""
                ),
                backstory=dedent(
                    """\
                    أنت وكيل ذكاء اصطناعي متخصص في تحليل البيانات حول عوامل الخطر وأعراض مرض السكري.
                    جميع الردود يجب أن تكون باللغة العربية"""
                ),
                verbose=True,
                allow_delegation=False,
            )


class MedicalDataAcquisitionAgent:
    def __init__(self, language):
        self.language = language
        self.tools = get_tools(language)

    def get_agent(self):
        if self.language == "en":
            return Agent(
                role="Medical Data Acquisition Specialist",
                goal=dedent(
                    """\
                    Analyze data related to types of diabetes.
                    Type 1 diabetes is caused by autoimmune destruction of the beta cells in the pancreas, leading to an absolute insulin deficiency.
                    Type 2 diabetes develops when the body becomes resistant to insulin or when the pancreas fails to produce sufficient insulin.
                    Gestational diabetes occurs during pregnancy and usually disappears after childbirth.
                    Other specific forms of diabetes include monogenic forms such as Maturity-Onset Diabetes of the Young (MODY) and secondary diabetes resulting from conditions such as pancreatic disease or medication-induced diabetes."""
                ),
                backstory=dedent(
                    """\
                    You are an AI Agent specializing in analyzing data about types of diabetes."""
                ),
                verbose=True,
                allow_delegation=False,
                tools=self.tools,
            )
        elif self.language == "ar":
            return Agent(
                role="جمع البيانات الطبية",
                goal=dedent(
                    """\
                    تحليل البيانات المتعلقة بأنواع مرض السكري.
                    السكري من النوع 1 ينتج عن تدمير المناعة الذاتية لخلايا بيتا في البنكرياس، مما يؤدي إلى نقص كامل في الأنسولين.
                    السكري من النوع 2 يتطور عندما يصبح الجسم مقاومًا للأنسولين أو عندما يفشل البنكرياس في إنتاج كميات كافية من الأنسولين.
                    يحدث سكري الحمل أثناء الحمل وعادة ما يختفي بعد الولادة.
                    تشمل أشكال السكري المحددة الأخرى أشكالًا أحادية المنشأ مثل سكري النضج لدى الشباب (MODY) والسكري الثانوي الناتج عن حالات مثل أمراض البنكرياس أو السكري الناجم عن الأدوية.
                    جميع الردود يجب أن تكون باللغة العربية"""
                ),
                backstory=dedent(
                    """\
                    أنت وكيل ذكاء اصطناعي متخصص في تحليل البيانات حول أنواع مرض السكري.
                    جميع الردود يجب أن تكون باللغة العربية"""
                ),
                verbose=True,
                allow_delegation=False,
                tools=self.tools,
            )


class MedicalDataPreprocessingAgent:
    def __init__(self, language):
        self.language = language

    def get_agent(self):
        if self.language == "en":
            return Agent(
                role="Medical Data Preprocessing Specialist",
                goal="Preprocess collected medical data for analysis",
                backstory="You are an AI Agent responsible for preprocessing collected medical data for analysis.",
                verbose=True,
                allow_delegation=False,
            )
        elif self.language == "ar":
            return Agent(
                role="معالجة البيانات الطبية",
                goal="معالجة البيانات الطبية التي تم جمعها للتحليل",
                backstory="أنت وكيل ذكاء اصطناعي مسؤول عن معالجة البيانات الطبية التي تم جمعها للتحليل. جميع الردود يجب أن تكون باللغة العربية",
                verbose=True,
                allow_delegation=False,
            )


class DiagnosisAgent:
    def __init__(self, language):
        self.language = language

    def get_agent(self):
        if self.language == "en":
            return Agent(
                role="Diagnosis Specialist",
                goal="Provide an initial diagnosis based on preprocessed medical data",
                backstory="You are an AI Agent responsible for providing an initial diagnosis based on preprocessed medical data.",
                verbose=True,
                allow_delegation=False,
            )
        elif self.language == "ar":
            return Agent(
                role="تشخيص",
                goal="تقديم تشخيص مبدئي بناءً على البيانات الطبية المعالجة",
                backstory="أنت وكيل ذكاء اصطناعي مسؤول عن تقديم تشخيص مبدئي بناءً على البيانات الطبية المعالجة. جميع الردود يجب أن تكون باللغة العربية",
                verbose=True,
                allow_delegation=False,
            )


class RecommendationAgent:
    def __init__(self, language):
        self.language = language

    def get_agent(self):
        if self.language == "en":
            return Agent(
                role="Recommendation Specialist",
                goal="Provide recommendations for necessary medical tests and analyses",
                backstory="You are an AI Agent responsible for providing recommendations for necessary medical tests and analyses.",
                verbose=True,
                allow_delegation=False,
            )
        elif self.language == "ar":
            return Agent(
                role="توصية",
                goal="تقديم توصيات للفحوصات والتحاليل الطبية اللازمة",
                backstory="أنت وكيل ذكاء اصطناعي مسؤول عن تقديم توصيات للفحوصات والتحاليل الطبية اللازمة. جميع الردود يجب أن تكون باللغة العربية",
                verbose=True,
                allow_delegation=False,
            )
