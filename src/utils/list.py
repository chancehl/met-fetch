from typing import List


def check_if_exists(obj_id: str, objects: List) -> bool:
    """
    Checks to see if an object with a given id exists in a list

    Parameters:
    id (str): The object id we are searching for
    objects (list): All objects

    Returns:
    bool: True if object exists, False otherwise
    """
    for obj in objects:
        if obj.get("id" == obj_id):
            return True

    return False
