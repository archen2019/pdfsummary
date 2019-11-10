import pke

def get_key_phrases(numKey, directory):
    extractor = pke.unsupervised.TopicRank()
    extractor.load_document(input='cleantext.txt', language='en')
    extractor.candidate_selection()
    extractor.candidate_weighting()
    keytuple = extractor.get_n_best(n=numKey)

    keyphrases = [t[0] for t in keytuple]

    with open(directory + 'keyphrases.txt', 'w') as f:
        for key in keyphrases:
            f.write(key + '\n')

    return keyphrases
