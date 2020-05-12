def read_data(train_raw_path):
    with open(train_raw_path, 'rb') as f:
        import json
        train_data = [json.loads(line) for line in f.readlines()]
    train_summarization = [d['summarization'] for d in train_data]
    train_article = [d['article'] for d in train_data]
    return train_summarization, train_article


if __name__ == '__main__':
    train_summarization, train_article = read_data('data/train_with_summ.txt')
    print(train_summarization[0])
    print(train_article[0])
