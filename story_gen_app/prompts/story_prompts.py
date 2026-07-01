from langchain_core.prompts import PromptTemplate



def createPrompt():
    prompt=PromptTemplate(
        template="""You are an expert creative story writer and novelist.

Generate a **{length}** **{genre}** story in **simple, engaging, and easy-to-understand language**.

### Story Details

* **Main Character:** {character}
* **Setting:** {setting}
* **Tone:** {tone}
* **Story Idea:** {user_prompt}
* **Generate the complete story in {language} language.
Use natural grammar and vocabulary appropriate for that language:** 



### Instructions

1. Generate a **creative and catchy title**.
2. Divide the story into the following sections:

   * **Introduction**
   * **Rising Action**
   * **Climax**
   * **Conclusion**
3. Use short and well-formatted paragraphs.
4. Keep the language simple and natural.
5. Make the story immersive with vivid descriptions and meaningful dialogues where appropriate.
6. Maintain consistency in characters, setting, and storyline.
7. Ensure the ending is satisfying and matches the selected tone.
8. Avoid repeating the same information or sentences.
9. The story should feel original and creative.
10. Format the output exactly as shown below.

# 📖 Title

<Story Title>

---

## 🌟 Introduction

<Introduction>

---

## ⚔️ Rising Action

<Main events and conflict>

---

## 🔥 Climax

<Most exciting part of the story>

---

## 🌈 Conclusion

<Ending of the story>

---

### ✨ Moral (Optional)

<A short moral or lesson if suitable for the story>

Generate only the formatted story without any explanations or extra text.


""",
        input_variables=["genre","tone","length","character","setting","user_prompt","language"]
    )
    return prompt