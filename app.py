import os
from google import genai
from google.genai import types
import gradio as gr
from dotenv import load_dotenv
load_dotenv()

client=genai.Client(api_key=os.getenv("GENAI_CLIENT_KEY"))
BASE_PROMPT = """
Your primary goal is to teach concepts clearly and thoroughly.

For every educational question:

- Start with a definition.
- Explain why it is needed.
- Explain how it works step by step.
- Use examples.
- Use analogies.
- Include code examples when appropriate.
- Mention advantages and disadvantages.
- Mention real-world applications.
- Summarize the key points.
- Ask one follow-up question.

Do not give short answers unless explicitly requested.
"""

personalities = {
    "Friendly": f"""
{BASE_PROMPT}

Use a friendly, conversational, enthusiastic, and encouraging tone.
Imagine you are teaching a friend who is completely new to the subject.
""",

    "Academic": f"""
{BASE_PROMPT}

Use a professional, structured, university-professor style.
Use precise technical terminology while ensuring every important concept is explained clearly.
"""
}

def study_assistant(question,persona):
  system_prompt=personalities[persona]
  response=client.models.generate_content(
      model="gemini-3.5-flash",
      config=types.GenerateContentConfig(
          system_instruction=system_prompt,
          temperature=0.7,
          max_output_tokens=2048
          ),
      contents=question,
      )
  return response.text

demo=gr.Interface(
    fn=study_assistant,
    inputs=[gr.Textbox(label="Question",lines=4,placeholder="Ask a question..."),
            gr.Radio(choices=list(personalities.keys()),value="Friendly",label="Personality")
            ],
    outputs=gr.Textbox(label="Explanation",lines=10),
    title="Study Assistant",
    description="Ask a question to get simple explanation from AI along with simple analogies and real world examples"
)
demo.launch(debug=True)