from english_words import get_english_words_set
from collections import defaultdict
from collections import OrderedDict


class FindWords:
    def __init__(self):
        self.word_list = get_english_words_set(['web2'], lower=True)
        self.word_rows = [
            'JGLOMGKOMSDOEOVMSCMWOOPRYTLSMLFJOMCES',
            'KOGJKLMSMIEOPJMISMMGKEJSKNMLESSONSJAPQ',
            'PEICREATIONJMXLAMFAJFLSMCGJIWLOVEPJFLAMVL',
            'WILFEGMLEMFMEPABNZLSHUMUOKUITEWJIKOKNV',
            'MSNGKDSLJGKDLSJGKLSGRATITUDEJGKLSJAKLGZV',
            'NMCNSJWUODLOPWSJGOSKIEMNBSKGMNBAXBOMSII',
            'IMELNGSANVOCONNECTIONKMGEWJNNZCMANHHEL',
            'NOIRPWIOTYIEJCZXNMXZVJSAGKSMZNVLGKELJWJK',
            'INSNJOORWADEXCRPWVGCRBYTHMONEYKUMLIMLY',
            'UJURNWCGEYVOPOWERPUYXORWKLJOSKLGJNDSLJI',
            'TALIGNMENTJEMSLJJFLSHAHMLFJELWPORIMSMM',
            'TGLDMGKDMSIOMCHANGEVVMSCMWOOPRYTLSMLFJ',
            '¡IMCESKOGJKLMSMIEOPJMLSMVMGKEJSKNMJAPOPE',
            'OOMXLAMFAHEALTHOFLSMCGJIWPJFLAMVLWILFEGM',
            'NNMFMEPAVBNZLSNMJOKUISELFCAREVMSNGKDSL',
            'JGMDLSJGKLSJGKLSJAKLGZUNMCNSJWUODLOPWSJ',
            'GDSKIEMNBSKGMNBAXBDMSGMELNGSANVDSMGEW',
            'JNNZCMANHHFLSTRENGTHWOIRPWIOTYIEJCZINMR',
            'ZVJSAGKSMZNVLGKELJWJKCNSNFAMILYUDORWADE',
            'XCRSWVGCRBYTNKUMLIMLYBJVRNWCGEYVOXDRWS',
            'LUDSKLWPURPOSEJKDSLJEMJGLDMGKOMSDOEOVM',
            'STMWOOMIRACLESPRYTSMIFJOMCESKOGJKLMSMI',
            'ELPJMLSMUMGKEJSKNMJAPOBREAKTHROUGHPEIJM',
            'KLAMFAJFLSGMDTVMWURHDKABNPOIUMAFNHAKHU',
            'JUMPSOMESWERUMAMBOCEHJAKOWHCSANKNLALADI'
        ]
        self.alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                         'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        self.word_storage = []
        self.results = []
        self.end_results = defaultdict(list)

    def check_words(self):
        for word in self.word_list:
            for r in self.word_rows:
                if word in r.lower() and len(word) > 1:
                    self.word_storage.append(word.upper())
                    self.word_alphabet(word)
        self.results = sorted(list(set(self.word_storage)))
        #self.get_unique_words()
        self.parse_word_list()

    def parse_word_list(self):
        self.end_results = dict(OrderedDict(sorted(dict(self.end_results).items())))
        for key, value in self.end_results.items():
            value_join = "\t".join(value)
            print(f"{key}: {value_join}")

    def word_alphabet(self, word):
        for abc in self.alphabet:
            if word.startswith(abc.lower()):
                self.end_results[abc].append(word)

    def get_unique_words(self):
        for r in self.results:
            print(r)


if __name__ == "__main__":
    fw = FindWords()
    fw.check_words()
