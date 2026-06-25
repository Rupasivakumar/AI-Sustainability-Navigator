import gradio as gr

from agents.analyzer import analyze_issue
from agents.sdg_mapper import map_sdg
from agents.impact_assessor import assess_impact
from agents.action_planner import generate_actions

from rag.retriever import retrieve_knowledge

from reports.report_generator import generate_report


def process_issue(issue):

    analysis = analyze_issue(issue)

    category = analysis["category"]
    severity = analysis["severity"]

    sdgs = map_sdg(category)

    knowledge = retrieve_knowledge(category)

    impact = assess_impact(category)

    actions = generate_actions(category)

    sustainability_score = {
        "High": 40,
        "Medium": 70,
        "Low": 90
    }.get(severity, 50)

    pdf_file = generate_report(
        issue,
        category,
        severity,
        sustainability_score,
        sdgs,
        impact,
        actions
    )

    return (
        category,
        severity,
        sustainability_score,
        sdgs,
        knowledge,
        impact,
        actions,
        pdf_file
    )


with gr.Blocks(
    title="AI Sustainability Navigator",
    css_paths=["assets/custom.css"]
) as app:

    gr.HTML("""
    <div class="hero">
        <h1>🌍 AI Sustainability Navigator</h1>
        <p>Agentic AI Platform for Community Sustainability Analysis</p>
        <p>Analyze • Assess • Act • Sustain</p>
    </div>
    """)

    with gr.Tab("📊 Analysis"):

        issue_input = gr.Textbox(
            lines=4,
            label="Describe Sustainability Issue",
            placeholder="Example: Plastic waste accumulating near a lake"
        )

        analyze_btn = gr.Button(
            "🔍 Analyze Issue",
            variant="primary"
        )

        category_output = gr.Textbox(
            label="Issue Category"
        )

        severity_output = gr.Textbox(
            label="Severity"
        )

        score_output = gr.Slider(
            minimum=0,
            maximum=100,
            label="🌍 Sustainability Score",
            interactive=False
        )

    with gr.Tab("🎯 SDG Mapping"):

        sdg_output = gr.Textbox(
            label="Mapped Sustainable Development Goals",
            lines=8
        )

    with gr.Tab("📚 Knowledge Base"):

        knowledge_output = gr.Textbox(
            label="Retrieved Sustainability Knowledge",
            lines=15
        )

    with gr.Tab("🌱 Impact Assessment"):

        impact_output = gr.Textbox(
            label="Environmental Impact"
        )

    with gr.Tab("📋 Action Plan"):

        action_output = gr.Textbox(
            label="Recommended Actions",
            lines=10
        )

        report_output = gr.File(
            label="📄 Download Sustainability Report"
        )

    analyze_btn.click(
        fn=process_issue,
        inputs=issue_input,
        outputs=[
            category_output,
            severity_output,
            score_output,
            sdg_output,
            knowledge_output,
            impact_output,
            action_output,
            report_output
        ]
    )

app.launch(share=True)