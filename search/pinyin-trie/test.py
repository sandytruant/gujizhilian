class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.all = []
        
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def traverse(self, node, current_word):
        if node.is_end_of_word:
            self.all.append(current_word)
        for char, child_node in node.children.items():
            self.traverse(child_node, current_word + char)


# 构建汉语拼音声韵组合字典树
def build_pinyin_trie():
    trie = Trie()
    initials = "b,p,m,f,d,t,n,l,g,k,h,j,q,x,zh,ch,sh,r,z,c,s".split(',')
    finals = {
        '开口呼': 'a,o,e,er,ai,ei,ao,ou,an,en,ang,eng'.split(','),
        '齐齿呼': 'i,ia,ie,iao,iu,iou,ian,in,iang,ing,iong'.split(','),
        '合口呼': 'u,ua,uo,uai,uei,ui,uan,un,uang,ong'.split(','),
        '合2': 'u,uo'.split(','),
        '撮口呼': 'ü,üe,üan,ün'.split(',')
    }

    # 插入零声母韵母
    for final in finals['开口呼']:
        trie.insert(final)

    # 插入带声母韵母
    for initial in initials:
        for final in finals['开口呼']:
            if initial not in 'j,q,x':
                trie.insert(initial + final)
        for final in finals['齐齿呼']:
            if initial in 'j,q,x':
                trie.insert(initial + final)
        for final in finals['合口呼']:
            if initial not in 'b,p,m,f,j,q,x':
                trie.insert(initial + final)
        for final in finals['合2']:
            if initial in 'b,p,m,f':
                trie.insert(initial + final)
        for final in finals['撮口呼']:
            if initial in 'j,q,x':
                trie.insert(initial + final)
    s = 'yi,ya,ye,yao,yu,you,yan,yin,yang,ying,yiong'.split(',') + \
           'wu,wa,wo,wai,wei,wan,wen,wang,weng'.split(',') + \
               'yu,yue,yuan,yun'.split(',')
    for syll in s:
        trie.insert(syll)
    
                    
    return trie

# 使用构建函数
pinyin_trie = build_pinyin_trie()

# 遍历并输出所有汉语拼音声韵组合
pinyin_trie.traverse(pinyin_trie.root, "")
print(pinyin_trie.all)

