from gittle import Gittle

repo_path = '/tmp/gittle_bare'
repo_url = 'git+ssh://git@github.com/AaronO/dulwich.git'

repo = Gittle.clone(repo_url, repo_path)

print((repo.tracked_files))
