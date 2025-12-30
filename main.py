from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

load_dotenv()

def main():
    print("Hello from langchain-course!")
    information = """
    Elon Musk
    Elon Reeve Musk (born June 28, 1971) is an engineer, entrepreneur, and business magnate. He holds South African citizenship by birth, Canadian citizenship through his mother, and U.S. citizenship via naturalization in 2002.[1][2][3][4]
    Musk serves as CEO of Tesla and SpaceX, owner of X, and founder of xAI. His early ventures include co-founding Zip2, sold to Compaq in 1999, and X.com, which merged to form PayPal and was acquired by eBay in 2002. He founded Neuralink in 2016 to advance brain-machine interfaces and The Boring Company in 2016 for infrastructure projects.[5][6][7][8][9]
    Musk's net worth, derived primarily from his stakes in Tesla, SpaceX, and xAI, has positioned him as the wealthiest person in the world.[10] His public profile includes advocacy for innovation, population growth, reduced government intervention, free speech, and political involvement.[11]
    """
    summary_template = """
    Given the information {information}, about a person. I want you to create:
    1. A short summary
    2. Two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(template=summary_template, input_variables=["information"])

    llm = ChatOpenAI(model="gpt-5", temperature=0)
    #lmm = ChatOllama(temperature=0, model="gemma3:270m")
    chain = summary_prompt_template | llm
    response = chain.invoke({"information": information})
    print(response.content)

if __name__ == "__main__":
    main()
