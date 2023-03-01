from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

class MLModel:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("microsoft/GODEL-v1_1-base-seq2seq")
        self.model = AutoModelForSeq2SeqLM.from_pretrained("microsoft/GODEL-v1_1-base-seq2seq")

    def predict(self, input):
        instruction = 'Instruction: given a dialog context, you need to response empathically'
        knowledge = '  '
        history = []

        s = list(sum(history, ()))
        s.append(input)
        dialog = ' EOS ' .join(s)
        #print(dialog)

        query = f"{instruction} [CONTEXT] {dialog} {knowledge}"

        top_p = 0.9
        min_length = 8
        max_length = 64


        # tokenize the new input sentence
        new_user_input_ids = self.tokenizer.encode(f"{query}", return_tensors='pt')


        output = self.model.generate(new_user_input_ids, min_length=int(
            min_length), max_length=int(max_length), top_p=top_p, do_sample=True).tolist()


        response = self.tokenizer.decode(output[0], skip_special_tokens=True)
        #history.append((input, response))
        history.append(response)
        return history
