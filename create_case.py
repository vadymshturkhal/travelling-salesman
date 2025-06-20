# --- A more robust way to create the problem file ---
# This avoids any formatting issues from multiline strings
name = "n=8"
tsp_content = (
    f"NAME: {name}\n"
    "TYPE: TSP\n"
    "COMMENT: A simple 8-city problem in a rectangular layout\n"
    "DIMENSION: 8\n"
    "EDGE_WEIGHT_TYPE: EUC_2D\n"
    "NODE_COORD_SECTION\n"
    " 1 0 0\n"
    " 2 30 0\n"
    " 3 60 0\n"
    " 4 60 40\n"
    " 5 60 80\n"
    " 6 30 80\n"
    " 7 0 80\n"
    " 8 0 40\n"
    "EOF\n"
)

with open(f"{name}.tsp", 'w') as f:
    f.write(tsp_content)
