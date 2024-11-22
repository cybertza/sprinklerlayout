import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

# Define garden dimensions
garden_width = 5  # meters
garden_length = 15  # meters

# Define sprinkler radius
sprinkler_radius = 5  # meters

# Custom sprinkler positions array
# Format: [name, posx, posy, type, color]
sprinklers = [
    # ["Quarter 3 (Q3)", 0, 7.5, "q5", "blue"],
   ["Quarter 1 (Q1)", 0, 0, "q1", "#ff6347"],  # Tomato
["Quarter 3 (Q2)", 0, 5, "q2", "#4682b4"],  # Steel Blue
["Half Bottom (HB)", 5, 0, "ht", "#32cd32"],  # Lime Green
["Half Bottom (HB)", 5, 5, "hb", "#ff4500"],  # Orange Red
["Half Bottom (HB)", 10, 0, "ht", "#8a2be2"],  # Blue Violet
["Half Bottom (HB)", 10, 5, "hb", "#daa520"],  # Goldenrod
["Half Bottom (HB)", 15, 5, "q3", "#ff69b4"],  # Hot Pink
["Half Bottom (HB)", 15, 0, "q4", "#9932cc"],  # Dark Orchid

    # ["Full Circle (FC)", 12.5, 2.5, "circle", "blue"]
]

# Custom sprinkler positions
def place_custom_sprinkler(ax, sprinkler):
    name, x, y, sprinkler_type, color = sprinkler
    if 0 <= x <= garden_length and 0 <= y <= garden_width:
        ax.text(garden_length + 1, y, name, fontsize=9, color=color, verticalalignment='center')
        ax.text(garden_length + 1, y, name, fontsize=9, color=color, verticalalignment='center')
        
        if sprinkler_type.lower().startswith('q'):  # Quarter circle
            direction = sprinkler_type[1].lower()
            if direction == '1':
                arc = patches.Arc((x, y), 2 * sprinkler_radius, 2 * sprinkler_radius, theta1=0, theta2=90, color=color, alpha=0.5, linewidth=3)
                ax.add_patch(arc)
            elif direction == '2':
                arc = patches.Arc((x, y), 2 * sprinkler_radius, 2 * sprinkler_radius, theta1=270, theta2=360, color=color, alpha=0.5, linewidth=3)
                ax.add_patch(arc)
            elif direction == '3':
                arc = patches.Arc((x, y), 2 * sprinkler_radius, 2 * sprinkler_radius, theta1=180, theta2=270, color=color, alpha=0.5, linewidth=3)
                ax.add_patch(arc)
            elif direction == '4':
                arc = patches.Arc((x, y), 2 * sprinkler_radius, 2 * sprinkler_radius, theta1=90, theta2=180, color=color, alpha=0.5, linewidth=3)
                ax.add_patch(arc)

        elif sprinkler_type.lower().startswith('h'):  # Half circle
            direction = sprinkler_type[1].lower()
            if direction == 't':  # Top
                arc = patches.Arc((x, y), 2 * sprinkler_radius, 2 * sprinkler_radius, theta1=0, theta2=180, color=color, alpha=0.3, linewidth=3)
                ax.add_patch(arc)
            elif direction == 'b':  # Bottom
                arc = patches.Arc((x, y), 2 * sprinkler_radius, 2 * sprinkler_radius, theta1=180, theta2=360, color=color, alpha=0.3, linewidth=3)
                ax.add_patch(arc)
            elif direction == 'l':  # Left
                arc = patches.Arc((x, y), 2 * sprinkler_radius, 2 * sprinkler_radius, theta1=90, theta2=270, color=color, alpha=0.3, linewidth=3)
                ax.add_patch(arc)
            elif direction == 'r':  # Right
                arc = patches.Arc((x, y), 2 * sprinkler_radius, 2 * sprinkler_radius, theta1=-90, theta2=90, color=color, alpha=0.3)
                ax.add_patch(arc)

        elif sprinkler_type.lower() == 'circle':  # Full circle
            circle = plt.Circle((x, y), sprinkler_radius, color=color, alpha=0.1)
            ax.add_artist(circle)

# Create figure
fig, ax = plt.subplots(figsize=(10, 5))

# Draw garden boundary
ax.plot([0, garden_length, garden_length, 0, 0], [0, 0, garden_width, garden_width, 0], color="green", lw=2, label="Garden Boundary")

# Place custom sprinklers
for sprinkler in sprinklers:
    place_custom_sprinkler(ax, sprinkler)

# Set plot limits
ax.set_xlim(-1, garden_length + 1)
ax.set_ylim(-1, garden_width + 1)

# Labels and grid
ax.set_title("Custom Irrigation Layout Plan")
ax.set_xlabel("Length (meters)")
ax.set_ylabel("Width (meters)")
ax.grid(color="gray", linestyle="--", linewidth=0.5)
ax.legend(loc="upper right")
ax.set_aspect('equal')

# Show the plot
plt.show()
