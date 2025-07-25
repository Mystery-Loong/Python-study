from pathlib import Path

def count_words(path):
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        # print(f"Sorry,the file {path} does not exist.")
        pass
    else:
        # 计算文件包含多少个单词
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

filenames = ['alice.txt','siddhartha.txt','Moby_Dick.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)