import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):

    def setUp(self):
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'C++', 'Java']

    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn('English', self.my_survey.responses)

    def test_store_three_response(self):
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        for response in self.responses:
            my_survey.store_response(response)
            self.assertIn(response, my_survey.responses)


if __name__ == '__main__':
    unittest.main()