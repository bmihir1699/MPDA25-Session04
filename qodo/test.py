import Rhino.Geometry as rg

def create_building(base_point, width, depth, height):
    """
    Creates a building using RhinoCommon.

    Parameters:
    - base_point: The base point of the building (rg.Point3d).
    - width: The width of the building.
    - depth: The depth of the building.
    - height: The height of the building.

    Returns:
    - A Rhino.Geometry.Extrusion object representing the building.
    """
    base = rg.Rectangle3d(rg.Plane.WorldXY, width, depth)
    base.Translate(base_point)
    building = rg.Extrusion.Create(base.ToNurbsCurve(), height, True)
    return building
