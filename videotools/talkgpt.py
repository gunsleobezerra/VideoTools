import g4f


    


def get_completion(prompt:str):
    # streamed completion
    response=""
    

    

    # normal response
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4_32k_0613,
        messages=[{"role": "user", "content": prompt}],
    )  # alternative model setting

    
    return response
