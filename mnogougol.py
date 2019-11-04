import math


def point_connect_figure_area(work_point: list, figure_points: list) -> float:
    res = 0.0
    for i in range(len(figure_points) // 2):
        if i == len(figure_points) // 2 - 1:
            res += triangle_area(work_point, figure_points[i * 2:i * 2 + 2], figure_points[0:2])
        else:
            res += triangle_area(work_point, figure_points[i * 2:i * 2 + 2],
                                 figure_points[i * 2 + 2:i * 2 + 4])
    return res


def triangle_area(a: list, b: list, c: list) -> float:
    return 0.5 * math.fabs((b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1]))


def is_inside(points: list) -> bool:
    work_point = points[:2]
    figure_points = points[2:]
    center_point = [sum(figure_points[::2]) * 2 / len(figure_points), sum(figure_points[1::2]) * 2 / len(figure_points)]
    figure_area = point_connect_figure_area(center_point, figure_points)
    new_figure_area = point_connect_figure_area(work_point, figure_points)
    return True if figure_area == new_figure_area else False
