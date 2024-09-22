import httpx


def github_check(url: str, response: httpx.Response) -> tuple[bool, bool]:
    if "github.com/" not in url:
        return False, False
    if (
        "months ago" in response.text
    ):
        return True, True

    return True, False


def gitlab_check(url: str, response: httpx.Response) -> tuple[bool, bool]:
    if not (("gitlab.com/" in url) or ("_gitlab_session" in response.cookies)):
        return False, False
    if (
        "months ago"
        in response.text
    ):
        return True, True

    return True, False


def gitea_check(url: str, response: httpx.Response) -> tuple[bool, bool]:
    if (
        "months ago" in response.text
        in response.text
    ):
        return True, True

    return True, False
