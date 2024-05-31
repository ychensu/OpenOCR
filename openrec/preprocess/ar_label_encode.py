import numpy as np

from openrec.preprocess.ctc_label_encode import BaseRecLabelEncode


class ARLabelEncode(BaseRecLabelEncode):
    """Convert between text-label and text-index."""

    BOS = '<s>'
    EOS = '</s>'
    PAD = '<pad>'

    def __init__(self,
                 max_text_length,
                 character_dict_path=None,
                 use_space_char=False,
                 **kwargs):
        super(ARLabelEncode,
              self).__init__(max_text_length, character_dict_path,
                             use_space_char)

    def __call__(self, data):
        text = data['label']
        text = self.encode(text)
        if text is None:
            return None
        data['length'] = np.array(len(text))
        text = [self.dict[self.BOS]] + text + [self.dict[self.EOS]]
        text = text + [self.dict[self.PAD]
                       ] * (self.max_text_len + 2 - len(text))
        data['label'] = np.array(text)
        return data

    def add_special_char(self, dict_character):
        dict_character = [self.EOS] + dict_character + [self.BOS, self.PAD]
        return dict_character
