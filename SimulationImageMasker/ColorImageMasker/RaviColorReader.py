import numpy as np
import hoomd
import freud
import gsd.hoomd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
import time
import csv
from PIL import Image
from matplotlib.animation import FuncAnimation, FFMpegWriter

img = Image.open('/Users/ravigautam/Documents/Passive_WCA2/Monalisa.png')

width, height = img.size
center_x, center_y = int(width/2), int(height/2)
square_size = min(width, height)

left = center_x - int(square_size/2)
top = center_y - int(square_size/2)
right = center_x + int(square_size/2)
bottom = center_y + int(square_size/2)

cropped_img = img.crop((left, top, right, bottom))

#cropped_img.show()
cropped_img

box_size = 100;
frames = np.arange(0, 999, 20)

phi1 = 62.0
# filename = f'HS_Cryst_Simulation_phi{phi1}_T1.0_sample1.0.gsd'
filename = f'/Users/ravigautam/Documents/Active_Doping/Doping_phi{75.0}_alpha{5.0}_Active{100.0}_sample{1}.gsd'
traj = gsd.hoomd.open(name=filename, mode='r')
frame = traj[980]
position = frame.particles.position
x = position[:, 0]
y = position[:, 1]
Np = len(position)

cropped_array = np.array(cropped_img)
red = cropped_array[:, :, 0]
green = cropped_array[:, :, 1]
blue = cropped_array[:, :, 2]

width, height = cropped_img.size

y1 = np.rint((x - box_size / 2) * width / box_size).astype(int)
x1 = np.rint((y - box_size / 2) * height / box_size).astype(int)
r = []
g = []
b = []

for i in range(Np):
    r.append(red[x1[i]][y1[i]])
    g.append(green[x1[i]][y1[i]])
    b.append(blue[x1[i]][y1[i]])

color = np.stack((r, g, b), axis=1) / 255

plt.figure(figsize=(10, 10))
scatter = plt.scatter(x, -y, s=25, marker='o', c=color)
plt.xlim(-box_size / 2, box_size / 2)
plt.ylim(-box_size / 2, box_size / 2)
plt.axis('equal')
plt.axis('off')
plt.title('Final look', fontsize=20)
plt.show()


frame = traj[0]
position = frame.particles.position
x = position[:,0]
y = position[:,1]

plt.figure(figsize=(10, 10))
scatter = plt.scatter(x, -y, s=25, marker='o', c=color)
plt.xlim(-box_size/2, box_size/2)
plt.ylim(-box_size/2, box_size/2)
plt.axis('equal')
plt.axis('off')
plt.title('Initial look',fontsize=20)
plt.show()

fig = plt.figure(figsize=(10, 10))


def update(f):
    frame = traj[int(frames[f])]
    position = frame.particles.position
    x = position[:, 0]
    y = position[:, 1]

    plt.cla()
    scatter = plt.scatter(x, -y, s=50, marker='o', c=color)
    plt.xlim(-box_size / 2, box_size / 2)
    plt.ylim(-box_size / 2, box_size / 2)
    plt.axis('equal')
    plt.axis('off')


plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
ani = FuncAnimation(fig, update, frames=len(frames), blit=False)
writer = FFMpegWriter(fps=10, metadata=dict(artist='Me'), bitrate=-1)
ani.save('/Users/ravigautam/Documents/Passive_WCA2/Monalisa.mp4', writer=writer)
plt.show()

dia = 1  # Radius of the outer circle
num_rounds = 4  # Number of concentric circles

points = []
points.append((0, 0))
# Generate points for each concentric circle
for r in np.linspace(0, dia / 2, num_rounds):
    perimeter = 2 * np.pi * r
    points_in_round = int(perimeter / (dia / 10))
    angles = np.linspace(0, 2 * np.pi, points_in_round, endpoint=False)
    for angle in angles:
        x = r * np.cos(angle)
        y = r * np.sin(angle)
        points.append((x, y))

box_size = 100;
frames = np.arange(0, 999, 20)

filename = f'/Users/ravigautam/Documents/Active_Doping/Doping_phi{75.0}_alpha{5.0}_Active{100.0}_sample{1}.gsd'
traj = gsd.hoomd.open(name=filename, mode='r')
frame = traj[980]
position = frame.particles.position
x = position[:, 0]
y = position[:, 1]
Np = len(position)

cropped_array = np.array(cropped_img)
red = cropped_array[:, :, 0]
green = cropped_array[:, :, 1]
blue = cropped_array[:, :, 2]

width, height = cropped_img.size

points = np.array(points)
N = Np * len(points)  # numner of points
shifted_position = []

for i in position:
    for j in points:
        new_point = (j[0] + i[0], j[1] + i[1])
        shifted_position.append(new_point)

shifted_position = np.array(shifted_position)
shifted_x = shifted_position[:, 0]
shifted_y = shifted_position[:, 1]

y2 = np.rint(-(np.array(shifted_x) - box_size / 2) * width / box_size).astype(int)
x2 = np.rint(-(np.array(shifted_y) - box_size / 2) * height / box_size).astype(int)
r = []
g = []
b = []

x2[x2 >= width - 1] = width - 1
y2[y2 >= height - 1] = height - 1
for i in range(N):
    r.append(red[x2[i]][y2[i]])
    g.append(green[x2[i]][y2[i]])
    b.append(blue[x2[i]][y2[i]])

color = np.stack((r, g, b), axis=1) / 255

plt.figure(figsize=(10, 10))
scatter = plt.scatter(-shifted_x, shifted_y, s=0.2, marker='o', c=color)
plt.xlim(-box_size / 2, box_size / 2)
plt.ylim(-box_size / 2, box_size / 2)
plt.axis('equal')
plt.axis('off')
plt.title('Final look', fontsize=20)
plt.show()



frame = traj[0]
position = frame.particles.position
x = position[:,0]
y = position[:,1]

shifted_position = []

for i in position:
    for j in points:
        new_point = (j[0] + i[0], j[1] + i[1])
        shifted_position.append(new_point)

shifted_position = np.array(shifted_position)
shifted_x = shifted_position[:,0]
shifted_y = shifted_position[:,1]

plt.figure(figsize=(10, 10))
scatter = plt.scatter(-shifted_x, shifted_y, s=0.1, marker='o', c=color)
plt.xlim(-box_size/2, box_size/2)
plt.ylim(-box_size/2, box_size/2)
plt.axis('equal')
plt.axis('off')
plt.title('Initial look',fontsize=20)
plt.show()

fig = plt.figure(figsize=(10, 10))


def update(f):
    frame = traj[int(frames[f])]
    position = frame.particles.position
    x = position[:, 0]
    y = position[:, 1]
    shifted_position = []

    for i in position:
        for j in points:
            new_point = (j[0] + i[0], j[1] + i[1])
            shifted_position.append(new_point)

    shifted_position = np.array(shifted_position)
    shifted_x = shifted_position[:, 0]
    shifted_y = shifted_position[:, 1]

    plt.cla()
    scatter = plt.scatter(-shifted_x, shifted_y, s=0.1, marker='o', c=color)
    plt.xlim(-box_size / 2, box_size / 2)
    plt.ylim(-box_size / 2, box_size / 2)
    plt.axis('equal')
    plt.axis('off')


plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
ani = FuncAnimation(fig, update, frames=len(frames), blit=False)
writer = FFMpegWriter(fps=10, metadata=dict(artist='Me'), bitrate=-1)
ani.save('/Users/ravigautam/Documents/Passive_WCA2/Monalisa_refined.mp4', writer=writer)
plt.show()