import subprocess

def cultural_chat(prompt):
    result = subprocess.run(["ollama", "run", "phi3", prompt], capture_output=True, text=True)
    return result.stdout.strip()
