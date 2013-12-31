"""read input file containing multiple loops as sequential x,y,z and output individual loops"""
from __future__ import print_function
print("loading numeric libraries...")
import numpy as np
import os
import shutil

# RUNTIME OPTIONS
INPUT_FILE = os.path.join('3D-ALL', '3D-(SCAD)z(mod).txt')
POINT_SEPARATION_THRESHOLD = 1 # maximum distance between points in a sequence (mm)
SECTION_SEPARATION_THRESHOLD = 2 # maximum distance between endpoints (mm)
VISUALIZE = True # display generated loops? (True/False)
VERBOSE = True # include detailed program output? (True/False)
OVERWRITE = False # overwrite output directory if exists? (True/False)

if VISUALIZE:
    print("loading visualization libraries...")
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D

def read_points_from_file(input_file):
    """read x,y,z from text file into numpy array"""
    with open(input_file, 'r') as f:
        lines = f.readlines()
    points = np.zeros((len(lines), 3))
    for i, line in enumerate(lines):
        points[i] = list(float(x.strip()) for x in line.strip().split(','))
    return points

def calculate_interpoint_distances(points):
    """calculate distance between each point in numpy array"""
    point_distances = np.zeros(points.shape[0]) # first entry will always be zero
    point_distances[1:] = np.sqrt(np.sum(np.diff(points, axis=0)**2, axis=1))
    return point_distances

def extract_loop_sections(points, point_distances):
    """identify loop sections based on point distances"""
    loop_start_locations = np.where(point_distances>POINT_SEPARATION_THRESHOLD)[0]
    point_indices = np.arange(point_distances.shape[0])
    list_of_loop_indices = np.split(point_indices, loop_start_locations)
    if VERBOSE:
        endpts = [0]
        for i in loop_start_locations:
            endpts.append(i-1)
            endpts.append(i)
        endpts.append(point_indices[-1])
        mindist = [min(distance(points[i], points[x]) for x in endpts if not i==x) for i in endpts]
        print("min distances to matching section endpoint:")
        print(mindist)
        print("suggested SECTION_SEPARATION_THRESHOLD:", np.ceil(max(mindist)))
    return [points[loop_indices, :] for loop_indices in list_of_loop_indices]

def distance(x, y):
    """calculate distance between two points"""
    return np.sqrt(np.sum((y-x)**2))

def normalize_axes(ax):
    """plot all axes at the same resolution"""
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    zlim = ax.get_zlim()
    if (xlim[1]-xlim[0] > ylim[1]-ylim[0]) and (xlim[1]-xlim[0] > zlim[1]-zlim[0]):
        radius = (xlim[1]-xlim[0])/2
        y_center = (ylim[1]+ylim[0])/2
        ax.set_ylim([y_center-radius, y_center+radius])
        z_center = (zlim[1]+zlim[0])/2
        ax.set_zlim([z_center-radius, z_center+radius])
    elif (ylim[1]-ylim[0] > xlim[1]-xlim[0]) and (ylim[1]-ylim[0] > zlim[1]-zlim[0]):
        radius = (ylim[1]-ylim[0])/2
        x_center = (xlim[1]+xlim[0])/2
        ax.set_xlim([x_center-radius, x_center+radius])
        z_center = (zlim[1]+zlim[0])/2
        ax.set_zlim([z_center-radius, z_center+radius])
    else:
        radius = (zlim[1]-zlim[0])/2
        x_center = (xlim[1]+xlim[0])/2
        ax.set_xlim([x_center-radius, x_center+radius])
        y_center = (ylim[1]+ylim[0])/2
        ax.set_ylim([y_center-radius, y_center+radius])

def get_loops_from_sections(loop_sections):
    """stitch loop sections together"""
    loops = []
    while len(loop_sections):
        section = loop_sections.pop(0) # remove section from list for tentative storage
        begin = section[0]
        end = section[-1]
        # see if ends meet. if so, save loop
        if distance(begin, end) < SECTION_SEPARATION_THRESHOLD: # done if ends meet
            section.append(section[0]) # copy beginning of loop to end
            loops.append(section)
            if VERBOSE: print(" ", len(loops), "loops extracted,", len(loop_sections), "loop sections remaining")
        # otherwise, stitch to an adjacent section
        else:
            if VERBOSE: print(" ", len(loops), "loops extracted,", len(loop_sections), "loop sections remaining")
            for i in range(len(loop_sections)):
                other_begin = loop_sections[i][0]
                other_end = loop_sections[i][-1]
                if distance(end, other_begin) < SECTION_SEPARATION_THRESHOLD:
                    # append other section
                    if VERBOSE: print("  stitching segment to end")
                    section = np.concatenate((section, loop_sections.pop(i)))
                    break
                elif distance(end, other_end) < SECTION_SEPARATION_THRESHOLD:
                    # append other section, reversed
                    if VERBOSE: print("  stitching reversed segment to end")
                    section = np.concatenate((section, np.array(list(reversed(loop_sections.pop(i))))))
                    break
                elif distance(begin, other_end) < SECTION_SEPARATION_THRESHOLD:
                    # prepend other section
                    if VERBOSE: print("  stitching segment to beginning")
                    section = np.concatenate((np.array(list(reversed(loop_sections.pop(i)))), section))
                    break
                elif distance(begin, other_begin) < SECTION_SEPARATION_THRESHOLD:
                    # prepend other section, reversed
                    if VERBOSE: print("  stitching reversed segment to beginning")
                    section = np.concatenate((loop_sections.pop(i), section))
                    break
            loop_sections.insert(0, section) # re-add section to list after stitching
    return loops

def plot_loop(loop, loop_num):
    """plot loop as 3D scatterplot"""
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(loop[:, 0], loop[:, 1], loop[:, 2])
    ax.set_xlabel('mm')
    ax.set_ylabel('mm')
    ax.set_zlabel('mm')
    ax.set_title('loop ' + str(loop_num))
    normalize_axes(ax)
    plt.show(block=False)
    pass

if __name__ == '__main__':
    print("loading points...")
    points = read_points_from_file(INPUT_FILE)
    print("calculating interpoint distances...")
    point_distances = calculate_interpoint_distances(points)
    print("identifying loop sections...")
    loop_sections = extract_loop_sections(points, point_distances)
    print("stitching adjacent sections...")
    loops = get_loops_from_sections(loop_sections)
    if VISUALIZE:
        print("visualizing extracted loops...")
        for i, loop in enumerate(loops):
            plot_loop(loop, i+1)
    output_dir = ''.join(INPUT_FILE.split('.')[:-1]) + '_loops'
    if OVERWRITE:
        if os.path.exists(output_dir):
            shutil.rmtree(output_dir)
    else:
        if os.path.exists(output_dir):
            i = 2
            while os.path.exists(output_dir + '_' + ('%02d' % i)):
                i += 1
            output_dir += '_' + ('%02d' % i)
    os.makedirs(output_dir)
    print("writing individual loops to output directory:", output_dir)
    for i, loop in enumerate(loops):
        output_file_name = os.path.join(output_dir, 'loop' + '_' + ('%02d' % (i+1)) + '.txt')
        with open(output_file_name, 'w') as f:
            for point in loop:
                f.write(str(point[0]) + ', ' + str(point[1]) + ', ' + str(point[2]) + '\n')
    print("writing complete.")
    if VISUALIZE:
        print("(close all open figures to exit program)")
        plt.show()