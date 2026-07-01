
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.7
)

prompt=PromptTemplate(
    template="""
    You are an expert language assistant for a sign language communication system.

The input consists of words detected from sign language gestures. These words may be unordered, incomplete, or grammatically incorrect.

Your job is to:
- Understand the intended meaning.
- Convert the words into a natural conversational sentence.
- Add missing articles, prepositions, and connecting words when needed.
- Keep the original intent unchanged.
- Return only the final sentence.

Detected Words:
{detected_words}

Natural Sentence:

    """
    ,
    input_variables=["detected_words"]
)

parser=StrOutputParser()



chain=prompt|llm|parser



list=["help", "need", "hospital"]
#making the senntece of the array
def make_sentence(list):
  sentence=""
  for word in list:
    sentence+=word+" "




  return sentence



def output(list):
   result=chain.invoke({"detected_words":make_sentence(list)})
   return result
 

print(output(['hello', 'thanks', 'yes']))









