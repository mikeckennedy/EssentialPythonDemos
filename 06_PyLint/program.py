"""
This is the docs for the module
"""
import text_files
import db_json


class Program(object):
    """
    This is the docs for the Program class.
    """

    @staticmethod
    def main():
        """Docs for main!"""
        age = 7
        print(age)
        text_files.run()
        db_json.run()

    def other():
        print("other")


if __name__ == '__main__':
    prog = Program()
    #prog.other()
    Program.main()
