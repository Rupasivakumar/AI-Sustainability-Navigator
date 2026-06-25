import os

# Knowledge base mapped to categories
KNOWLEDGE_BASE = {
    "Air Quality": [
        "Air pollution causes respiratory diseases including asthma, bronchitis, and lung cancer.",
        "PM2.5 particles penetrate deep into lungs and enter the bloodstream, causing cardiovascular damage.",
        "Schools near high-traffic roads show 30% higher rates of childhood asthma.",
        "Clean Air Act regulations have reduced US air pollution by 78% since 1970.",
        "Indoor air quality can be 2-5x worse than outdoor air due to trapped pollutants.",
        "Trees and green spaces reduce urban air pollution by absorbing CO2 and particulates.",
        "Electric vehicles can reduce local air pollution by up to 70% compared to petrol cars.",
        "WHO guidelines recommend PM2.5 levels below 15 micrograms per cubic meter annually."
    ],
    "Waste Management": [
        "Only 9% of all plastic ever produced has been recycled globally.",
        "Plastic waste in oceans harms over 800 marine species through entanglement and ingestion.",
        "Landfills produce methane, a greenhouse gas 25x more potent than CO2.",
        "Composting organic waste reduces landfill methane emissions by up to 50%.",
        "A single plastic bottle takes 450 years to decompose in a landfill.",
        "Recycling one ton of paper saves 17 trees and 7,000 gallons of water.",
        "Zero-waste communities divert over 90% of waste from landfills through recycling and composting.",
        "Extended Producer Responsibility (EPR) laws make manufacturers responsible for product end-of-life."
    ],
    "Water Management": [
        "Over 2 billion people lack access to safe drinking water globally.",
        "Agriculture accounts for 70% of global freshwater withdrawals.",
        "Water pollution from industrial runoff affects aquatic ecosystems and human health.",
        "Drip irrigation can reduce agricultural water use by 30-50% compared to flood irrigation.",
        "Rainwater harvesting can supply 50-100% of household non-potable water needs.",
        "Wetlands act as natural water filters, removing up to 90% of water pollutants.",
        "Groundwater depletion threatens food security in regions like South Asia and the Middle East.",
        "Grey water recycling for irrigation can reduce household water consumption by 30%."
    ],
    "Energy Efficiency": [
        "Buildings account for 40% of global energy consumption and 33% of greenhouse gas emissions.",
        "LED lighting uses 75% less energy than incandescent bulbs and lasts 25x longer.",
        "Solar panel costs have fallen by 89% in the last decade, making renewable energy affordable.",
        "Smart thermostats reduce heating and cooling energy use by 10-15% on average.",
        "Energy-efficient appliances can cut household electricity bills by up to 30%.",
        "Passive house design reduces heating energy demand by up to 90% compared to standard buildings.",
        "Community solar programs allow renters to access renewable energy without rooftop installation.",
        "Industrial energy audits typically identify 10-20% energy savings opportunities."
    ],
    "Biodiversity": [
        "One million plant and animal species are currently threatened with extinction.",
        "Deforestation destroys 10 million hectares of forest annually, eliminating critical habitat.",
        "Pollinators like bees contribute $235-577 billion to global food production annually.",
        "Urban green corridors allow wildlife movement between fragmented natural habitats.",
        "Invasive species are the second leading cause of biodiversity loss worldwide.",
        "Marine protected areas increase fish biomass by 600% compared to unprotected zones.",
        "Native plant gardens support 4x more wildlife than gardens with non-native species.",
        "Rewilding projects restore ecosystem functions and increase local species diversity by 50%."
    ],
    "Climate Risk": [
        "Global temperatures have risen 1.1 degrees Celsius above pre-industrial levels.",
        "Extreme weather events have increased 5x in frequency over the past 50 years.",
        "Sea level rise threatens 1 billion people living in coastal and low-lying areas.",
        "Climate change could displace 216 million people within their own countries by 2050.",
        "Urban heat islands make cities 1-7 degrees Celsius hotter than surrounding rural areas.",
        "Nature-based solutions can provide 30% of cost-effective climate mitigation needed by 2030.",
        "Climate adaptation investments yield $4-$36 in economic benefits for every $1 spent.",
        "Carbon pricing mechanisms have reduced emissions by 15-20% in regions where implemented."
    ]
}

# Keyword to category mapping for flexible matching
KEYWORD_MAP = {
    "air": "Air Quality",
    "pollution": "Air Quality",
    "smoke": "Air Quality",
    "dust": "Air Quality",
    "emission": "Air Quality",
    "smog": "Air Quality",
    "fume": "Air Quality",
    "exhaust": "Air Quality",

    "waste": "Waste Management",
    "plastic": "Waste Management",
    "trash": "Waste Management",
    "garbage": "Waste Management",
    "litter": "Waste Management",
    "dump": "Waste Management",
    "landfill": "Waste Management",
    "recycle": "Waste Management",
    "rubbish": "Waste Management",

    "water": "Water Management",
    "river": "Water Management",
    "lake": "Water Management",
    "flood": "Water Management",
    "drain": "Water Management",
    "sewage": "Water Management",
    "ocean": "Water Management",
    "sea": "Water Management",
    "groundwater": "Water Management",

    "energy": "Energy Efficiency",
    "electricity": "Energy Efficiency",
    "solar": "Energy Efficiency",
    "power": "Energy Efficiency",
    "fuel": "Energy Efficiency",
    "carbon": "Energy Efficiency",
    "greenhouse": "Energy Efficiency",

    "biodiversity": "Biodiversity",
    "wildlife": "Biodiversity",
    "forest": "Biodiversity",
    "tree": "Biodiversity",
    "species": "Biodiversity",
    "animal": "Biodiversity",
    "plant": "Biodiversity",
    "habitat": "Biodiversity",
    "ecosystem": "Biodiversity",

    "climate": "Climate Risk",
    "temperature": "Climate Risk",
    "heat": "Climate Risk",
    "storm": "Climate Risk",
    "drought": "Climate Risk",
    "disaster": "Climate Risk",
    "risk": "Climate Risk"
}


def retrieve_knowledge(category_or_issue: str) -> str:
    """
    Retrieve knowledge for a given category name OR a raw issue description.
    Works even if the category has emojis or extra whitespace.
    """
    if not category_or_issue:
        return _fallback()

    text = category_or_issue.strip()

    # 1. Direct category match (strip emojis/symbols first)
    clean_text = ''.join(c for c in text if c.isalpha() or c.isspace()).strip()
    for key in KNOWLEDGE_BASE:
        if key.lower() in clean_text.lower() or clean_text.lower() in key.lower():
            return _format(key)

    # 2. Keyword match against the full input text
    lower = text.lower()
    for keyword, cat in KEYWORD_MAP.items():
        if keyword in lower:
            return _format(cat)

    # 3. Fallback — return all categories summary
    return _fallback()


def _format(category: str) -> str:
    facts = KNOWLEDGE_BASE.get(category, [])
    lines = [f"Knowledge Base: {category}", "=" * 40]
    for i, fact in enumerate(facts, 1):
        lines.append(f"{i}. {fact}")
    return "\n".join(lines)


def _fallback() -> str:
    lines = ["General Sustainability Knowledge", "=" * 40]
    for cat, facts in KNOWLEDGE_BASE.items():
        lines.append(f"\n[{cat}]")
        lines.append(facts[0])
    return "\n".join(lines)