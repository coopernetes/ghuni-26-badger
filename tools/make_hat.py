"""
Put a hunter's hat and mask on the menu Mona.

Reads the original model from original-files/apps/menu/mona_menu.p3d and writes
apps/menu/mona_menu.p3d with three extra parts: "hat" (crown and front-pointing brim),
"hatwing" (the two torn wings that flare up at the back) and "mask" (the cloth over the lower
face). The menu moves every part except "torso" with the head, so they nod and sway with her
with no code changes.

The crown is fitted to the head from the model's own vertices and the mask is ray-cast onto the
face, so neither needs hand placement.

Run from the repo root:  python3 -I tools/make_hat.py
"""

import math
import struct

SOURCE = "original-files/apps/menu/mona_menu.p3d"
OUTPUT = "apps/menu/mona_menu.p3d"

SEGMENTS = 28
FRONT = math.pi / 2          # the face looks down +z; angles are measured as x = cos, z = sin
CENTRE_Z = 0.05              # the head is centred a little forward of the origin

# crown: half an ellipsoid sitting on the head, sized from the head's vertices
RIM_Y = 0.60                 # equator of the crown, just above the eyes (they top out at 0.33)
CROWN_HEIGHT = 0.95
CROWN_MARGIN = 1.05
CROWN_RINGS = 4

# brim: pointed at the front, folded up at the sides
BRIM_BASE = 0.22
BRIM_CORNER = 0.50
BRIM_FRONT_EXTRA = 0.45
BRIM_CURL = 0.30
BRIM_FRONT_DROOP = 0.22
BRIM_THICKNESS = 0.05

# wings: torn sheets at the two back corners
WING_SPREAD = 0.50           # half-width of the base, in radians around the head
WING_OUT = 0.85
WING_HEIGHT = 1.25
WING_TEETH = (0.95, 0.45, 1.10, 0.40, 1.20, 0.50, 0.90, 0.35, 0.65)
WING_BACK = math.radians(105)  # how far round from the front the wings sit

# mask: ray-cast onto the lower face
MASK_BOTTOM = -1.02
MASK_TOP_CENTRE = -0.40
MASK_TOP_DROP = 0.36
MASK_HALF_ANGLE = math.radians(100)
MASK_COLUMNS = 20
MASK_ROWS = 5
MASK_OFFSET = 0.055

HAT_RGB = (0x2a, 0x29, 0x2e)
WING_RGB = (0x56, 0x46, 0x3a)
MASK_RGB = (0x4a, 0x4a, 0x52)


class Builder:
    def __init__(self):
        self.vertices = []
        self.normals = []
        self.triangles = []

    def vertex(self, position, normal):
        length = math.sqrt(sum(c * c for c in normal)) or 1.0
        self.vertices.append(tuple(position))
        self.normals.append(tuple(c / length for c in normal))
        return len(self.vertices) - 1

    def triangle(self, a, b, c, convention):
        # wind the triangle so its geometric normal agrees with the vertex normals
        # (convention is +1 or -1, measured from the original model)
        pa, pb, pc = (self.vertices[i] for i in (a, b, c))
        u = [pb[k] - pa[k] for k in range(3)]
        v = [pc[k] - pa[k] for k in range(3)]
        geometric = (u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0])
        wanted = [sum(self.normals[i][k] for i in (a, b, c)) for k in range(3)]
        if sum(g * w for g, w in zip(geometric, wanted)) * convention < 0:
            b, c = c, b
        self.triangles.append((a, b, c))

    def quad(self, a, b, c, d, convention):
        self.triangle(a, b, c, convention)
        self.triangle(a, c, d, convention)

    def pack(self):
        positions = b"".join(struct.pack("<3f", *p) for p in self.vertices)
        normals = b"".join(struct.pack("<3f", *n) for n in self.normals)
        indices = b"".join(struct.pack("<3H", *t) for t in self.triangles)
        return len(self.vertices), len(self.triangles), positions, normals, indices


