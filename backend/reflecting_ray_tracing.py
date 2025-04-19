import matplotlib.pyplot as plt
import numpy as np
import math as mt

def reflect_vector(v, n):
    n = n / np.linalg.norm(n)
    return v - 2 * np.dot(v, n) * n

def plot_reflection_on_circle(ax, angle, center, radius, ray_length=50, color='blue'):
    a, b = center
    origin = np.array([0, 0])
    dx = np.cos(angle)
    dy = np.sin(angle)

    A = dx**2 + dy**2 
    B = -2 * (a * dx + b * dy)
    C = a**2 + b**2 - radius**2

    roots = np.roots([A, B, C])
    ts = [t for t in roots if t > 0]
    if not ts:
        print(f"No intersection at angle {angle}")
        return

    t_hit = min(ts)
    x_hit = t_hit * dx
    y_hit = t_hit * dy
    hit_point = np.array([x_hit, y_hit])

    ax.plot([0, x_hit], [0, y_hit], color='blue', lw=1, zorder=10) # This is the incident ray
    
    normal_vector = hit_point - np.array([a, b]) #Normal at point of reflection
    # ax.plot([a, x_hit], [b, y_hit], color='green', lw=1)

    # Reflection, this is key
    incident_vector = hit_point - origin
    reflected_vector = reflect_vector(incident_vector, normal_vector)
    reflected_unit = 1000* reflected_vector / np.linalg.norm(reflected_vector)

    ax.arrow(x_hit, y_hit,
             reflected_unit[0] * ray_length,
             reflected_unit[1] * ray_length,
             head_width=1.8, head_length=1.5,
             fc=color, ec=color, zorder=10)

    return incident_vector, reflected_vector



def reflecting_plotter(a = 20, b = 20, r = 15, ray_count = 15):
    max_dim = max(abs(a), abs(b), r) * 3
    fig, ax = plt.subplots()
    ax.set_xlim(-max_dim, max_dim)
    ax.set_ylim(-max_dim, max_dim)
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    
    circle = plt.Circle((a, b), r, color='black', fill=False)
    ax.add_artist(circle)
    
    theta_center = mt.atan2(b, a)
    d = mt.hypot(a, b)
    
    try:
        delta = mt.asin(r / d)
    except:
        raise ValueError("Circle radius is too large for the given center coordinates.")
    
    lower_angle = theta_center - delta
    upper_angle = theta_center + delta
    
    def normalize(angle):
        return angle % (2 * mt.pi)
    
    lower_angle = normalize(lower_angle)
    upper_angle = normalize(upper_angle)
    
    def is_angle_between(angle, start, end):
        angle = normalize(angle)
        start = normalize(start)
        end = normalize(end)
        if start < end:
            return start <= angle <= end
        else:
            return angle >= start or angle <= end
    
        # Function to generate a line from origin at a given angle
    def draw_line(angle, length=max(max_dim, 500), x_0=0, y_0=0):
        x_1 = length * mt.cos(angle) + x_0
        y_1 = length * mt.sin(angle) + y_0
        return [x_0, x_1], [y_0, y_1]
    
    increment = 2*mt.pi/increment
    for angle in np.arange(0, 2 * np.pi, increment):
        dx = mt.cos(angle)
        dy = mt.sin(angle)
        if is_angle_between(angle, lower_angle, upper_angle):
            plot_reflection_on_circle(ax, angle, center=(a, b), radius=r)
        
        else:
            x, y = draw_line(angle)
            ax.plot(x, y, color='red', lw=1, zorder=5)
    # plot_reflection_on_circle(ax, angle, center=(a, b), radius=r)
    
    plt.show()
    fig.canvas.draw()
    image_array = np.array(fig.canvas.renderer.buffer_rgba())
    plt.close(fig)
    return image_array