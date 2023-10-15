import os


# The Missing Frame Finder is a script to help identify missing frame numbers within a specified frame range in a directory containing image files. 
# To ensure that all frames are present, especially when rendering many frames using a render farm. Occasionally,
# render farms may provide incomplete frames due to issues during rendering or downloading.

# Define the frame range.
frame_start = 1
frame_end = 250

# Define the directory where frame files are located.
frame_directory = "/mnt/c/Users/Workstation/Desktop/Data/Showreel 2023/Blender/Intro - Send to Render Farm - Style 1/Render/Cycles/Complete Style 1/Image/Part 1"
prefix_filename = "Intro - Send to Render Farm - Style 1"

# Create a set to store the frame numbers of existing frames.
existing_frames = set()

# Iterate through the files in the directory.
for filename in os.listdir(frame_directory):
    ### Using sufix filename.
    # Check if the file is a PNG image.
    if filename.endswith(".png"):
        # Extract the frame number from the end of the filename.
        # Assumes a four-digit frame number (e.g., 0001.png).
        frame_number = filename[-8:-4]
        if frame_number.isdigit():
            frame_number = int(frame_number)
            existing_frames.add(frame_number)

    # ### Using prefix_filename.
    # # Check if the filename matches the expected format.
    # if filename.startswith(prefix_filename) and filename.endswith(".png"):
    #     try:
    #         # Extract the frame number from the filename.
    #         # frame_number = int(filename.split(".")[-2])
    #         frame_number = int(filename.split("_")[-1].split(".")[0])
    #         existing_frames.add(frame_number)
    #     except ValueError:
    #         pass

### Consecutive Frame Sequence list.
# Find missing frames and group them.
missing_frames = []
current_range = []

for frame in range(frame_start, frame_end + 1):
    if frame not in existing_frames:
        current_range.append(frame)
    else:
        if current_range:
            missing_frames.append(current_range[:])
            current_range.clear()

# Check if there's a gap at the end.
if len(current_range) > 0:
    missing_frames.append(current_range)

# Print the missing frame numbers and ranges.
if missing_frames:
    print("Missing Frames Found:")
    for frame_range in missing_frames:
        if len(frame_range) == 1:
            print("{:04d}".format(frame_range[0]))
        else:
            print("{:04d}-{:04d}".format(frame_range[0], frame_range[-1]))
else:
    print("Congrats! No missing frames are found.")

# ### Individual Frame Sequence list.
# # Find missing frames.
# missing_frames = []

# for frame in range(frame_start, frame_end + 1):
#     if frame not in existing_frames:
#         missing_frames.append(frame)

# # Print the missing frame numbers and filenames.
# if missing_frames:
#     print("Missing Frames Found:")
#     for frame in missing_frames:
#         missing_filename = f"{prefix_filename}{frame:04d}.png"
#         print("{:04d}".format(frame))
# else:
#     print("Congrats! No missing frames are found.")
