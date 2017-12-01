import dartpy as dart
import numpy as np
import unittest

class TestCreateWorld(unittest.TestCase):
    def test_create_world(self):
        world = dart.simulation.World()
        self.assertIsNotNone(world)

        world.setTimeStep(0.01)
        self.assertEqual(world.getTimeStep(), 0.01)

        gravity = np.zeros((3, 1))
        world.setGravity(gravity)
        self.assertTrue((world.getGravity() == gravity).all())

if __name__ == '__main__':
    unittest.main()
