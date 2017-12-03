import os.path
import unittest

import dartpy as dart


class TestUrdfParser(unittest.TestCase):
    def test_parse_skeleton(self):
        root_path = os.path.join(os.path.dirname(__file__), 'data')
        cube_path = os.path.join(root_path, 'urdf', 'cube.urdf')

        urdf_loader = dart.utils.DartLoader()
        cube = urdf_loader.parseSkeleton(cube_path)

        self.assertIsNotNone(cube)
        self.assertEqual(cube.getNumBodyNodes(), 1)
        self.assertEqual(cube.getNumJoints(), 1)
        self.assertEqual(cube.getNumDofs(), 6)
        self.assertIsNotNone(cube.getRootBodyNode(0))


if __name__ == '__main__':
    unittest.main()
