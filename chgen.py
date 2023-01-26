import paddlehub as hub

class ChineseGen():
    dft_line = 4
    dft_word = 7

    def __init__(self):
        self.dft_line = 4
        self.dft_word = 7

    def genSS(self, txt, ln=4, wd=7):
        """module = hub.Module(directory="~/.paddlehub/models/ernie_gen_lover_words")"""
        module = hub.Module(name="ernie_gen_lover_words")

        #testTxt = ['家人','亲情','故乡']
        testTxt = txt.split(',')
        results = module.generate(texts=testTxt, use_gpu=False, beam_width=2)
        for rr in results:
            for result in rr:
                print(result)
        return results[0]

    def genSiWithHead(self, txt, ln=4, wd=7):
        module = hub.Module(name="ernie_gen_acrostic_poetry", line=ln, word=wd)

        testTxt = [txt]
        results = module.generate(texts=testTxt, use_gpu=False, beam_width=2)
        for rr in results:
            for result in rr:
                print(result)
        return results[0]

    def genSi(self, txt,ln=4, wd=7):
        module = hub.Module(name="ernie_gen_poetry")

        testTxt = [txt]
        results = module.generate(texts=testTxt, use_gpu=False, beam_width=2)
        for r in results[0]:
            print(txt)
            print(r)
            print('\n')
        return results[0]

    def genCouplet(self, txt, ln=4, wd=7):
        module = hub.Module(name="ernie_gen_couplet")

        #testTxt = ['天清气朗人欢笑']
        testTxt = [txt]
        results = module.generate(texts=testTxt, use_gpu=False, beam_width=5)
        for rr in results:
            for result in rr:
                print(txt)
                print(result)
                print('\n')
        return results[0]

if __name__ == '__main__':
    chgen= ChineseGen()
    chgen.genSiWithHead('天清气爽人欢笑语', 8, 5)
    chgen.genSS('家人,亲情,故乡')
    chgen.genCouplet('天清气朗人欢笑')
    chgen.genSi('明月别枝惊鹊，清风半夜鸣蝉。')