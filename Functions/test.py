# import openai
# from decouple import config

# OPENAIGPT3_API_KEY = config('openai_API_KEY')


# def openaiGPT3():
#     # set the API key for OpenAI's GPT-3 API
#     openai.api_key = OPENAIGPT3_API_KEY

#     query = "Who is elon musk?"
#     # create a completion request using the GPT-3 API
#     response = openai.Completion.create(
#         # specify the engine to use
#         engine="text-davinci-002",
#         # The prompt to generate a response for
#         prompt=query,
#         # set the temperature to control the randomness of the response
#         temperature=0.1,
#         # set the maximum number of tokens to generate, , By setting max_tokens to a certain value, you can limit the length of the generated text.
#         # Here we set it to 256 that means the API will return a maximum of 256 tokens in its response.
#         max_tokens=256,
#         # set the top-p value to control the proportion of the response that comes from the model
#         top_p=1,
#         # set the number of different completions to generate
#         best_of=2,
#         # set the frequency penalty to control the balance between generating novel words and using common words
#         frequency_penalty=0.4,
#         # set the presence penalty to encourage the model to generate words that were in the prompt
#         presence_penalty=0.3)
#     # get the text of the first choice
#     answer = response['choices'][0]['text']
#     # return the answer
#     print(answer)


# openaiGPT3()
