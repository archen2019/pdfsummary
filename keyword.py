import pke

extractor = pke.unsupervised.TopicRank()
extractor.load_document(input='cleantext.txt', language='en')
extractor.candidate_selection()
extractor.candidate_weighting()
keyphrases = extractor.get_n_best(n=7)
