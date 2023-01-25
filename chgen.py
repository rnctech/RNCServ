import paddlehub as hub

def genSS():
    """module = hub.Module(directory="/Users/admin/PycharmProjects/RNCServ/models/ernie_gen_lover_words")"""
    module = hub.Module(name="ernie_gen_lover_words")

    testTxt = ['家人','亲情','故乡']
    results = module.generate(texts=testTxt, use_gpu=False, beam_width=1)
    for rr in results:
        for result in rr:
            print(result)

def genSiWithHead(txt, ln=4, wd=7):
    module = hub.Module(name="ernie_gen_acrostic_poetry", line=ln, word=wd)

    testTxt = [txt]
    results = module.generate(texts=testTxt, use_gpu=False, beam_width=2)
    for rr in results:
        for result in rr:
            print(result)

def genSi(txt):
    module = hub.Module(name="ernie_gen_poetry")

    testTxt = [txt]
    results = module.generate(texts=testTxt, use_gpu=False, beam_width=2)
    for r in results[0]:
        print(txt)
        print(r)
        print('\n')

def genCouplet(txt):
    module = hub.Module(name="ernie_gen_couplet")

    #testTxt = ['天清气朗人欢笑']
    testTxt = [txt]
    results = module.generate(texts=testTxt, use_gpu=False, beam_width=5)
    for rr in results:
        for result in rr:
            print(txt)
            print(result)
            print('\n')

if __name__ == '__main__':
    genSiWithHead('天清气爽人欢笑语', 8, 5)
    genSS()
    genCouplet('天清气朗人欢笑')
    genSi('明月别枝惊鹊，清风半夜鸣蝉。')