from langchain_core.prompts import PromptTemplate # type: ignore
from langchain.chat_models import ChatOpenAI # type: ignore

import pandas as pd # type: ignore
import json
import os

OPENAI_API_KEY = os.environ['OPENAI_API_KEY']

def question_generator(df):
    template = """
        You are an expert question writer. 
        Given the following question, please generate two variants of the question that are 
        similar in difficulty and assess the same knowledge.
        Generate the variants in json format with keys "variant1" and "variant2".

        Original Question: {question}

        """
    prompt = PromptTemplate(
    input_variables=["question"],
    template=template,)

    # Initialize the ChatOpenAI model for question generation
    model = ChatOpenAI(temperature=0)
    chain = prompt | model

    variant1 =[]
    variant2 = []
    
    for index, row in df.iterrows():
        response = chain.invoke(row['question'])
        response_json = json.loads(response.content)
        variant1.append(response_json.get('variant1'))
        variant2.append(response_json.get('variant2'))

    df['variant1'] = variant1
    df['variant2'] = variant2
    return df

