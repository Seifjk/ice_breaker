from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent

from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Now you can access your environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")
proxycurl_api_key = os.getenv("PROXYCURL_API_KEY")
# information = """
# Elon Reeve Musk (/ˈiːlɒn/ EE-lon; born June 28, 1971) is a business magnate and investor. He is the founder, CEO and chief engineer of SpaceX; angel investor, CEO and product architect of Tesla, Inc.; owner and CTO of Twitter; founder of the Boring Company; co-founder of Neuralink and OpenAI; and president of the philanthropic Musk Foundation. Musk is the wealthiest person in the world, with an estimated net worth, as of July 6, 2023, of around US$248 billion according to the Bloomberg Billionaires Index and $251.1 billion according to Forbes's Real Time Billionaires list, primarily from his ownership stakes in Tesla and SpaceX.[4][5][6]
# """

if __name__ == "__main__":
    print("Hello langchain!")
    linkedin_profile_url = linkedin_lookup_agent(name="Eden Marco")

    summary_template = """
        given the Linkedin information {information} about a person from I want you to create:
        1. a short summary
        2. two interesting facts about them
    """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_profile_url = linkedin_lookup_agent(name="Eden Marco")
    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url=linkedin_profile_url
    )
    print(chain.run(information=linkedin_data))
