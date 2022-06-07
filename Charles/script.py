import requests
import urllib.parse
from github import Github


# Search query Format: SEARCH_KEYWORD_1 SEARCH_KEYWORD_N QUALIFIER_1 QUALIFIER_N
# query = 'GitHub Octocat in:readme user:defunkt'
query = 'addClass+in:file+language:js+repo:jquery/jquery'


ACCESS_TOKEN = 'yourtokenhere'

qualifiers = 'in:name+in:description'

# OAuth
base = 'curl -u username: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 https://api.github.com/user'

keywords = ['Flask-admin']

def search_repositories():
    # query = '+'.join(keywords) + '+in:readme+in:description'
    response = requests.get('https://api.github.com')
    print(response.json())

search_repositories()
