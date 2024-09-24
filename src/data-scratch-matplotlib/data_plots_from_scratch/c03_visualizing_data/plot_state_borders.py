import re
from os.path import abspath, dirname

from matplotlib import pyplot as plt


def read_lines(file_path):
    with open(file_path, "r") as f:
        lines = [line for line in f]
    return lines


def lines_to_segments(lines):
    lat_long_regex = r"<point lat=\"(.*)\" lng=\"(.*)\""
    segments = []
    points = []
    for line in lines:
        if line.startswith("</state>"):
            for p1, p2 in zip(points, points[1:]):
                segments.append((p1, p2))
            points = []
        s = re.search(lat_long_regex, line)
        if s:
            lat, lon = s.groups()
            points.append((float(lon), float(lat)))
    return segments


def plot_state_borders(segments, color="0.8"):
    for (lon1, lat1), (lon2, lat2) in segments:
        plt.plot([lon1, lon2], [lat1, lat2], color=color)


if __name__ == "__main__":
    current_dir = abspath(dirname(__file__))
    data_dir = abspath(f"{current_dir}/../../../data")
    lns = read_lines(file_path=f"{data_dir}/states.txt")
    sgmts = lines_to_segments(lns)
    plot_state_borders(segments=sgmts)
