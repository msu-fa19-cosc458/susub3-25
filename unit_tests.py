import unittest
import functions

class ChatBotResponseTest(unittest.TestCase):
    def test_not_command(self):
        response = functions.get_chatbot_response("Purple")
        self.assertEquals(response, "")
        
    def test_add_command(self):
        response = functions.get_chatbot_response("!! add 2 2")
        self.assertEquals(response, 4)
        
    def test_divide_command(self):
        response = functions.get_chatbot_response("!! divide 2 2")
        self.assertEquals(response, 1)

if __name__ == '__main__':
    unittest.main()