import re
class SimpleTokenizerV1:
    def __init__(self, vocab):
         self.str_to_int = vocab
         self.int_to_str = {i:s for s, i in vocab.items()}

    def encode(self, text):
        pre_processed = re.split(r'([,.:;?_!"()\']|--|\s)', text)
        pre_processed = [
            item.strip() for item in pre_processed if item.strip()
        ]

        ids = [self.str_to_int[s] for s in pre_processed]
        return ids


    def decode(self, token_ids):
        text = " ".join([self.int_to_str[id] for id in token_ids])
        text = re.sub(r'\s+([,.?!"()\'])', r'\1', text)
        return text