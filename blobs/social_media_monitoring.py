def run(state):
    """Simulate monitoring social media for additional reports of the weather event."""
    simulated_reports = [
        "Local reports of rising water levels and minor flooding.",
        "High winds causing power outages in parts of the city.",
        "Citizens reporting high temperatures and increased heat discomfort.",
        "Social media reports indicate severe storm damage in local infrastructure.",
        "Reports of traffic disruptions due to heavy rain.",
        "No unusual social media reports related to the weather at this time."
    ]

    social_media_report = random.choice(simulated_reports)
    return {
        **state,
        "social_media_reports": state["social_media_reports"] + [social_media_report],
        "messages": state["messages"] + [SystemMessage(content=f"Social media report added: {social_media_report}")]
    }