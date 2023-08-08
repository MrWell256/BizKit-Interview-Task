from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!
    current_users = USERS
    searched_users = []

    if "id" in args:
        searched_users = [user for user in current_users if user["id"] == args["id"]]

    if "name" in args:
        name_to_search = args["name"].lower()
        searched_users += [user for user in current_users if name_to_search in user["name"].lower()]

    if "age" in args:
        age_to_search = int(args["age"])
        searched_users += [user for user in current_users if int(user["age"]) == age_to_search - 1]

        searched_age = [user for user in current_users if int(user["age"]) == age_to_search]
        for user in searched_age:
            if user["id"] not in (u["id"] for u in searched_users):
                searched_users.append(user)

        plus_one = [user for user in current_users if int(user["age"]) == age_to_search + 1]
        for user in plus_one:
            if user["id"] not in (u["id"] for u in searched_users):
                searched_users.append(user)

    if "occupation" in args:
        occupation_to_search = args["occupation"].lower()
        searched_users += [user for user in current_users if occupation_to_search in user["occupation"].lower()]

    elif searched_users == []:
        return current_users

    return searched_users
