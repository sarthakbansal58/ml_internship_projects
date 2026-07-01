import os
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from prompts.story_prompts import createPrompt
from langchain_core.runnables import RunnableSequence
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()

# llm=HuggingFaceEndpoint(
#     repo_id="deepseek-ai/DeepSeek-V4-Pro",
#     temperature=0.9,
#     # task="conversational",
#     huggingfacehub_api_token=os.getenv("HUGGINGFACE_API")
# )

llm=ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_GEMINI_API"),
    temperature=0.9    
)


# model=ChatHuggingFace(llm=llm)
parser=StrOutputParser()




def generateStory(genre,tone,length,character,setting,user_prompt,language):

    prompt=createPrompt()

    chain=RunnableSequence(prompt,llm,parser)


    try:
        response=chain.invoke({
        "genre":genre,
        "tone":tone,
        "length":length,
        "character":character,
        "setting":setting,
        "user_prompt":user_prompt,
        "language":language
        })
        return response
    except Exception as e:
        return f"Error is {str(e)}"




# print(os.getenv("HUGGINGFACE_API"))

    



