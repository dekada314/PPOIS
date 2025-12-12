import sys

import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

rot_angle = 0.0
VERTICES = np.array([
    [-1, -1, -1], [ 1, -1, -1], [ 1,  1, -1], [-1,  1, -1],
    [-1, -1,  1], [ 1, -1,  1], [ 1,  1,  1], [-1,  1,  1]
], dtype=float)

EDGES = np.array([
    [0, 1], [1, 2], [2, 3], [3, 0],
    [4, 5], [5, 6], [6, 7], [7, 4],
    [0, 4], [1, 5], [2, 6], [3, 7]
], dtype=int)

FACES = np.array([
    [0, 3, 2, 1], 
    [4, 5, 6, 7], 
    [0, 4, 7, 3], 
    [1, 2, 6, 5], 
    [0, 1, 5, 4], 
    [3, 2, 6, 7]  
], dtype=int)

BLUE_FILL = (0.19, 0.31, 0.8)  
WHITE_LINE = (1.0, 1.0, 1.0)   

def draw_cube(size, fill_color, line_color, alpha):
    """
    Рисует куб заданного размера с заполнением и каркасом.
    """
    
    glPushMatrix()
    glScalef(size, size, size) 
    
    if alpha > 0.0:
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        
        glColor4f(fill_color[0], fill_color[1], fill_color[2], alpha)
        
        glBegin(GL_QUADS)
        for face in FACES:
            for vertex_index in face:
                glVertex3fv(VERTICES[vertex_index])
        glEnd()
        
        glDisable(GL_BLEND)

    
    glColor3f(line_color[0], line_color[1], line_color[2])
    glLineWidth(2.5) 

    glBegin(GL_LINES)
    for edge in EDGES:
        for vertex_index in edge:
            glVertex3fv(VERTICES[vertex_index])
    glEnd()
    
    glPopMatrix()

def display():
    global rot_angle
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
    glRotatef(rot_angle, 0.5, 1.0, 0.0) 

    draw_cube(
        size=0.7, 
        fill_color=BLUE_FILL, 
        line_color=WHITE_LINE, 
        alpha=0.6 
    )
    draw_cube(
        size=0.35, 
        fill_color=(0.0, 0.0, 0.0), 
        line_color=WHITE_LINE, 
        alpha=0.0 
    )
    glutSwapBuffers()

def update_rotation(value):
    global rot_angle
    rot_angle += 0.5 
    if rot_angle > 360:
        rot_angle -= 360
    glutPostRedisplay()
    glutTimerFunc(16, update_rotation, 0) 

def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    aspect = width / height
    if width <= height:
        glOrtho(-1.5, 1.5, -1.5 / aspect, 1.5 / aspect, -10.0, 10.0)
    else:
        glOrtho(-1.5 * aspect, 1.5 * aspect, -1.5, 1.5, -10.0, 10.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 800)
    glutCreateWindow(b"Exact Nested Translucent Cube")
    
    glClearColor(0.0, 0.0, 0.0, 1.0) 
    glEnable(GL_DEPTH_TEST) 
    
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutTimerFunc(16, update_rotation, 0)
    glutMainLoop()

if __name__ == '__main__':
    main()