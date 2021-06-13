import unittest
import base64
import requests

class APITestCase(unittest.TestCase):

    def test_equal_img(self):
        url = 'http://apimeme.com/meme?meme=Alarm-Clock&top=Top+text&bottom=Bottom+text'

        with open('example.jpg', 'rb') as img_1:
            img_base = base64.b64encode(img_1.read()).decode('utf-8')

        request_img = requests.get(url)
        img_base2 = base64.b64encode(request_img.content).decode('utf-8')

        self.assertEqual(img_base, img_base2)


if __name__ == '__main__':
    unittest.main()
