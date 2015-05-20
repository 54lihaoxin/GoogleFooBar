import sys
import solution
# from classes import ?


class TestSuite:
    
    def run(self):
        self.test000()
        self.test001()
#         self.test002()
#         self.test003()
#         self.test004()

    def test000(self):
        print 'test 000\n'
        population = [[1, 2, 3], [2, 3, 4], [3, 2, 1]]
        x = 0
        y = 0
        strength = 2
        r = solution.answer(population, x, y, strength)
        print '  input:\t', population, x, y, strength
        print '  expect:\t', [[-1, -1, 3], [-1, 3, 4], [3, 2, 1]]
        print '  output:\t', r
        print
        
    def test001(self):
        print 'test 002\n'
        population = [[6, 7, 2, 7, 6], [6, 3, 1, 4, 7], [0, 2, 4, 1, 10], [8, 1, 1, 4, 9], [8, 7, 4, 9, 9]]
        x = 2
        y = 1
        strength = 5
        r = solution.answer(population, x, y, strength)
        print '  input:\t', population, x, y, strength
        print '  expect:\t', [[6, 7, -1, 7, 6], [6, -1, -1, -1, 7], [-1, -1, -1, -1, 10], [8, -1, -1, -1, 9], [8, 7, -1, 9, 9]]
        print '  output:\t', r
        print
        
def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)