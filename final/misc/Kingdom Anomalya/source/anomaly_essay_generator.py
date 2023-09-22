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

    while anomaly_essay[result] in [' ', '.', '\n']:
        result = (result + 1) % len(anomaly_essay)
    return result

def get_random_indexes():
    result = [get_random_valid_index() for _ in range(len(flag))]
    result.sort()

    if not all(result[i - 1] != result[i] for i in range(1, len(flag))):
        return get_random_indexes()
    return result

anomaly_essay = list(anomaly_essay)
while True:
    valid = True
    indexes = get_random_indexes()

    original = ''
    altered  = ''

    for i, j in enumerate(indexes):
        if anomaly_essay[j] == flag[i]:
            valid = False
            break
    if valid:
        for i, j in enumerate(indexes):
            original += flag[i]
            altered  += anomaly_essay[j]

            anomaly_essay[j] = flag[i]
        anomaly_essay = ''.join(anomaly_essay)

        print(original)
        print(altered)
        break


# WRITE FILES
with open('anomaly_essay.txt', 'w', encoding='utf-8') as file:
    file.writelines(anomaly_essay)

    print("ESSAY GENERATED")

    file.close()