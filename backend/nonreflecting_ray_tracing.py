import matplotlib.pyplot as plt
import numpy as np
import math as mt

def quad_solver(a, b, c):
    det = b**2 - 4*a*c
    if det < 0:
        raise ValueError("No real roots")
    elif det == 0:
        return -b / (2*a), -b / (2*a)
    else:
        return (-b - mt.sqrt(det)) / (2*a), (-b + mt.sqrt(det)) / (2*a)


def normalize(angle):
    return angle % (2 * mt.pi)

def is_angle_between(angle, start, end):
    angle = normalize(angle)
    start = normalize(start)
    end = normalize(end)
    if start < end:
        return start <= angle <= end
    else:
        return angle >= start or angle <= end


def nonreflecting_plotter(a = 20, b = 20, r = 15, ray_count = 50):
    if a == 0 and b == 0:
        raise ValueError("Circle center cannot be at the origin (0, 0).")

    max_dim = max(abs(a), abs(b), r) * 3
    fig, ax = plt.subplots()
    ax.set_xlim(-max_dim, max_dim)
    ax.set_ylim(-max_dim, max_dim)
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')

    ax.axhline(0, color='black', lw=1)
    ax.axvline(0, color='black', lw=1)
    
    circle = plt.Circle((a, b), r, color='blue', fill=False)
    ax.add_artist(circle)

    def draw_line(angle, length=max(max_dim, 500), x_0=0, y_0=0):
        x_1 = length * mt.cos(angle) + x_0
        y_1 = length * mt.sin(angle) + y_0
        return [x_0, x_1], [y_0, y_1]

    
    theta_center = mt.atan2(b, a)
    d = mt.hypot(a, b)
    
    try:
        delta = mt.asin(r / d)
    except:
        raise ValueError("Circle radius is too large for the given center coordinates.")
    
    lower_angle = theta_center - delta
    upper_angle = theta_center + delta

    lower_angle = normalize(lower_angle)
    upper_angle = normalize(upper_angle)    

    increment = 2*mt.pi/ray_count

    for angle in np.arange(0, 2 * mt.pi, increment):  # 1° steps
        dx = mt.cos(angle)
        dy = mt.sin(angle)
        if is_angle_between(angle, lower_angle, upper_angle):
            # continue
            A = dx**2 + dy**2
            B = -2 * (a * dx + b * dy)
            C = a**2 + b**2 - r**2
    
            try:
                t1, t2 = quad_solver(A, B, C)
                if abs(t1) < abs(t2):
                    t_hit = t1
                else:
                    t_hit = t2
                # t_hit = min(t1, t2)
                if t_hit < 0:
                    continue  
                x = [0, t_hit * dx]
                y = [0, t_hit * dy]
                ax.plot(x, y, color='orange', lw=1)
            except ValueError:
                continue 
        else:
            x, y = draw_line(angle)
            ax.plot(x, y, color='red', lw=1)

    x1, y1 = draw_line(lower_angle)
    x2, y2 = draw_line(upper_angle)

    ax.plot(x1, y1, color='green', lw=2, linestyle='--')
    ax.plot(x2, y2, color='green', lw=2, linestyle='--')
    
    ax.set_title(f'Rays with shadow from a perfectly absorbing circle at ({a},{b}) with radius {r}')
    plt.grid(True)
    plt.show()

    fig.canvas.draw()
    image_array = np.array(fig.canvas.renderer.buffer_rgba())
    plt.close(fig)
    return image_array