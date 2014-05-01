from tests.game_tests import GameTests


class A:
    @classmethod
    def create(cls):
        print("Creating type from: " + str(cls))
        return A()

    def use_var(self):
        print("using local instance: " + str(id(self)))


a1 = A.create()
a2 = A.create()

a1.use_var()
a2.use_var()


GameTests.setUpClass()

t1 = GameTests()
t1.setUp()
t1.test_can_create_empty_game()

t2 = GameTests()
t2.setUp()
t2.test_cell_can_be_played()