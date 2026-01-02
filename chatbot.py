import json
import random
from preprocess import preprocess
from llm import llm_response

def load_knowledge_base(path="african_mother_data.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def similarity(set1, set2):
    if not set1 or not set2:
        return 0
    return len(set1 & set2) / len(set1 | set2)

def get_all_sentences(kb):
    sentences = []
    for category in kb["categories"].values():
        sentences.extend(category)
    for example in kb["example_intents"]:
        sentences.append(example["response"])
    return sentences

def get_most_relevant_sentence(user_input, sentences):
    user_tokens = preprocess(user_input)
    best_score = 0
    best_sentence = None

    for sentence in sentences:
        score = similarity(user_tokens, preprocess(sentence))
        if score > best_score:
            best_score = score
            best_sentence = sentence

    return best_sentence, best_score

def chatbot(user_input, kb):
    sentences = get_all_sentences(kb)
    response, score = get_most_relevant_sentence(user_input, sentences)

    # Rule-based response if confidence is high
    if score >= 0.2 and response:
        endearment = random.choice(kb["persona"]["default_terms_of_endearment"])
        return f"{endearment}, {response}"

    # LLM fallback
    return llm_response(user_input)
