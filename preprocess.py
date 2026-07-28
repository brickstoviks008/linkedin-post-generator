import json
from llm_helper import llm
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException


def process_posts(raw_file_path, processed_file_path=None):
    enriched_posts = []
    with open(raw_file_path, encoding='utf-8') as file:
        posts = json.load(file)
        for post in posts:
            metadata = extract_metadata(post['text'])
            post_with_metadata = post | metadata
            enriched_posts.append(post_with_metadata)

    unified_tags = get_unified_tags(enriched_posts)
    for post in enriched_posts:
        current_tags = post['tags']
        new_tags = {unified_tags[tag] for tag in current_tags}
        post['tags'] = list(new_tags)

    with open(processed_file_path, encoding='utf-8', mode="w") as outfile:
        json.dump(enriched_posts, outfile, indent=4)

def extract_metadata(post):
    template = '''
       You are given a LinkedIn post. You need to extract number of lines, language of the post and tags.
       1. Return a valid JSON. No preamble. 
       2. JSON object should have exactly three keys: line_count, language and tags. 
       3. tags is an array of text tags. Extract maximum two tags.
       4. Language must be either "English" or "Hinglish" (Hinglish means hindi + english).
          - Use "Hinglish" ONLY if the post contains actual Hindi words, 
            e.g. "hai", "nahi", "kya", "achi baat", "sapne", "kar", "raha". 
          - If the post is entirely in English with no Hindi/Roman-Hindi words mixed in, 
            the language MUST be "English", even if the topic, tone, or style feels Indian.
          - Do NOT classify as Hinglish just because the post is about Indian topics like LinkedIn, jobs, or Indian workplaces.

       Examples:
       Post: "Just saw a LinkedIn Influencer with 65K+ followers claiming he can help you grow your platform."
       Language: English

       Post: "sapne dekhna achi baat hai, lekin job ka sapna dekh ke 'interested' likhna, yeh toh achi baat nahi hai na?"
       Language: Hinglish

       Post: "To everyone who's still looking for a job... I see you. I feel you."
       Language: English

       Here is the actual post on which you need to perform this task:  
       {post}
       '''
    pt = PromptTemplate.from_template(template)
    chain = pt | llm
    response = chain.invoke(input={"post": post})

    try:
        json_parser = JsonOutputParser()
        res = json_parser.parse(response.content)
    except OutputParserException:
        raise OutputParserException("Context too big. Unable to parse jobs.")
    return res


def get_unified_tags(posts_with_metadata):
    unique_tags = set()
    # Loop through each post and extract the tags
    for post in posts_with_metadata:
        unique_tags.update(post['tags'])  # Add the tags to the set

    unique_tags_list = ','.join(unique_tags)

    template = '''I will give you a list of tags. You need to unify tags with the following requirements,
    1. Tags are unified and merged to create a shorter list. 
       Example 1: "Job seekers", "Job Hunting" can be all merged into a single tag "Job Search". 
       Example 2: "Motivation", "Inspiration", "Drive" can be mapped to "Motivation"
       Example 3: "Personal Growth", "Personal Development", "Self Improvement" can be mapped to "Self Improvement"
       Example 4: "Scam Alert", "Job Scam" can be mapped to "Scams"
    2. Each tag should be follow title case convention. example: "Motivation", "Job Search"
    3. Output should be a JSON object, No preamble
    3. Output should have mapping of original tag and the unified tag. 
       For example: {{"Job seekers": "Job Search",  "Job Hunting": "Job Search", "Motivation": "Motivation}}
    4. Tags must describe the THEME or TOPIC of the post — never a literal word, phrase, or quote pulled from the post text itself.
    5. Tags must always be in English, even if the post is in Hinglish or Hindi. Never output a Hindi word as a tag (e.g. never "Sapne", "Naukri", "Sapna" — instead use the English concept, like "Dreams" or "Job Search").
    6. Tags should be generic and reusable across many posts (think: category labels), not specific to this one post's wording.

    Here is the list of tags: 
    {tags}
    '''
    pt = PromptTemplate.from_template(template)
    chain = pt | llm
    response = chain.invoke(input={"tags": str(unique_tags_list)})
    try:
        json_parser = JsonOutputParser()
        res = json_parser.parse(response.content)
    except OutputParserException:
        raise OutputParserException("Context too big. Unable to parse jobs.")
    return res

if __name__ == "__main__":
    process_posts("data/raw_posts.json", "data/processed_posts.json")