import unittest
import sqlite3


class SqliteTestCase(unittest.TestCase):

    def setUp(self):
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()

    def tearDown(self):
        self.conn.close()

    def test_population_less_than_50_sqrm(self):
        USA_Population = self.cursor.execute('SELECT Population FROM Countries WHERE Country = "USA"').fetchone()
        USA_Area = self.cursor.execute('SELECT Area FROM Countries WHERE Country = "USA"').fetchone()
        Population_on_sqmtr = int(USA_Population[0]) / int(USA_Area[0])

        self.assertLess(Population_on_sqmtr, 50)

    def test_sum_of_countries_less_than_2_billion(self):
        All_Population = 0
        for pop in self.cursor.execute('SELECT Population FROM Countries'):
            All_Population += int(pop[0])

        self.assertLess(All_Population, 2 * pow(10, 9))

if __name__ == '__main__':
    unittest.main()
