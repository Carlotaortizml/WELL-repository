from transformers import AutoModelWithLMHead, AutoModelForCausalLM, AutoTokenizer
import torch

class DialoGPTModel:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("/DialoGPT-small")
        self.model = AutoModelForCausalLM.from_pretrained("/DialoGPT-small")

    def predict_new(self, user_input):
        new_user_input_ids = self.tokenizer.encode(user_input + self.tokenizer.eos_token, return_tensors='pt')

        for step in range(12):
            bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids

            chat_history_ids = self.model.generate(
                new_user_input_ids, max_length=200,
                pad_token_id=self.tokenizer.eos_token_id,
                no_repeat_ngram_size=3,
                do_sample=True,
                top_k=100,
                top_p=0.7,
                temperature=0.4
            )

            #output = self.tokenizer.decode(chat_history_ids[0])
            output = self.tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
            print(chat_history_ids[:, bot_input_ids.shape[-1]:][0])
            return output

    def predict(self, user_input):
        new_user_input_ids = self.tokenizer.encode(user_input + self.tokenizer.eos_token, return_tensors='pt')

        for step in range(12):
            bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids

            chat_history_ids = self.model.generate(
                new_user_input_ids, max_length=200,
                pad_token_id=self.tokenizer.eos_token_id,
                no_repeat_ngram_size=3,
                do_sample=True,
                top_k=100,
                top_p=0.7,
                temperature=0.4
            )

            #output = self.tokenizer.decode(chat_history_ids[0])
            output = self.tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
            return output

    def generate_response(self):
        # Let's chat for 4 lines
        for step in range(50):
            # encode the new user input, add the eos_token and return a tensor in Pytorch
            new_user_input_ids = self.tokenizer.encode(input(">> User:") + self.tokenizer.eos_token, return_tensors='pt')
            # print(new_user_input_ids)

            # append the new user input tokens to the chat history
            bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids

            # generated a response while limiting the total chat history to 1000 tokens,
            chat_history_ids = self.model.generate(
                bot_input_ids, max_length=200,
                pad_token_id=self.tokenizer.eos_token_id,
                no_repeat_ngram_size=3,
                do_sample=True,
                top_k=100,
                top_p=0.7,
                temperature=0.4
            )
            # pretty print last ouput tokens from bot
            print("Therapist: {}".format(self.tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)))

if __name__=='__main__':
    DialoGPTModel.generate_response
