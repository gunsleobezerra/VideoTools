import g4f

def get_completion(prompt:str):
    allowed_models = [
    'code-davinci-002',
    'text-ada-001',
    'text-babbage-001',
    'text-curie-001',
    'text-davinci-002',
    'text-davinci-003'
]

    response = g4f.Completion.create(
        model  = 'text-davinci-003',
        prompt = prompt)
    
    return  str(response)




