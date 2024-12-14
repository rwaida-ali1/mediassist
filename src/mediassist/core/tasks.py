from crewai import Task
from textwrap import dedent


def get_tasks(agents, language):
    if language == "en":
        return [
            Task(
                description=dedent(
                    """\
                    Analyze data about types of diabetes.
                    Your final answer MUST be a report that includes:
                    - Overview of the different types of diabetes (Type 1, Type 2, Gestational, and other specific forms).
                    - Key characteristics and differences between each type.
                    - Common causes and risk factors for each type.
                    - Typical symptoms associated with each type.
                    - Diagnostic criteria for each type.
                    - General management and treatment approaches for each type.
                    - Potential complications associated with each type.
                    - Any other relevant information about the types of diabetes.
                    The user input is: {data}
                    Make sure to use the data provided by the user for your analysis.
                """
                ),
                agent=agents["medical_data_agent"],
                expected_output=dedent(
                    """\
                    Comprehensive report on the different types of diabetes, including their characteristics, causes, symptoms, diagnosis, management, and complications."""
                ),
            ),
            Task(
                description=dedent(
                    """\
                    Analyze data about risk factors and symptoms of diabetes.
                    Your final answer MUST be a report that includes:
                    - Comprehensive list of risk factors for developing diabetes, categorized by type (Type 1, Type 2, Gestational).
                    - Detailed explanation of each risk factor and its impact on diabetes development.
                    - Analysis of the user's provided data to identify specific risk factors present.
                    - Comprehensive list of common symptoms associated with diabetes.
                    - Description of each symptom and its potential implications.
                    - Assessment of the user's reported symptoms in relation to the known symptoms of diabetes.
                    - Evaluation of the likelihood of the user having diabetes based on the identified risk factors and symptoms.
                    - Any other relevant information related to risk factors and symptoms of diabetes.
                    The user input is: {data}
                    Make sure to use the data provided by the user for your analysis.
                """
                ),
                agent=agents["medical_data_acquisition_agent"],
                expected_output=dedent(
                    """\
                    Thorough report on risk factors and symptoms of diabetes, including an assessment of the user's specific situation based on the provided data."""
                ),
            ),
            Task(
                description=dedent(
                    """\
                    Preprocess collected medical data for analysis.
                    Your final answer MUST be a report that includes:
                    - Summary of the raw medical data collected from the user.
                    - Description of the data cleaning and preprocessing steps applied.
                    - Explanation of how missing data or inconsistencies were handled.
                    - Transformation of categorical variables into a suitable format for analysis.
                    - Standardization or normalization of numerical data if necessary.
                    - Any other relevant information related to data preprocessing.
                    The user input is: {data}
                    Make sure to use the data provided by the user for your analysis.
                """
                ),
                agent=agents["medical_data_preprocessing_agent"],
                expected_output=dedent(
                    """\
                    Detailed report on the preprocessing steps applied to the medical data, including data cleaning, transformation, and standardization."""
                ),
            ),
            Task(
                description=dedent(
                    """\
                    Provide an initial diagnosis based on preprocessed medical data.
                    Your final answer MUST be a report that includes:
                    - Analysis of the preprocessed medical data to identify potential indicators of diabetes.
                    - Assessment of the user's risk factors and symptoms in relation to the diagnostic criteria for diabetes.
                    - Determination of the likelihood of the user having diabetes based on the available data.
                    - Classification of the potential type of diabetes (Type 1, Type 2, Gestational, or other) if applicable.
                    - Discussion of any differential diagnoses that should be considered.
                    - Any other relevant information related to the initial diagnosis.
                    The user input is: {data}
                    Make sure to use the data provided by the user for your analysis.
                """
                ),
                agent=agents["diagnosis_agent"],
                expected_output=dedent(
                    """\
                    Comprehensive report providing an initial diagnosis of the user's diabetes status based on the preprocessed medical data, including the likelihood and potential type of diabetes."""
                ),
            ),
            Task(
                description=dedent(
                    """\
                    Provide recommendations for necessary medical tests and analyses.
                    Your final answer MUST be a report that includes:
                    - List of recommended medical tests for confirming the diagnosis of diabetes.
                    - Explanation of the purpose and significance of each recommended test.
                    - Prioritization of the tests based on their importance and urgency.
                    - Recommendations for additional analyses or consultations with specialists if necessary.
                    - Guidance on lifestyle modifications or preventive measures based on the user's risk factors.
                    - Any other relevant information related to medical tests, analyses, and recommendations.
                    The user input is: {data}
                    Make sure to use the data provided by the user for your analysis.
                """
                ),
                agent=agents["recommendation_agent"],
                expected_output=dedent(
                    """\
                    Detailed report outlining the recommended medical tests, analyses, and lifestyle modifications for the user based on their specific situation and potential diagnosis."""
                ),
            ),
        ]
    elif language == "ar":
        return [
            Task(
                description=dedent(
                    """\
                    تحليل البيانات حول أنواع مرض السكري.
                    يجب أن يكون ردك النهائي تقريرًا يتضمن:
                    - نظرة عامة على الأنواع المختلفة لمرض السكري (النوع 1، النوع 2، سكري الحمل، وغيرها من الأشكال المحددة).
                    - الخصائص الرئيسية والاختلافات بين كل نوع.
                    - الأسباب الشائعة وعوامل الخطر لكل نوع.
                    - الأعراض النموذجية المرتبطة بكل نوع.
                    - معايير التشخيص لكل نوع.
                    - طرق الإدارة والعلاج العامة لكل نوع.
                    - المضاعفات المحتملة المرتبطة بكل نوع.
                    - أي معلومات أخرى ذات صلة بأنواع مرض السكري.
                    مدخلات المستخدم هي: {data}
                    تأكد من استخدام البيانات التي قدمها المستخدم في تحليلك.
                """
                ),
                agent=agents["medical_data_agent"],
                expected_output=dedent(
                    """\
                    تقرير شامل عن الأنواع المختلفة لمرض السكري، بما في ذلك خصائصها وأسبابها وأعراضها وتشخيصها وإدارتها ومضاعفاتها.
                    جميع الردود يجب أن تكون باللغة العربية"""
                ),
            ),
            Task(
                description=dedent(
                    """\
                    تحليل البيانات حول عوامل الخطر وأعراض مرض السكري.
                    يجب أن يكون ردك النهائي تقريرًا يتضمن:
                    - قائمة شاملة بعوامل الخطر للإصابة بمرض السكري، مصنفة حسب النوع (النوع 1، النوع 2، سكري الحمل).
                    - شرح مفصل لكل عامل خطر وتأثيره على تطور مرض السكري.
                    - تحليل بيانات المستخدم المقدمة لتحديد عوامل الخطر المحددة الموجودة.
                    - قائمة شاملة بالأعراض الشائعة المرتبطة بمرض السكري.
                    - وصف كل عرض وتداعياته المحتملة.
                    - تقييم أعراض المستخدم المبلغ عنها فيما يتعلق بالأعراض المعروفة لمرض السكري.
                    - تقييم احتمالية إصابة المستخدم بمرض السكري بناءً على عوامل الخطر والأعراض المحددة.
                    - أي معلومات أخرى ذات صلة تتعلق بعوامل الخطر وأعراض مرض السكري.
                    مدخلات المستخدم هي: {data}
                    تأكد من استخدام البيانات التي قدمها المستخدم في تحليلك.
                """
                ),
                agent=agents["medical_data_acquisition_agent"],
                expected_output=dedent(
                    """\
                    تقرير شامل عن عوامل الخطر وأعراض مرض السكري، بما في ذلك تقييم لحالة المستخدم المحددة بناءً على البيانات المقدمة.
                    جميع الردود يجب أن تكون باللغة العربية"""
                ),
            ),
            Task(
                description=dedent(
                    """\
                    معالجة البيانات الطبية المجمعة للتحليل.
                    يجب أن يكون ردك النهائي تقريرًا يتضمن:
                    - ملخص للبيانات الطبية الأولية التي تم جمعها من المستخدم.
                    - وصف لخطوات تنظيف البيانات ومعالجتها مسبقًا.
                    - شرح لكيفية التعامل مع البيانات المفقودة أو التناقضات.
                    - تحويل المتغيرات الفئوية إلى تنسيق مناسب للتحليل.
                    - توحيد أو تسوية البيانات الرقمية إذا لزم الأمر.
                    - أي معلومات أخرى ذات صلة تتعلق بالمعالجة المسبقة للبيانات.
                    مدخلات المستخدم هي: {data}
                    تأكد من استخدام البيانات التي قدمها المستخدم في تحليلك.
                """
                ),
                agent=agents["medical_data_preprocessing_agent"],
                expected_output=dedent(
                    """\
                    تقرير مفصل عن خطوات المعالجة المسبقة المطبقة على البيانات الطبية، بما في ذلك تنظيف البيانات وتحويلها وتوحيدها.
                    جميع الردود يجب أن تكون باللغة العربية"""
                ),
            ),
            Task(
                description=dedent(
                    """\
                    تقديم تشخيص مبدئي بناءً على البيانات الطبية المعالجة.
                    يجب أن يكون ردك النهائي تقريرًا يتضمن:
                    - تحليل البيانات الطبية المعالجة مسبقًا لتحديد المؤشرات المحتملة لمرض السكري.
                    - تقييم عوامل الخطر والأعراض لدى المستخدم فيما يتعلق بمعايير تشخيص مرض السكري.
                    - تحديد احتمالية إصابة المستخدم بمرض السكري بناءً على البيانات المتاحة.
                    - تصنيف نوع مرض السكري المحتمل (النوع 1، النوع 2، سكري الحمل، أو غيره) إن أمكن.
                    - مناقشة أي تشخيصات تفاضلية يجب أخذها في الاعتبار.
                    - أي معلومات أخرى ذات صلة تتعلق بالتشخيص الأولي.
                    مدخلات المستخدم هي: {data}
                    تأكد من استخدام البيانات التي قدمها المستخدم في تحليلك.
                """
                ),
                agent=agents["diagnosis_agent"],
                expected_output=dedent(
                    """\
                    تقرير شامل يقدم تشخيصًا أوليًا لحالة مرض السكري لدى المستخدم بناءً على البيانات الطبية المعالجة مسبقًا، بما في ذلك احتمالية الإصابة ونوع مرض السكري المحتمل.
                    جميع الردود يجب أن تكون باللغة العربية"""
                ),
            ),
            Task(
                description=dedent(
                    """\
                    تقديم توصيات للفحوصات والتحاليل الطبية اللازمة.
                    يجب أن يكون ردك النهائي تقريرًا يتضمن:
                    - قائمة بالفحوصات الطبية الموصى بها لتأكيد تشخيص مرض السكري.
                    - شرح لغرض وأهمية كل اختبار موصى به.
                    - تحديد أولويات الاختبارات بناءً على أهميتها وإلحاحها.
                    - توصيات لتحليلات إضافية أو استشارات مع متخصصين إذا لزم الأمر.
                    - إرشادات بشأن تعديلات نمط الحياة أو التدابير الوقائية بناءً على عوامل الخطر لدى المستخدم.
                    - أي معلومات أخرى ذات صلة تتعلق بالاختبارات الطبية والتحاليل والتوصيات.
                    مدخلات المستخدم هي: {data}
                    تأكد من استخدام البيانات التي قدمها المستخدم في تحليلك.
                """
                ),
                agent=agents["recommendation_agent"],
                expected_output=dedent(
                    """\
                    تقرير مفصل يحدد الفحوصات الطبية والتحاليل وتعديلات نمط الحياة الموصى بها للمستخدم بناءً على حالته الخاصة والتشخيص المحتمل.
                    جميع الردود يجب أن تكون باللغة العربية"""
                ),
            ),
        ]
