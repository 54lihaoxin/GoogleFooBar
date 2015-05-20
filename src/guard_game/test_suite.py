import sys
import solution
# from classes import ?


class TestSuite:
    
    def run(self):
        self.test000()
        self.test001()
        self.test002()
#         self.test003()
#         self.test004()

    def test000(self):
        print 'test 000\n'
        n = 13
        r = solution.answer(n)
        print '  input:\t', n
        print '  expect:\t', 4
        print '  output:\t', r
        print
        
    def test001(self):
        print 'test 002\n'
        n = 1235
        r = solution.answer(n)
        print '  input:\t', n
        print '  expect:\t', 2
        print '  output:\t', r
        print
        
    def test002(self):
        print 'test 002\n'
        n = 6471289
        r = solution.answer(n)
        print '  input:\t', n
        print '  expect:\t', 1
        print '  output:\t', r
        print
        
def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)