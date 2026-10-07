"""Заготовки задач на NumPy."""

import numpy as np
from grader_contracts.numpy_tasks import (
    BinarizeInput, ChessInput, EllipseInput, MatrixInput, MatrixStatistics,
    MatrixVectorBatchInput, OneHotInput, RandomMatrixInput, RectangleInput,
    TimeSeriesInput, TimeSeriesStatistics,
)


def sum_prod(data: MatrixVectorBatchInput) -> np.ndarray:
    matrices, vectors = data.matrices, data.vectors
    a = matrices[0] @ vectors[0]
    for i in range(1, len(matrices)):
        a+=(matrices[i] @ vectors[i])
    return a

print(sum_prod(MatrixVectorBatchInput(matrices=[np.array([[1, 2], [3, 4]]), np.array([[2, 0], [1, 3]])], vectors=[np.array([[1], [3]]), np.array([[4], [1]])])))
print(sum_prod(MatrixVectorBatchInput(matrices=[np.array([[1, 5], [2, 1]]), np.array([[4, 0], [0, 1]])],vectors=[np.array([[2], [1]]), np.array([[1], [1]])])))

def binarize(data: BinarizeInput) -> np.ndarray:
    matrix, threshold = data.matrix, data.threshold
    a = (matrix > threshold).astype(int)
    return a

print(binarize(BinarizeInput(matrix=np.array([[0.5, 1.2], [2.1, 0.0]]), threshold=1.0)))
print(binarize(BinarizeInput(matrix=np.array([[-1, 2], [0, 5]]), threshold=0.0)))

def unique_rows(data: MatrixInput) -> list[list[float]]:
    matrix = data.matrix
    a =[]
    for i in matrix:
        s = np.unique(i)
        a.append(s.tolist())
    return a

print(unique_rows(MatrixInput(matrix=np.array([[1, 1, 2], [3, 3, 3]]))))

def unique_columns(data: MatrixInput) -> list[list[float]]:
    matrix = data.matrix
    a =[]
    tmatrix =matrix.T
    for j in tmatrix:
        s = np.unique(j)
        a.append(s.tolist())
    return a

print(unique_columns(MatrixInput(matrix=np.array([[1, 1, 2], [3, 3, 3]]))))

def matrix_statistics(data: RandomMatrixInput) -> MatrixStatistics:
    rows, columns, mean, std, seed = data.rows, data.columns, data.mean, data.std, data.seed
    rng = np.random.default_rng(seed)
    a = rng.normal(loc=mean, scale=std, size=(rows, columns))
    m1 = np.mean(a, axis=1)
    m2 = np.mean(a, axis=0)
    v1 = np.var(a, axis=1)
    v2 = np.var(a, axis=0)
    return MatrixStatistics(matrix=a, row_means=m1, column_means=m2, row_variances=v1, column_variances=v2)

print(matrix_statistics(RandomMatrixInput(rows=2, columns=3, mean=0.0, std=1.0, seed=42)).matrix)
print(matrix_statistics(RandomMatrixInput(rows=3, columns=2, mean=10.0, std=2.0, seed=123)).matrix)

def chess(data: ChessInput) -> np.ndarray:
    rows, columns, first, second = data.rows, data.columns, data.first, data.second
    a = np.zeros((rows, columns))
    for i in range(rows):
        for j in range(columns):
            if (i + j) % 2 == 0:
                a[i, j] = first
            else:
                a[i, j] = second
                
    return a

print(chess(ChessInput(rows=3, columns=4, first=0, second=1)))
print(chess(ChessInput(rows=2, columns=2, first=5, second=9)))

def draw_rectangle(data: RectangleInput) -> np.ndarray:
    width, height = data.width, data.height
    image_height, image_width = data.image_height, data.image_width
    shape_color, background_color = data.shape_color, data.background_color
    a = np.zeros((image_height, image_width, 3), dtype=np.uint8)
    a[...] = background_color
    cy = image_height // 2
    cx = image_width // 2
    y_start = max(0, cy - height // 2)
    y_end = min(image_height, cy + (height + 1) // 2)
    x_start = max(0, cx - width // 2)
    x_end = min(image_width, cx + (width + 1) // 2)
    a[y_start:y_end, x_start:x_end] = shape_color
    return a

print(draw_rectangle(RectangleInput(width=4, height=4, image_height=10, image_width=10, shape_color=(255, 0, 0), background_color=(0, 0, 0))))
print(draw_rectangle(RectangleInput(width=2, height=4, image_height=6, image_width=6, shape_color=(0, 255, 0), background_color=(255, 255, 255))))

def draw_ellipse(data: EllipseInput) -> np.ndarray:
    semi_axis_x, semi_axis_y = data.semi_axis_x, data.semi_axis_y
    image_height, image_width = data.image_height, data.image_width
    shape_color, background_color = data.shape_color, data.background_color
    a = np.zeros((image_height, image_width, 3), dtype=np.uint8)
    for i in range(image_height):
        for j in range(image_width):
            a[i, j] = background_color
    cy = image_height // 2
    cx = image_width // 2
    for i in range(image_height):
        for j in range(image_width):
            e = ((j - cx) ** 2) / (semi_axis_x ** 2) + ((i - cy) ** 2) / (semi_axis_y ** 2)
            if e <= 1:
                a[i, j] = shape_color

    return a

print(draw_ellipse(EllipseInput(semi_axis_x=2, semi_axis_y=2, image_height=8, image_width=8, shape_color=(255, 255, 0), background_color=(128, 128, 128))))

def analyze_time_series(data: TimeSeriesInput) -> TimeSeriesStatistics:
    values, window = data.values, data.window
    m = np.mean(values)
    d = np.var(values)
    s = np.std(values)
    lmax = []
    lmin= []
    for i in range(1, len(values) - 1):
        a1 = values[i - 1]
        a2 = values[i]
        a3 = values[i + 1]
        if a2>a1 and a2>a3:
            lmax.append(i)
        if a2<a1 and a2<a3:
            lmin.append(i)
    ma = []
    num= len(values)
    for i in range(num - window + 1):
        cw = values[i : i + window]
        w = np.mean(cw)
        ma.append(w)
    maarray = np.array(ma)

    return TimeSeriesStatistics(mean=m,variance=d,std=s,local_maxima_indices=lmax,local_minima_indices=lmin,moving_average=maarray)

print(analyze_time_series(TimeSeriesInput(values=np.array([1.0, 3.0, 2.0, 5.0, 1.0]), window=2)))
print(analyze_time_series(TimeSeriesInput(values=np.array([1.0, 4.0, 2.0, 8.0, 3.0, 9.0]), window=3)))

def one_hot(data: OneHotInput) -> np.ndarray:
    labels, class_count = data.labels, data.class_count
    if class_count is None:
        class_count = np.max(labels)+1
    a = np.zeros((len(labels), class_count), dtype=int)
    for i in range(len(labels)):
        class_label = labels[i]
        a[i, class_label] = 1

    return a
    
print(one_hot(OneHotInput(labels=np.array([0, 2, 3, 0]), class_count=None)))
print(one_hot(OneHotInput(labels=np.array([1, 0, 2]), class_count=4)))