def read_model(path):
    data = open(path, "rb").read()
    magic, count = struct.unpack_from("<4sI", data, 0)
    if magic != b"P3D2":
        raise ValueError("expected a P3D2 model")
    parts = []
    for index in range(count):
        name, rgb, verts, tris, pos, nrm, idx, col = struct.unpack_from("<16sIIIIIII", data, 8 + 44 * index)
        parts.append({
            "name": name.rstrip(b"\0"), "rgb": rgb, "verts": verts, "tris": tris,
            "pos": data[pos:pos + verts * 12], "nrm": data[nrm:nrm + verts * 12],
            "idx": data[idx:idx + tris * 6], "col": data[col:col + verts * 4] if col else b"",
        })
    return parts


def mesh_of(part):
    flat = struct.unpack("<%df" % (part["verts"] * 3), part["pos"])
    points = [flat[i:i + 3] for i in range(0, len(flat), 3)]
    ids = struct.unpack("<%dH" % (part["tris"] * 3), part["idx"])
    return points, [ids[i:i + 3] for i in range(0, len(ids), 3)]


def winding_convention(parts):
    # +1 if the original triangles are wound so their geometric normal follows the stored normals
    body = next(p for p in parts if p["name"] == b"body")
    positions = struct.unpack("<%df" % (body["verts"] * 3), body["pos"])
    normals = struct.unpack("<%df" % (body["verts"] * 3), body["nrm"])
    indices = struct.unpack("<%dH" % (body["tris"] * 3), body["idx"])
    agree = 0
    for t in range(body["tris"]):
        a, b, c = indices[t * 3:t * 3 + 3]
        p = [positions[i * 3:i * 3 + 3] for i in (a, b, c)]
        u = [p[1][k] - p[0][k] for k in range(3)]
        v = [p[2][k] - p[0][k] for k in range(3)]
        g = (u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0])
        n = [sum(normals[i * 3 + k] for i in (a, b, c)) for k in range(3)]
        agree += 1 if sum(x * y for x, y in zip(g, n)) > 0 else -1
    return 1 if agree >= 0 else -1


def write_model(path, parts):
    header = 8 + 44 * len(parts)
    body = b""
    records = b""
    for part in parts:
        offsets = []
        for key in ("pos", "nrm", "idx", "col"):
            offsets.append(header + len(body) if part[key] else 0)
            body += part[key]
        records += struct.pack("<16sIIIIIII", part["name"], part["rgb"], part["verts"], part["tris"], *offsets)
    with open(path, "wb") as f:
        f.write(struct.pack("<4sI", b"P3D2", len(parts)) + records + body)


def part_from(name, mesh, rgb):
    verts, tris, pos, nrm, idx = mesh.pack()
    if verts > 65535:
        raise ValueError("too many vertices")
    return {"name": name.encode(), "rgb": (rgb[0] << 16) | (rgb[1] << 8) | rgb[2],
            "verts": verts, "tris": tris, "pos": pos, "nrm": nrm, "idx": idx, "col": b""}


def ray_hit(origin, direction, points, triangles):
    # farthest intersection of a ray with the head's triangles (Moller-Trumbore), or None
    best = None
    for a, b, c in triangles:
        p0, p1, p2 = points[a], points[b], points[c]
        e1 = [p1[k] - p0[k] for k in range(3)]
        e2 = [p2[k] - p0[k] for k in range(3)]
        h = (direction[1] * e2[2] - direction[2] * e2[1], direction[2] * e2[0] - direction[0] * e2[2],
             direction[0] * e2[1] - direction[1] * e2[0])
        det = sum(e1[k] * h[k] for k in range(3))
        if abs(det) < 1e-9:
            continue
        s = [origin[k] - p0[k] for k in range(3)]
        u = sum(s[k] * h[k] for k in range(3)) / det
        if u < 0 or u > 1:
            continue
        q = (s[1] * e1[2] - s[2] * e1[1], s[2] * e1[0] - s[0] * e1[2], s[0] * e1[1] - s[1] * e1[0])
        v = sum(direction[k] * q[k] for k in range(3)) / det
        if v < 0 or u + v > 1:
            continue
        t = sum(e2[k] * q[k] for k in range(3)) / det
        if t > 0 and (best is None or t > best):
            best = t
    return best


