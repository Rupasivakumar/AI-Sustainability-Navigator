def assess_impact(category):

    impacts = {

        "Waste Management":
        """
Improper waste disposal can pollute land and water resources,
harm wildlife, and increase greenhouse gas emissions.
        """,

        "Water Management":
        """
Poor water management can lead to water scarcity,
resource depletion, and sanitation issues.
        """,

        "Energy Efficiency":
        """
Excessive energy consumption increases carbon emissions
and contributes to climate change.
        """,

        "Air Quality":
        """
Air pollution negatively affects human health,
causes respiratory diseases, and impacts ecosystems.
        """,

        "Biodiversity Conservation":
        """
Loss of biodiversity weakens ecosystems and threatens
plant and animal species.
        """,

        "Climate Risk":
        """
Climate risks such as floods, droughts, and heatwaves
can affect communities, infrastructure, and livelihoods.
        """
    }

    return impacts.get(
        category,
        "Further impact assessment required."
    )