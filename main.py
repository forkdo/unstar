from sys import argv
from time import sleep
from GitStars import GitStars
from GitStarsException import GitStarsException


if __name__ == '__main__':
    my_stars = GitStars("https://api.github.com", argv[1])

    try:
        reposes = my_stars.get_all_star_repos(2)

        for repo in reposes:
            if my_stars.delete_star(repo):
                print(f"{repo} is unstarred")
            else:
                print(f"{repo} not found")

            sleep(1)

    except GitStarsException as e:
        print('exception is - ' + e.__str__())
