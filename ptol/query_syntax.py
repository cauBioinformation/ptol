import nltk
from nltk.corpus import wordnet
import inflect
import itertools

def run_query_syntax(args):

    if 'init' == args.mode:
        nltk.download('wordnet')
        nltk.download('averaged_perceptron_tagger')
        print('Successfully downloaded wordnet and other thesaurus!')
    elif 'run' == args.mode:

        p = inflect.engine()

        def get_word_variants(word):
            variants = {word, word.lower(), word.upper(), word.capitalize()}
            plural = p.plural(word)
            if plural:
                variants.add(plural)
            singular = p.singular_noun(word)
            if singular:
                variants.add(singular)
            return variants

        def get_word_forms(word):
            word_forms = {}
            for synset in wordnet.synsets(word):
                word_type = synset.pos()
                lemmas = [lemma.name().replace('_', ' ') for lemma in synset.lemmas()]
                if word_type not in word_forms:
                    word_forms[word_type] = set(lemmas)
                else:
                    word_forms[word_type].update(lemmas)
            return word_forms

        def build_search_query(word):
            variants = get_word_variants(word)
            word_forms = get_word_forms(word)
            all_forms = set()
            for forms in word_forms.values():
                for form in forms:
                    all_forms.update(get_word_variants(form))
            all_search_terms = variants.union(all_forms)
            # print(all_search_terms)

            return list(all_search_terms)


        keywordsFilePointer = open(args.inputFilePath, 'r', encoding='utf-8')
        resultFilePointer = open(args.outputFilePath, 'w', encoding='utf-8')
        originalKeywordsList = []
        for line in keywordsFilePointer:
            keyword = line.strip('\n')
            # word = "enzyme"
            all_search_terms_list = build_search_query(keyword)
            originalKeywordsList.append(all_search_terms_list)
            resultFilePointer.write(keyword + ':\n' + ' | '.join(all_search_terms_list) + '\n')

        resultFilePointer.write('Note: Please determine the most professional keywords that you need. For example, '
                                  'through professional thesaurus such as MeSH, use * to reduce the possible repetition of words.\n')

        #  originalKeywordsList = [['chen', 'hui'], ['xu', 'gang'], ['long', 'yang']]

        combinations = list(itertools.product(*originalKeywordsList))


        # pubmed
        def format_combination(combination):
            formatted = f"({combination[0]}[Title/Abstract])"
            for word in combination[1:]:
                formatted = f"({formatted} AND ({word}[Title/Abstract]))"
            return formatted

        formatted_strings = [format_combination(combination) for combination in combinations]

        resultFilePointer.write('\nPubMed database search terms are as follows:\n')

        for string in formatted_strings:
            resultFilePointer.write(string[1:-1]+'\n')
            # print(string[1:-1])
        resultFilePointer.write(
            'You can simply copy the query and paste it to the PubMed website (https://pubmed.ncbi.nlm.nih.gov/advanced/) for retrieval.\n')

        def transformPubmedLink(string):
            replacements = {
                '[': '%5B',
                '/': '%2F',
                ']': '%5D',
                '(': '%28',
                ')': '%29',
                ' AND ': '+AND+'
            }
            for old, new in replacements.items():
                string = string.replace(old, new)

            pubmedWebsiteString = 'https://pubmed.ncbi.nlm.nih.gov/?term=' + string + '&sort='
            return pubmedWebsiteString

        resultFilePointer.write('\nHere, we automatically generate the corresponding pubmed search results URL link for you:\n')
        for string in formatted_strings:
            resultFilePointer.write(transformPubmedLink(string[1:-1])+'\n')


        # web of science
        def format_combination2(combination):
            formatted = f"(ALL=({combination[0]}))"
            for word in combination[1:]:
                formatted = f"({formatted} AND ALL=({word}))"
            return formatted

        formatted_strings = [format_combination2(combination) for combination in combinations]

        resultFilePointer.write('\nWeb of Science database search terms are as follows:\n')

        for string in formatted_strings:
            resultFilePointer.write(string[1:-1] + '\n')

        resultFilePointer.write(
            'You can simply copy the query and paste it to the Web of Science website (https://www.webofscience.com/wos/woscc/advanced-search) for retrieval.\n')

        keywordsFilePointer.close()
        resultFilePointer.close()

    # Created by Huilong Chen.
