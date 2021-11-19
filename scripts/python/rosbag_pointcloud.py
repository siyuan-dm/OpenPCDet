
"""Extract images from a rosbag.
"""

import argparse
import rosbag
import numpy as np
import os
import ros_numpy


def main():
    """Extract a folder of images from a rosbag.
    """
    parser = argparse.ArgumentParser(description="Extract images from a ROS bag.")
    parser.add_argument("bag_file", help="Input ROS bag.")
    parser.add_argument("output_dir", help="Output file.")
    parser.add_argument("topic", help="topic.")

    args = parser.parse_args()

    print("Extract %s with topic %s into %s" % (args.bag_file, args.topic, args.output_dir))

    bag = rosbag.Bag(args.bag_file, "r")
    for topic, msg, t in bag.read_messages(topics=[args.topic]):
        cur_ts = t.to_nsec()
        print(cur_ts)
        data = ros_numpy.point_cloud2.pointcloud2_to_xyz_array(msg)
        npy_file = os.path.join(args.output_dir, str(cur_ts) + ".npy")
        final_data = np.zeros((len(data), 4))
        final_data[:, :3] = data
        np.save(npy_file, final_data) 
            
    bag.close()

    return

if __name__ == '__main__':
    main()
