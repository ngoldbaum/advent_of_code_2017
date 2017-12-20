import numpy as np

with open('input', 'r') as f:
    data = [t.strip().split(', ') for t in f.readlines()]

positions = np.array([
    list(map(int, d[0].lstrip('p=<').rstrip('>').split(','))) for d in data])
velocities = np.array([
    list(map(int, d[1].lstrip('v=<').rstrip('>').split(','))) for d in data])
accelerations = np.array([
    list(map(int, d[2].lstrip('a=<').rstrip('>').split(','))) for d in data])

for i in range(int(100)):
    print(i, positions.shape[0])
    velocities += accelerations
    positions += velocities
    unique_pos, inds, unique_counts = np.unique(
        positions, axis=0, return_inverse=True, return_counts=True)
    if unique_counts.max() > 1:
        wh = np.where(unique_counts[inds] == 1)[0]
        positions = positions[wh]
        velocities = velocities[wh]
        accelerations = accelerations[wh]

mpos = np.abs(positions).sum(axis=1)
wh = np.where(mpos == mpos.min())
print(wh[0])
