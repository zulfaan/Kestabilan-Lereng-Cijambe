from numpy import array
from pybimstab.slope import NaturalSlope
from pybimstab.bim import BlocksInMatrix
from pybimstab.slipsurface import CircularSurface, TortuousSurface
from pybimstab.slices import MaterialParameters, Slices
from pybimstab.slopestabl import SlopeStabl
terrainCoords = array([[-10, -9.0331, -8.0153, -6.0305, 2.0102, 3.028, 3.0789, 3.486, 3.9949, 3.9949,
                        6.0305, 6.5394, 6.9975, 8.0153, 9.0331, 10],
                       [20.0509, 20.0509, 18.9822, 15.063613, 15.012723, 13.028, 9.9237, 8.6514, 7.2265,
                        6.056, 4.987, 4.478, 4.02, 3.969, 2.952, 0]])
slope = NaturalSlope(terrainCoords)
bim = BlocksInMatrix(slopeCoords=slope.coords, blockProp=0.15,
                     tileSize=0.8, seed=1)
preferredPath = CircularSurface(
    slopeCoords=slope.coords, dist1=5, dist2=17, radius=16)
surface = TortuousSurface(
    bim, dist1=10, dist2=15.5, heuristic='euclidean',
    reverseLeft=False, reverseUp=False, smoothFactor=2,
    preferredPath=preferredPath.coords, prefPathFact=2)
material = MaterialParameters(
    cohesion=2.46, frictAngle=55.18, unitWeight=12.99,
    blocksUnitWeight=None, wtUnitWeight=9.8)
slices = Slices(
    material=material, slipSurfCoords=surface.coords,
    slopeCoords=slope.coords, numSlices=10, bim=bim)
stabAnalysis = SlopeStabl(slices, seedFS=1, Kh=0)
fig = stabAnalysis.plot()
