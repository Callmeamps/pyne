from js import document
from pyodide.ffi import create_proxy
#import langchain

prompt_list = []

def add_prompt(prompt):
    prompt_list.append(prompt)
    
def write_prompts(prompts):
    if prompts isinstance(prompts, List):
        for prompt in prompts:
            add_prompt(prompt)
            pyscript.write(prompt)
    else:
        add_prompt(prompts)
        pyscript.write(prompts)

add_new_prompt = create_proxy(add_prompt)
print_prompts = create_proxy(write_prompts)
prompt_area = document.getElementById("input_area")
send_btn = document.getElementById("sendBtn")

send_btn.addEventListener("click", print_prompts)
