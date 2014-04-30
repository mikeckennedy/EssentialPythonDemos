from db import Repository, UserNotFoundError, SQLError


def display_user():
    r = Repository()
    with r:
        user_id_text = input('Who do you want to find? ')
        the_id = int(user_id_text)
        u = r.find_user(the_id)
        print("Cool you found {}".format(u.name))


def main():
    try:
        display_user()
    except ValueError as ve:
        print("Oops, we expected a number!")
    except UserNotFoundError as unf:
        print("sorry, that user with id {0} doesn't exist. More info {1}".format(
            unf.user_id, str(unf)
        ))
    except SQLError as sqle:
        print("Oops, DB offline!")
    #except Exception as e:
     #   print("sorry, FAIL: " + str(e), type(e))
    finally:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
