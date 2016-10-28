# Appbaseio open source

### Development
```
pip install pystache requests pygithub3
generate.py
```

Repository data (repos.json) is pulled via the GitHub API (e.g., website). By default the
script performs unauthenticated requests, so it's easy to run up against
GitHub's limit of [60 unauthenticated requests per
hour](http://developer.github.com/v3/#rate-limiting). To make authenticated
requests and work around the rate-limiting, add an entry for api.github.com to
your ~/.netrc file, preferably with a Personal Access Token from
https://github.com/settings/applications.

    machine api.github.com
      login YourUsername
      password PersonalAccessToken

Images are loaded by convention from the `repo_images/` directory. Ensure the
name is the same as the repo name in the `repos.json` file and has a `.jpg`
extension.