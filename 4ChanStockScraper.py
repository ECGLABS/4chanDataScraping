import collections
import re
import requests
from bs4 import BeautifulSoup

def get_common_phrases(thread_url, phrase_length, exclude_list=None, exclude_dict=None):
    response = requests.get(thread_url)
    response.raise_for_status()

    phrases = collections.Counter()
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    posts = soup.find_all(class_='postMessage')

    for post in posts:
        # Extract phrases of specified length consisting of all capital letters
        text = post.get_text()
        matches = re.findall(r'\b[A-Z]{%d}\b' % phrase_length, text)
        for match in matches:
            if match not in exclude_list and match not in exclude_dict:
                phrases[match] += 1

    # Get the most common phrases
    most_common_phrases = phrases.most_common(10)  # Change the number as desired
    return most_common_phrases

# On the next line change the URL to the current Stock Market General on BIZ
thread_url = 'https://boards.4channel.org/biz/thread/55352526'
phrase_length = 3 # or 4, depending on your desired length

exclude_list = ['ABCD', 'EFGH']  # Specify the phrases you want to exclude in a list
exclude_dict = {'IJKL': 1, 'MNOP': 2}  # Specify the phrases and their counts to exclude in a dictionary

exclude_list = ['TURN', 'PLAN','PUMP', 'AUSE', 'ONTH', 'SAND', 'INGS', 'WILL', 'MENT', 'MARK', 'RKET', 'RADI', 'YEAR', 'IONS', 'COMP', 'INVE', 'ADIN', 'ESTI', 'VEST', 'FORE', 'NVES', 'EDTO', 'VERY', 'WHAT', 'SIDE', 'TYOU', 'MONE', 'THES', 'CASH', 'EYOU', 'LIKE', 'IGHT', 'STOC', 'ARKE', 'DONT', 'ABOU', 'BOUT', 'BOND', 'ERES', 'ANDT', 'ATIO', 'ESTO', 'TOCK', 'LOCK', 'ROCK', 'COCK', 'TRAD', 'STHE', 'MAKE', 'OUGH', 'DING', 'INGA', 'ONEY', 'INGI', 'THAT', 'CUCK', 'THER', 'TTHE', 'TRAN', 'HAVE', 'THIN', 'JUST', 'TING', 'INGT', 'ETHE', 'THIS', 'THEM', 'YOUR', 'HERE', 'WITH', 'TION', 'ALLY', 'NTHE', 'SOME', 'OULD', 'THEY', 'OFTH', 'FTHE', 'THEN', 'HTTP', 'TTPS', 'HING', 'WHEN', 'OTHE', 'KING', 'EVER']  # Specify the phrases you want to exclude in a list

common_phrases = get_common_phrases(thread_url, phrase_length, exclude_list, exclude_dict)

print(f'Most common {phrase_length}-letter phrases:')
for phrase, count in common_phrases:
    print(f'{phrase}: {count} occurrences')