import time
from flask import Blueprint

# I'm using PyCharm as my IDE, "from .data.match_data import MATCHES" does not work on my end
# so I changed it to "from .data import match_data" and used "match_data.MATCHES" instead to make it work
from .data import match_data


bp = Blueprint("match", __name__, url_prefix="/match")


@bp.route("<int:match_id>")
def match(match_id):
    if match_id < 0 or match_id >= len(match_data.MATCHES):
        return "Invalid match id", 404

    start = time.time()
    msg = "Match found" if (is_match(*match_data.MATCHES[match_id])) else "No match"
    end = time.time()

    return {"message": msg, "elapsedTime": end - start}, 200


def is_match(fave_numbers_1, fave_numbers_2):
    # Made fave_numbers_1 into a set to make the matching process faster
    fave_numbers_1_set = set(fave_numbers_1)

    for number in fave_numbers_2:
        if number not in fave_numbers_1_set:
            return False

    return True
