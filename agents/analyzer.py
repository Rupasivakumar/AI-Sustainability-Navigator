def analyze_issue(issue):

    issue = issue.lower()

    # Waste Management
    if any(word in issue for word in [
        "waste", "garbage", "plastic", "trash",
        "litter", "dumping", "recycling"
    ]):

        return {
            "category": "Waste Management",
            "sdgs": "SDG 11, SDG 12, SDG 13",
            "impact": "Potential pollution and environmental degradation.",
            "severity": "High"
        }

    # Water Management
    elif any(word in issue for word in [
        "water", "leak", "leakage",
        "river", "lake", "groundwater",
        "drainage", "sanitation"
    ]):

        return {
            "category": "Water Management",
            "sdgs": "SDG 6, SDG 11, SDG 13",
            "impact": "Water wastage and resource depletion.",
            "severity": "Medium"
        }

    # Energy Efficiency
    elif any(word in issue for word in [
        "energy", "electricity", "light",
        "power", "fuel", "renewable",
        "solar", "battery"
    ]):

        return {
            "category": "Energy Efficiency",
            "sdgs": "SDG 7, SDG 11, SDG 13",
            "impact": "Increased energy consumption and carbon emissions.",
            "severity": "Medium"
        }

    # Air Quality
    elif any(word in issue for word in [
        "air pollution", "smoke", "emission",
        "vehicle", "factory", "dust",
        "pollution", "air quality"
    ]):

        return {
            "category": "Air Quality",
            "sdgs": "SDG 3, SDG 11, SDG 13",
            "impact": "Negative effects on public health and the environment.",
            "severity": "High"
        }

    # Biodiversity
    elif any(word in issue for word in [
        "forest", "tree", "wildlife",
        "animal", "biodiversity",
        "species", "deforestation"
    ]):

        return {
            "category": "Biodiversity Conservation",
            "sdgs": "SDG 15, SDG 13",
            "impact": "Loss of ecosystems and biodiversity.",
            "severity": "High"
        }

    # Climate Risk
    elif any(word in issue for word in [
        "flood", "heatwave", "drought",
        "climate", "storm",
        "extreme weather"
    ]):

        return {
            "category": "Climate Risk",
            "sdgs": "SDG 13, SDG 11",
            "impact": "Increased vulnerability to climate-related disasters.",
            "severity": "High"
        }

    else:

        return {
            "category": "General Sustainability Issue",
            "sdgs": "SDG 11, SDG 12, SDG 13",
            "impact": "Further assessment required.",
            "severity": "Low"
        }