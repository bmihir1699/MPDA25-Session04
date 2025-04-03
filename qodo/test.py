<<<<<<< HEAD
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
=======


# make a funcion that gets a joke from the internet
def get_joke():
    import requests
    response = requests.get('https://icanhazdadjoke.com')
    if response.status_code == 200:
        return response.json()['joke']
    else:
        return "Failed to retrieve joke"


get_joke()

>>>>>>> e124991b982e8e4977e01390ffbe4000cbef2125