def fit_crown(points):
    # smallest ellipsoid half (equator at RIM_Y) that holds every head vertex above the rim
    radius_x = radius_z = 1.0
    scale = 1.0
    for x, y, z in points:
        if y < RIM_Y - 0.25:
            continue
        dy = max(0.0, y - RIM_Y) / CROWN_HEIGHT
        flat = (x / radius_x) ** 2 + ((z - CENTRE_Z) / radius_z) ** 2 + dy * dy
        scale = max(scale, math.sqrt(flat))
    return radius_x * scale * CROWN_MARGIN, radius_z * scale * CROWN_MARGIN


def build_hat(convention, radius_x, radius_z):
    mesh = Builder()
    angles = [i * 2 * math.pi / SEGMENTS for i in range(SEGMENTS)]

    def rim(angle):
        return (radius_x * math.cos(angle), RIM_Y, CENTRE_Z + radius_z * math.sin(angle))

    # crown dome
    ring_ids = []
    for k in range(CROWN_RINGS):
        alpha = (math.pi / 2) * k / CROWN_RINGS
        row = []
        for angle in angles:
            x = radius_x * math.cos(alpha) * math.cos(angle)
            z = CENTRE_Z + radius_z * math.cos(alpha) * math.sin(angle)
            y = RIM_Y + CROWN_HEIGHT * math.sin(alpha)
            normal = (x / radius_x ** 2, (y - RIM_Y) / CROWN_HEIGHT ** 2, (z - CENTRE_Z) / radius_z ** 2)
            row.append(mesh.vertex((x, y, z), normal))
        ring_ids.append(row)
    top = mesh.vertex((0.0, RIM_Y + CROWN_HEIGHT, CENTRE_Z), (0.0, 1.0, 0.0))
    for k in range(CROWN_RINGS - 1):
        for i in range(SEGMENTS):
            j = (i + 1) % SEGMENTS
            mesh.quad(ring_ids[k][i], ring_ids[k][j], ring_ids[k + 1][j], ring_ids[k + 1][i], convention)
    for i in range(SEGMENTS):
        mesh.triangle(ring_ids[-1][i], ring_ids[-1][(i + 1) % SEGMENTS], top, convention)

    # brim
    def corner(angle):
        return 0.5 + 0.5 * math.cos(3 * (angle - FRONT))

    def front(angle):
        return max(0.0, math.cos(angle - FRONT)) ** 4

    def brim_point(angle, fraction):
        base = rim(angle)
        reach = BRIM_BASE + BRIM_CORNER * corner(angle) ** 1.5 + BRIM_FRONT_EXTRA * front(angle)
        rise = BRIM_CURL * (1 - corner(angle)) - BRIM_FRONT_DROOP * front(angle)
        return (base[0] + math.cos(angle) * reach * fraction, base[1] + rise * fraction ** 2,
                base[2] + math.sin(angle) * reach * fraction)

    fractions = (0.0, 0.5, 1.0)
    for normal_y in (1.0, -1.0):
        grid = [[mesh.vertex(brim_point(angle, f), (0.0, normal_y, 0.0)) for f in fractions] for angle in angles]
        for i in range(SEGMENTS):
            j = (i + 1) % SEGMENTS
            for k in range(len(fractions) - 1):
                mesh.quad(grid[i][k], grid[j][k], grid[j][k + 1], grid[i][k + 1], convention)
    for i in range(SEGMENTS):
        j = (i + 1) % SEGMENTS
        edge = []
        for angle in (angles[i], angles[j]):
            high = brim_point(angle, 1.0)
            outward = (math.cos(angle), 0.0, math.sin(angle))
            edge.append((mesh.vertex(high, outward), mesh.vertex((high[0], high[1] - BRIM_THICKNESS, high[2]), outward)))
        (a, b), (c, d) = edge
        mesh.quad(a, c, d, b, convention)
    return mesh, brim_point


