class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

    def __repr__(self):
        return self.children
    
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        syllables = []
        current_syllable = ""
        for char in word:
            # print(char, node.children.keys())
            
            if char in node.children:
                current_syllable += char
                node = node.children[char]
                # if node.is_end_of_word:
                #     # print(char, node.children.keys())
                #     syllables.append(current_syllable)
                #     current_syllable = ""
                #     node = self.root  # 重置搜索节点到根节点
            else:
                # print("New")
                # 如果当前字符不在字典树中，标记当前音节结束，并重置搜索节点
                if current_syllable:
                    syllables.append(current_syllable)

                current_syllable = ""
                node = self.root
                if char in node.children:
                    node = node.children[char]
                    current_syllable += char
        # 添加最后一个音节（如果有的话）
        if current_syllable:
            syllables.append(current_syllable)
        return syllables
    
    def traverse(self, node, current_word):
        if node.is_end_of_word:
            self.all.append(current_word)
        for char, child_node in node.children.items():
            self.traverse(child_node, current_word + char)

class SyllSeg:
    
    def __init__(self):
        trie = Trie()
        a = ['yu', 'yue', 'yun', 'yuan', 'ya', 'yan', 'yang', 'yao', 'yi', 'yin', 'ying', 'you', 'yong', 'ye', 'shu', 'shun', 'shui', 'shua', 'shuai', 'shuan', 'shuang', 'shuo', 'she', 'shen', 'sheng', 'shei', 'sha', 'shai', 'shao', 'shan', 'shang', 'shou', 'shi', 'su', 'sui', 'suo', 'suan', 'sun', 'sa', 'san', 'sang', 'sao', 'sai', 'se', 'sen', 'seng', 'sou', 'song', 'si', 'a', 'ao', 'an', 'ang', 'ai', 'ca', 'cai', 'can', 'cang', 'cao', 'cha', 'chan', 'chang', 'chao', 'chai', 'che', 'chen', 'cheng', 'chu', 'chuai', 'chuan', 'chuang', 'chun', 'chuo', 'chui', 'chou', 'chong', 'chi', 'cu', 'cuan', 'cun', 'cui', 'cuo', 'ce', 'cen', 'ceng', 'cou', 'cong', 'ci', 'mi', 'mie', 'miao', 'mian', 'min', 'ming', 'miu', 'me', 'men', 'meng', 'mei', 'ma', 'mao', 'man', 'mang', 'mai', 'mu', 'mo', 'mou', 'de', 'deng', 'dei', 'du', 'duan', 'duo', 'dun', 'dui', 'da', 'dao', 'dai', 'dan', 'dang', 'di', 'ding', 'diao', 'dian', 'diu', 'die', 'dong', 'dou', 'pa', 'pan', 'pang', 'pai', 'pao', 'pi', 'pie', 'pin', 'ping', 'piao', 'pian', 'po', 'pou', 'pen', 'peng', 'pei', 'pu', 'hu', 'huo', 'hua', 'huan', 'huang', 'huai', 'hun', 'hui', 'ha', 'han', 'hang', 'hao', 'hai', 'he', 'hen', 'heng', 'hei', 'hou', 'hong', 'li', 'lian', 'liang', 'liao', 'lin', 'ling', 'liu', 'lie', 'la', 'lan', 'lang', 'lao', 'lai', 'lu', 'lun', 'luo', 'luan', 'le', 'lei', 'leng', 'lou', 'long', 'lv', 'lve', 'ni', 'nian', 'niang', 'niao', 'nie', 'niu', 'ning', 'nv', 'nve', 'nu', 'nuo', 'nuan', 'na', 'nao', 'nan', 'nang', 'nai', 'ne', 'nei', 'nen', 'neng', 'nong', 'nou', 'ga', 'gan', 'gang', 'gao', 'gai', 'gu', 'gun', 'gua', 'guan', 'guang', 'guai', 'gui', 'guo', 'ge', 'gei', 'gen', 'geng', 'gong', 'gou', 'ba', 'bao', 'bai', 'ban', 'bang', 'bo', 'ben', 'beng', 'bei', 'bi', 'bian', 'biao', 'bin', 'bing', 'bie', 'bu', 'ta', 'tan', 'tang', 'tao', 'tai', 'tu', 'tun', 'tui', 'tuo', 'tuan', 'ti', 'ting', 'tiao', 'tian', 'tie', 'te', 'teng', 'tou', 'tong', 'kong', 'kou', 'ke', 'ken', 'keng', 'ku', 'kun', 'kua', 'kuai', 'kuan', 'kuang', 'kuo', 'kui', 'ka', 'kan', 'kang', 'kai', 'kao', 'ju', 'jue', 'jun', 'juan', 'ji', 'jin', 'jing', 'jia', 'jian', 'jiang', 'jiao', 'jiu', 'jie', 'jiong', 'e', 'en', 'er', 'qi', 'qin', 'qing', 'qiong', 'qia', 'qian', 'qiang', 'qiao', 'qie', 'qiu', 'qu', 'que', 'qun', 'quan', 'zu', 'zuo', 'zui', 'zun', 'zuan', 'zhi', 'zhu', 'zhui', 'zhun', 'zhuo', 'zhua', 'zhuai', 'zhuan', 'zhuang', 'zha', 'zhai', 'zhao', 'zhan', 'zhang', 'zhe', 'zhen', 'zheng', 'zhong', 'zhou', 'zi', 'ze', 'zei', 'zen', 'zeng', 'zong', 'zou', 'za', 'zan', 'zang', 'zao', 'zai', 'fen', 'feng', 'fei', 'fo', 'fou', 'fa', 'fan', 'fang', 'fu', 'wo', 'wen', 'weng', 'wei', 'wa', 'wan', 'wang', 'wai', 'wu', 'xu', 'xuan', 'xue', 'xun', 'xi', 'xia', 'xian', 'xiang', 'xiao', 'xin', 'xing', 'xiong', 'xie', 'xiu', 'ru', 'rui', 'run', 'ruo', 'ruan', 'ran', 'rang', 'rao', 're', 'ren', 'reng', 'ri', 'rong', 'rou', 'o', 'ou']  # 这应该是一个实际的列表
        for syll in a:
            trie.insert(syll)
        self.pinyin_trie = trie
        
    def seg(self, source):
        syllables = self.pinyin_trie.search(source)
        return syllables
        
        
# SyllSeg = SyllSeg()
# print(SyllSeg.seg("海内cunzhiji"))

