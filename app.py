import gradio as gr
import llm_agents as LLMAgents

model_choices=['meta/llama3-70b-instruct','meta/llama3-8b-instruct']

# Gradio UI setup
with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column(scale=4):
            user_text = gr.Textbox(placeholder="Write your question here", label="User input")
            model_output = gr.Textbox(label="Model output", lines=10, interactive=False)
            button_submit = gr.Button(value="Submit")

        with gr.Column(scale=1):
            """max_new_tokens = gr.Slider(minimum=1, maximum=1000, value=250, step=1, label="Max New Tokens")
            top_p = gr.Slider(minimum=0.05, maximum=1.0, value=0.95, step=0.05, label="Top-p (nucleus sampling)")
            top_k = gr.Slider(minimum=1, maximum=50, value=50, step=1, label="Top-k")"""
            temperature = gr.Slider(minimum=0.1, maximum=1.0, value=0.5, step=0.1, label="Temperature")
            model = gr.Dropdown(choices=model_choices, multiselect=False, label="Select Model")
            
    user_text.submit(LLMAgents.get_llm_agent_response, [user_text,model, temperature], model_output)
    button_submit.click(LLMAgents.get_llm_agent_response, [user_text,model, temperature], model_output)

    demo.queue(max_size=32).launch(server_port=8082)



