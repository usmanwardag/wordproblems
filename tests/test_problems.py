import wordproblems.problems as problems
import wordproblems.data as data

class TestProblems(object):
	
	@classmethod
	def setup_class(self):
		self.text = data.level0()

	def test_basic(self):
		problems.solve(self.text)
