import requests
import urllib.parse
from github import Github

ACCESS_TOKEN = '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'

g = Github(ACCESS_TOKEN)

# print(g.get_user().get_repos())

def search_github(keywords):
    query = '+'.join(keywords) + '+in:name+in:description'
    result = g.search_repositories(query, 'stars', 'desc')

    print(f'Found {result.totalCount} repo(s)')

    for repo in result:
        print(repo.clone_url)


if __name__ == '__main__':
    keywords = input('Enter keyword(s)[e.g python, flask, postgres]: ')
    keywords = [keyword.strip() for keyword in keywords.split(',')]
    search_github(keywords)