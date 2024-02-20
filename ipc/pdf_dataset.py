#to get all the description data from the pdf this functions are used

from openai import OpenAIError
import openai

openai.api_key = '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'


class OpenAIServiceForPdf:
    @staticmethod
    def get_patent_ideas_pdf(ipc_symbols, engine="gpt-3.5-turbo-instruct"):
        descriptions = {}
        for symbol in ipc_symbols:
            prompt = f"Explain in short lines the IPC symbol {ipc_symbols} in the context of patent classification."
            response = openai.Completion.create(engine=engine, prompt=prompt, max_tokens=200)
            descriptions[symbol] = response.choices[0].text.strip()
        return descriptions

    # ipc_symbols = ["A01N 33/00", "H01L 31/0216"]  # Example IPC symbols from IPAMAS
    # ipc_descriptions = OpenAIService.get_patent_ideas(ipc_symbols)
    # print(ipc_descriptions, '------ipc_descriptions----')

    # def fetch_ipc_descriptions(ipc_symbols):
    #     descriptions = {}
    #     for symbol in ipc_symbols:
    #         response = openai.Completion.create(
    #             engine="davinci",
    #             prompt=f"Explain the IPC symbol {symbol} in the context of patent classification.",
    #             max_tokens=100
    #         )
    #         descriptions[symbol] = response.choices[0].text.strip()
    #     return descriptions

    # ipc_symbols = ["A01N 33/00", "H01L 31/0216"]  # Example IPC symbols from IPAMAS
    # ipc_descriptions = fetch_ipc_descriptions(ipc_symbols)
    # print(ipc_symbols,'------ipc_symbols----')

    def generate_market_overview(field_of_invention):
        prompt = f"Provide a market overview for the {field_of_invention} industry, including trends, size, and growth potential with this headings ."
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=700
        )
        market_overview = response.choices[0].text.strip()
        return market_overview

    #
    #
    # field_of_invention = "solar energy innovations"  # Example field from IPAMAS
    # market_overview = generate_market_overview(field_of_invention)
    # print(market_overview,'------market_overview-----')

    def generate_innovative_component(field_of_invention):
        prompt = f"Provide Innovative Components for the {field_of_invention}."
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=200
        )
        innovative_component = response.choices[0].text.strip()
        return innovative_component

    def generate_potential_application(field_of_invention):
        prompt = f"Provide Potential Components for the {field_of_invention}."
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=200
        )
        potential_application = response.choices[0].text.strip()
        return potential_application

    def ip_protection_strategies(field_of_invention):
        prompt = f"Provide IP Protection Strategies for the {field_of_invention}."
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=200
        )
        ipc_protection = response.choices[0].text.strip()
        return ipc_protection

    #
    def licensing_opportunities(field_of_invention):
        prompt = f"Provide Licensing Opportunities for the {field_of_invention}."
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=200
        )
        licensing_opportunities = response.choices[0].text.strip()
        return licensing_opportunities

    def future_directions(field_of_invention):
        prompt = f"Provide Future R&D Directions for the {field_of_invention}."
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=200
        )
        furure_opportunities = response.choices[0].text.strip()
        return furure_opportunities

    def collaboration_opportunities(field_of_invention):
        prompt = f"Provide Collaboration Opportunities for the {field_of_invention}."
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=200
        )
        collab = response.choices[0].text.strip()
        return collab

    def glossary_terms(field_of_invention):
        prompt = f"Provide Glossary of Terms for the {field_of_invention}."
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=200
        )
        terms = response.choices[0].text.strip()
        return terms
    
    def target_market_segments(field_of_invention):
        prompt = f"Provide Target Market Segments for the {field_of_invention}."
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=180
        )
        segments = response.choices[0].text.strip()
        return segments
    
    def enhanced_ipc_analysis(field_of_invention):
        prompt = f"Provide Enhanced IPC Analysis for the {field_of_invention}."
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=200
        )
        analysis = response.choices[0].text.strip()
        return analysis

    def regulatory_landscape(field_of_invention):
        prompt = f"Provide Regulatory Landscape for the {field_of_invention}."
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=200
        )
        landscape = response.choices[0].text.strip()
        return landscape

    def compliance_requirements(field_of_invention):
        prompt = f"Provide Compliance Requirements for the {field_of_invention}."
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=200
        )
        compliance = response.choices[0].text.strip()
        return compliance

    def abstract(field_of_invention):
        prompt = f"Provide Abstract for the {field_of_invention}."
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=170
        )
        abstract = response.choices[0].text.strip()
        return abstract
    
    def reference(field_of_invention):
        prompt = f"Provide References and Links for the {field_of_invention}."
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=200
        )
        reference = response.choices[0].text.strip()
        return reference

