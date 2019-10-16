import unittest
import functions

class ChatBotResponseTest(unittest.TestCase):
    def test_not_command(self):
        # response = functions.get_chatbot_response("Purple")
        response = functions.get_chatbot_response("!! add 5 3")
        print(response)
        self.assertEquals(response, 8)
        
        
        response = functions.get_chatbot_response("!! divide 5 3")
        print(response)
        self.assertEquals(response, 1)

if __name__ == '__main__':
    unittest.main()