def build_wings(convention, brim_point, radius_x, radius_z):
    mesh = Builder()
    columns = len(WING_TEETH)
    for sign in (1, -1):
        centre = FRONT + sign * WING_BACK
        grid = []
        for c in range(columns):
            angle = centre + (c / (columns - 1) * 2 - 1) * WING_SPREAD
            radial = (math.cos(angle), 0.0, math.sin(angle))
            base = brim_point(angle, 0.9)
            tooth = WING_TEETH[c]
            column = []
            for row, (out, up) in enumerate(((0.0, 0.0), (WING_OUT * 0.45, WING_HEIGHT * 0.5), (WING_OUT, WING_HEIGHT * tooth))):
                column.append((base[0] + radial[0] * out, base[1] + up, base[2] + radial[2] * out, radial))
            grid.append(column)
        for facing in (1.0, -1.0):
            ids = []
            for column in grid:
                ids.append([mesh.vertex(p[:3], (p[3][0] * facing, 0.3 * facing, p[3][2] * facing)) for p in column])
            for c in range(columns - 1):
                for r in range(2):
                    mesh.quad(ids[c][r], ids[c + 1][r], ids[c + 1][r + 1], ids[c][r + 1], convention)
    return mesh


def build_mask(convention, points, triangles):
    mesh = Builder()
    grid = []
    for c in range(MASK_COLUMNS + 1):
        angle = -MASK_HALF_ANGLE + 2 * MASK_HALF_ANGLE * c / MASK_COLUMNS
        direction = (math.sin(angle), 0.0, math.cos(angle))
        top = MASK_TOP_CENTRE - MASK_TOP_DROP * (abs(angle) / MASK_HALF_ANGLE) ** 1.3
        column = []
        for r in range(MASK_ROWS + 1):
            y = top + (MASK_BOTTOM - top) * r / MASK_ROWS
            origin = (0.0, y, CENTRE_Z)
            reach = ray_hit(origin, direction, points, triangles) or 0.9
            drape = MASK_OFFSET * (1 + 0.8 * r / MASK_ROWS)
            position = tuple(origin[k] + direction[k] * (reach + drape) for k in range(3))
            column.append(mesh.vertex(position, direction))
        grid.append(column)
    for c in range(MASK_COLUMNS):
        for r in range(MASK_ROWS):
            mesh.quad(grid[c][r], grid[c + 1][r], grid[c + 1][r + 1], grid[c][r + 1], convention)
    return mesh


if __name__ == "__main__":
    original = [p for p in read_model(SOURCE)]
    convention = winding_convention(original)
    head_points, head_triangles = [], []
    for part in original:
        if part["name"] in (b"body", b"face"):
            points, tris = mesh_of(part)
            head_triangles += [tuple(i + len(head_points) for i in t) for t in tris]
            head_points += points
    radius_x, radius_z = fit_crown(head_points)
    hat_mesh, brim_point = build_hat(convention, radius_x, radius_z)
    added = [
        part_from("hat", hat_mesh, HAT_RGB),
        part_from("hatwing", build_wings(convention, brim_point, radius_x, radius_z), WING_RGB),
        part_from("mask", build_mask(convention, head_points, head_triangles), MASK_RGB),
    ]
    write_model(OUTPUT, original + added)
    print("crown radii x %.2f z %.2f" % (radius_x, radius_z))
    for part in added:
        print("%-8s %4d verts %4d tris" % (part["name"].decode(), part["verts"], part["tris"]))
    print("model total", sum(p["tris"] for p in original + added), "tris, was", sum(p["tris"] for p in original))
