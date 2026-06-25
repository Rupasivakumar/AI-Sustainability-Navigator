def map_sdg(category):

    mapping = {

        "Waste Management":
        """
🏙 SDG 11 – Sustainable Cities & Communities

♻ SDG 12 – Responsible Consumption & Production

🌍 SDG 13 – Climate Action
        """,

        "Water Management":
        """
💧 SDG 6 – Clean Water & Sanitation

🏙 SDG 11 – Sustainable Cities & Communities

🌍 SDG 13 – Climate Action
        """,

        "Energy Efficiency":
        """
⚡ SDG 7 – Affordable & Clean Energy

🏙 SDG 11 – Sustainable Cities & Communities

🌍 SDG 13 – Climate Action
        """,

        "Air Quality":
        """
❤️ SDG 3 – Good Health and Well-Being

🏙 SDG 11 – Sustainable Cities & Communities

🌍 SDG 13 – Climate Action
        """,

        "Biodiversity Conservation":
        """
🌳 SDG 15 – Life on Land

🌍 SDG 13 – Climate Action
        """,

        "Climate Risk":
        """
🌍 SDG 13 – Climate Action

🏙 SDG 11 – Sustainable Cities & Communities
        """
    }

    return mapping.get(
        category,
        "🌍 General Sustainability Goals"
    )