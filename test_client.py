import unittest
import client

class TestPrototype(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.animationInstance = client.Animation()
        cls.communicationInstance = client.Communication()
        cls.connectionInstance = client.Connection()
        cls.uiInstance = client.UI()

    def test_inputs(self):
        self.uiInstance.openSetup()

        self.assertEqual('10', '10')

#if __name__ == '__main__':
    #unittest.main()c
