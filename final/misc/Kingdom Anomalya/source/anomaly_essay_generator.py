from random import randrange


# GET ESSAY FROM SOURCE TEXT
with open('essay.txt', 'r', encoding='utf-8') as file:
    paragraphs = file.readlines()

    file.close()


# GENERATE ANOMALY ESSAY
anomaly_essay = ''
for paragraph in paragraphs:
    sentences = [sentence.strip() for sentence in paragraph.split('.')]

    anomaly_paragraph = ''
    for sentence in sentences:
        if (len(sentence) == 0):
            continue

        sentence += '. '
        anomaly_paragraph += sentence * randrange(3, 2500)

    anomaly_essay += anomaly_paragraph.rstrip()
    anomaly_essay += '\n'


# INSERTING FLAG
with open('flag.txt', 'r') as file:
    flag = file.read()

    file.close()

def get_random_valid_index():
    result = randrange(len(anomaly_essay))

    if result in {' ', '.', '\n'}:
        return get_random_indexes()
    return result

def get_random_indexes():
    result = [get_random_valid_index() for _ in range(len(flag))]
    result.sort()

    if not all(result[i - 1] != result[i] for i in range(1, len(flag))):
        return get_random_indexes()
    return result

anomaly_essay = list(anomaly_essay)
for i, j in enumerate(get_random_indexes()):
    anomaly_essay[j] = flag[i]
anomaly_essay = ''.join(anomaly_essay)


# WRITE FILES
with open('anomaly_essay.txt', 'w', encoding='utf-8') as file:
    file.writelines(anomaly_essay)

    file.close()