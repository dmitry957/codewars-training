def dropzone(p, dropzones):
    return min(dropzones, key=lambda dz: (p[0] - dz[0])**2 + (p[1] - dz[1])**2)