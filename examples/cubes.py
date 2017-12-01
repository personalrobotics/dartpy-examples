import dartpy as dart
import os.path
import sys
from OpenGL.GLUT import *

if __name__ == '__main__':
    world = dart.simulation.World()

    root_path = os.path.join(os.path.dirname(__file__), 'data')
    cube_path = os.path.join(root_path, 'urdf', 'cube.urdf')

    urdf_loader = dart.utils.DartLoader()
    cube = urdf_loader.parseSkeleton(cube_path)
    world.addSkeleton(cube)

    glutInit(sys.argv)
    viewer = dart.gui.SimWindow()
    viewer.initWindow(640, 480, 'Cubes')
    # viewer.setWorld(world)
    glutMainLoop()
